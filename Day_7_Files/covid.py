import ssl
import json
import urllib.request
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime, timedelta
pio.renderers.default = "browser"
import numpy as np
import plotly.express as px
from collections import deque
from statistics import mean

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


# def find_incidence_rate(df):
#     """
#     given the data frame, it looks at 14d incidence of each country, and divides highest - lowest incidence/ by time difference between measurements
#     :param df:
#     :return:
#     """
#     array_countries = list(df["countries_terr"].unique())
#     list_continents = list(df["continents"].unique())
#
#     dictionary = {}
#     for pos, country in enumerate(array_countries):
#         incidences = df[["countries_terr", "14d_incidence"]].groupby(["countries_terr"]).get_group((array_countries[pos]))
#         max_inc = max(incidences["14d_incidence"])
#         min_inc = min(incidences["14d_incidence"])
#         max_time = df.date_rep[df["14d_incidence"].idxmax]
#         min_time = df.date_rep[df["14d_incidence"].idxmin]
#         time_diff = (max_time - min_time)/timedelta(days=1)
#         dictionary[str(country)] = float(max_inc - min_inc) / time_diff
#     return dictionary


def find_inc_rate_cont(df):
    data = []
    data2 = []

    # df['year'] = df['date_rep'].year

    for continent, cont_grp in df.groupby("continent"):
        for country, country_group in cont_grp.groupby("countries_terr"):
            for year, year_group in country_group.groupby("year"):
                diffs = year_group.set_index("delta_time").sort_index()["14d_incidence"].diff().fillna(0)
                max_diffs = float(max(diffs))
                min_diffs = float(min(diffs))
                data.append([continent, country, year, max_diffs, min_diffs])
    fdf = pd.DataFrame(data, columns=["continent", "country", "year", "max_diffs", "min_diffs"])
    fdf["max_diffs"] = pd.to_numeric(fdf["max_diffs"])
    fdf["min_diffs"] = pd.to_numeric(fdf["min_diffs"])

    for continent, cont_grp in fdf.groupby("continent"):
        for year, year_grp in cont_grp.groupby("year"):
            country_max = fdf["country"].iloc[year_grp["max_diffs"].idxmax]
            country_min = fdf["country"].iloc[year_grp["min_diffs"].idxmin]
            max_diff_cont = max(year_grp.max_diffs)
            min_diff_cont = min(year_grp.min_diffs)
            data2.append([continent, year, country_max, max_diff_cont, country_min, min_diff_cont])
    incidence = pd.DataFrame(data2,
                             columns=["continent", "year", "country_max", "max_diff", "country_min", "min_diff"])
    return incidence


def find_inc_rate(df):
    data = []
    data2 = []
    for continent, cont_grp in df.groupby("continent"):
        for country, country_group in cont_grp.groupby("countries_terr"):
            for year, year_group in country_group.groupby("year"):
                diffs = year_group.set_index("delta_time").sort_index()["14d_incidence"].diff().fillna(0)
                max_diffs = float(max(diffs))
                min_diffs = float(min(diffs))
                data.append([continent, country, year, max_diffs, min_diffs])
    fdf = pd.DataFrame(data, columns=["continent", "country", "year", "max_diffs", "min_diffs"])
    fdf["max_diffs"] = pd.to_numeric(fdf["max_diffs"])
    fdf["min_diffs"] = pd.to_numeric(fdf["min_diffs"])

    for year, year_group in fdf.groupby("year"):
        country_max = fdf["country"].iloc[year_group["max_diffs"].idxmax]
        country_min = fdf["country"].iloc[year_group["min_diffs"].idxmin]
        max_diff_cont = max(year_group.max_diffs)
        min_diff_cont = min(year_group.min_diffs)
        data2.append([year, country_max, max_diff_cont, country_min, min_diff_cont])
    incidence = pd.DataFrame(data2, columns=["year", "country_max", "max_diff", "country_min", "min_diff"])

    return incidence


def find_inc_rate_cont_plot(df, continent="Europe"):
    cont_group = df.groupby("continent").get_group(continent)
    fig = go.Figure()
    for country, country_group in cont_group.groupby("countries_terr"):
        country_incid = country_group.set_index("delta_time").sort_index()["14d_incidence"]
        dates = country_group.set_index("delta_time").sort_index()["date_rep"]

        fig.add_trace(go.Scatter(x=dates, y=country_incid,
                             mode='lines',
                             name= country))

    fig.update_layout(title="14d incidences in" + str(continent))
    fig.layout.xaxis.title = "Time"
    fig.layout.yaxis.title = "14d_incidence"
    fig.show()
    return


def inc_cont_plot_smooth(df, continent="Europe"):
    smoothed_cont_group = df.groupby("continent").get_group(continent).copy()
    smoothed_cont_group_14d = smoothed_cont_group["14d_incidence"].rolling(window=13, center = True).mean()
    smoothed_cont_group["smoothed_14d_inc"]= smoothed_cont_group_14d
    smoothed_cont_group = smoothed_cont_group.groupby(["countries_terr"])

    fig = go.Figure()

    for pos, country in enumerate(list(smoothed_cont_group["countries_terr"].unique())):
        smoothed_country = smoothed_cont_group.get_group(country).sort_values("delta_time")

        # country_window.append(country_group.set_index("delta_time").sort_index()["14d_incidence"])
        # date_window = date_window.append(country_group.set_index("delta_time").sort_index()["date_rep"])        # Series
        # incid_threemonths.append(mean(country_window))

        fig.add_trace(go.Scatter(x=smoothed_country["date"], y=smoothed_country["smoothed_14d_inc"],
                             mode='lines',
                             name= country))

    fig.update_layout(title="14d incidences in" + str(continent))
    fig.layout.xaxis.title = "Time"
    fig.layout.yaxis.title = "14d_incidence"
    fig.show()
    return


def create_radial_plot(df, list_of_countries):
    fig = go.Figure()

    for country in list_of_countries:
        r_values = []
        theta_values = []
        current_country = df.groupby("countries_terr").get_group(country)

        # only keep rows for measurements within first year since start of measurement:
        current_country_firstyear = current_country[current_country["delta_time"] < 365]        ## different format?

        for row in range(current_country_firstyear.shape[0]):
            r_values.append(current_country_firstyear.iloc[row, 12])  # death_per population
            theta_values.append(current_country_firstyear.iloc[row, 13] * 360)  # percent*grad

        fig.add_trace(go.Scatterpolargl(r=r_values,
                                        theta=theta_values,
                                        name=country,
                                        mode='markers'))

    fig.update_layout(title={"text": "death rate per 100,000 people in first year measuring",
                      "font": {"size": 20}}
                      )
    fig.update_layout(title_xref='paper')  # titel ned so weit links
    # fig.update_layout(legend_x=0.8)  # legende weiter links
    fig.update_polars(radialaxis_title_text="death rate")
    fig.update_polars(angularaxis_tickmode='array')
    # fig.update_polars(angularaxis_tickvals=[0, 41.425, 82.849, 124.274, 165.699, 207.123, 248.550, 289.973, 331.397])  # an den Stellen gibts ticks
    # fig.update_polars(angularaxis_ticktext=["0 weeks since start of measurements", 6, 12, 18, 24, 30, 36, 42, 48])  # Beschriftung für die ticks

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
                              "continentExp":"continent", "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000":"14d_incidence"})        # they renamed the 14d incidence to cumulative number not notification rate
    # also possibly renamed cases_weekly and deaths_weekly

    cdf.info()
    # 14d_incidence is Dtype object and not a float
    # date also objects

    cdf["14d_incidence"] = pd.to_numeric(cdf["14d_incidence"])  #turns column datatype to float64
    cdf.info()

    # datetime objects
    cdf["date_rep"] = pd.to_datetime(cdf["date"], format="%d/%m/%Y", errors="raise")   # added column date_rep with datetime version of column date

    # add new column with time since start of recording
    cdf = delta_time(cdf, "date_rep", "delta_time")

    # add another column year, with just the year of the data
    for i in range(cdf.shape[0]):
        cdf.loc[i, 'year'] = cdf.loc[i, 'date_rep'].year

    # describe dataframe
    described = cdf.describe()
    # there are negative min values in cases_weekly, deaths_weekly, and 14d_incidence
    # neg values can also be seen in histogram
    # create_hist(cdf, "cases_weekly", "cases weekly")
    # create_hist(cdf, "deaths_weekly", "deaths weekly")
    # create_hist(cdf, "14d_incidence", "14d")

    # clean (delete negative values and their rows)
    cdf_clean = delete_neg_rows(cdf, "cases")
    cdf_clean = delete_neg_rows(cdf_clean, "deaths")
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

    # most drastic increase and decrease:
    # by continent per year
    incidence_df_cont = find_inc_rate_cont(cdf_clean)
    # by world per year
    incidence_gen = find_inc_rate(cdf_clean)

    # line plot for 14d_incidences for all European, groupby to generate data list for plotly plot
    plot_europe = find_inc_rate_cont_plot(cdf_clean, continent="Europe")

    # line plot smoothed version average 3 months
    plot_europe_smooth = inc_cont_plot_smooth(cdf_clean, continent="Europe")        # doesn't work

    # radial plot
    list_of_countries = ["Greece", "Italy", "Sweden", "Germany"]
    create_radial_plot(cdf_clean, list_of_countries)


