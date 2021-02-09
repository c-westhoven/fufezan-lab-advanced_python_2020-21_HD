import ssl
import json
import urllib.request
import pandas as pd
import plotly.express as px


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


def create_hist(df, xaxis="", yaxis=""):
    df = px.df.deaths_weekly()
    fig = px.histogram(df, x=xaxis, y=yaxis)
    fig.show()
    return


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



