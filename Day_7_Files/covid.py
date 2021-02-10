import ssl
import json
import urllib.request
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime, timedelta
pio.renderers.default = "browser"

def url_to_df(url):
    covid_json_unformated = urllib.request.urlopen(url).read().decode("utf-8")
    covid_json = json.loads(covid_json_unformated)
    cdf = pd.DataFrame(covid_json['records'])
    return cdf


# def rename(df, oldname, newname):
#     df = df.rename(columns={str(oldname): str(newname)})
#     return df

def delta_time(df, date_time_column, newname):
    """
    adds column to data frame, finding oldest date_time of given column and subtracting the times of each column from the min time
    returns dataframe
    :param df:
    :param date_time_column:
    :param newname:
    :return:
    """
    # find min
    minidx = df[str(date_time_column)].idxmin()
    df[newname] = df[date_time_column] - df[date_time_column].iloc[minidx]
    return df


def create_hist(df, column, title="", xaxis="", yaxis=""):
    data = [
        go.Histogram(
            x=df[column]
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title=title)
    fig.layout.xaxis.title=xaxis
    fig.layout.yaxis.title=yaxis
    fig.show()
    return


def delete_neg_rows(df, column):
    """
    deletes rows that have neg or NaN elements in a column
    no inplace, so original df still contains bad elements
    :param df:
    :param column:
    :return: clean_df
    """
    if column == "date_rep":
        listidx = df.index[df[column] > df.loc[0, "date_rep"].now()].tolist()
        df_del = df.drop(labels=listidx, axis=0)
        df_clean = df_del.dropna()
    else:
        listidx = df.index[df[column] < 0].tolist()
        df_del = df.drop(labels=listidx, axis=0)
        df_clean = df_del.dropna()
    return df_clean


def find_incidence_rate(df):
    """
    given the data frame, it looks at 14d incidence of each country, and divides highest - lowest incidence/ by time difference between measurements
    :param df:
    :return:
    """
    array_countries = list(df["countries_terr"].unique())
    list_continents = list(df["continents"].unique())

    dictionary = {}
    for pos, country in enumerate(array_countries):
        incidences = df[["countries_terr", "14d_incidence"]].groupby(["countries_terr"]).get_group((array_countries[pos]))
        max_inc = max(incidences["14d_incidence"])
        min_inc = min(incidences["14d_incidence"])
        max_time = df.date_rep[df["14d_incidence"].idxmax]
        min_time = df.date_rep[df["14d_incidence"].idxmin]
        time_diff = (max_time - min_time)/timedelta(days=1)
        dictionary[str(country)] = float(max_inc - min_inc) / time_diff
    return dictionary


def find_inc_rate(df):
    data = []
    data2 = []
    for continent, cont_grp in df.groupby("continent"):
        for country, country_group in cont_grp.groupby("countries_terr"):
            diffs = country_group.set_index("delta_time").sort_index()["14d_incidence"].diff().fillna(0)
            max_diff = max(diffs)
            min_diff = min(diffs)
            data.append([continent, country, max_diff, min_diff])
    fdf = pd.DataFrame(data, columns=["continent", "country", "max_diff", "min_diff"])
    for continent, cont_grp in fdf.groupby("continent"):

        data2.append([continent, country, incidence, min_or_max])
    fdf2 = pd.DataFrame(data2, columns=["continent", "country", "incidence", "min or max"])
    return fdf2


    # test = cdf_clean[["continent", "countries_terr", "14d_incidence"]].groupby(["countries_terr"]).get_group(("China"))
    # maxim = max(test["14d_incidence"])
    # test.get_group(("China"))



if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    covid_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    cdf = url_to_df(covid_url)

    oldname = "dateRep"
    newname = "date"
    cdf = cdf.rename(columns={"dateRep": "date", "countriesAndTerritories":"countries_terr", "geoId": "geo_id",
                              "countryterritoryCode":"geo_code", "popData2019":"pop_data_2019",
                              "continentExp":"continent", "notification_rate_per_100000_population_14-days":"14d_incidence"})

    cdf.info()
    # 14d_incidence is Dtype object and not a float
    # date also objects

    cdf["14d_incidence"] = pd.to_numeric(cdf["14d_incidence"])  #turns column datatype to float64
    cdf.info()

    # datetime objects
    cdf["date_rep"] = pd.to_datetime(cdf["date"])   # added column date_rep with datetime version of column date

    # add new column with time since start of recording
    cdf = delta_time(cdf, "date_rep", "delta_time")

    # describe dataframe
    described = cdf.describe()
    # there are negative min values in cases_weekly, deaths_weekly, and 14d_incidence
    # neg values can also be seen in histogram
    # create_hist(cdf, "cases_weekly", "cases weekly")
    # create_hist(cdf, "deaths_weekly", "deaths weekly")
    # create_hist(cdf, "14d_incidence", "14d")

    # clean (delete negative values and their rows)
    cdf_clean = delete_neg_rows(cdf, "cases_weekly")
    cdf_clean = delete_neg_rows(cdf_clean, "deaths_weekly")
    cdf_clean = delete_neg_rows(cdf_clean, "14d_incidence")
    cdf_clean = delete_neg_rows(cdf_clean, "pop_data_2019")
    cdf_clean = delete_neg_rows(cdf_clean, "date_rep")

    # cleaned hists
    # create_hist(cdf_clean, "cases_weekly", "cases weekly")
    # create_hist(cdf_clean, "deaths_weekly", "deaths weekly")
    # create_hist(cdf_clean, "14d_incidence", "14d")

    # countries, grouped by continent which show most drastic increase and decrease of 14d incidence
    cdf_group = cdf_clean.groupby("continent").describe()
    grp = cdf_clean[["continent", "countries_terr", "14d_incidence", "date_rep"]].groupby("continent")
    # grp.head()

    # idea how o define most drastic increase and decrease
    # look at each country, find min 14d incidence and max 14d incidence and divide by times difference of incidence == out of this find highest and lowest

    print(cdf_group)

    test = find_inc_rate(cdf_clean)


