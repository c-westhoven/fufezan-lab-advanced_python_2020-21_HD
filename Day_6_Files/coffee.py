import pandas as pd
import plotly.graph_objects as go

# What to do
# Read dataset into a dataframe
# Drop all columns except country.of.origin, producer, and processing.method, and rename them
# clean data set --> which columns have extreme outliers
# plotly histogram, write a loop?
# clean outliers: classify outliers for each column, set outliers to median
csv = "../data/arabica_data_cleaned.csv"

# read file
df = pd.read_csv(csv)
# Unnamed: O column, comes from the csv file: header is ""

# drop columns except for named above
list = df.columns.difference(["Country.of.Origin", "Producer", "Processing.Method"])

df_thin = df.drop(df.columns.difference(["Country.of.Origin", "Producer", "Processing.Method"]), 1)

# rename
df_thin_name = df_thin.rename(columns={"Country.of.Origin": "Country of Origin", "Processing.Method": "Processing Method"})

# make columns into lists
# column_name = "Country of Origin" or "Producer" or "Processing Method"
for column_name in df_thin_name:
    list_elements = df_thin_name[column_name].dropna().unique()

    counts = df_thin_name[column_name].value_counts()   # series

    yvalues = []
    for element in list_elements:       # ex country in list of countries
        yvalues.append(counts.loc[element])

    # classifiying outliers
    # set outliers to median
    median = float(counts.median())
    yvalues_amend = []
    for element in list_elements:       # country in list of countries
        if counts.loc[element] > counts.quantile(.9):   # larger than 9th quantile
            yvalues_amend.append(median)
        elif counts.loc[element] < counts.quantile(.1):     # smaller than 1st quantile
            yvalues_amend.append(median)
        else:
            yvalues_amend.append(counts.loc[element])

    data = [
        go.Bar(
            x=list_elements,
            y=yvalues
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text="Coffee Arabica",
                      xaxis=dict(
                          title=str(column_name)
                      ),
                      yaxis=dict(
                          title=str(column_name) + " Counts"
                      ))
    fig.show()

    data = [
        go.Bar(
            x=list_elements,
            y=yvalues_amend
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text="Coffee Arabica Amended",
                      xaxis=dict(
                          title=str(column_name)
                      ),
                      yaxis=dict(
                          title=str(column_name) + " Counts"
                      ))
    fig.show()

    # * Which countries have more than 10 and less than 30 entries?
    if column_name == "Country of Origin":
        more10less30 = []
        for element in list_elements:
            if 30 > counts.loc[element] > 10:
                more10less30.append(element)
        print("Countries with >10 but <30 entries: ", more10less30)

    # * Which is the producer with most entries?
    elif column_name == "Producer":
        maxprod = counts.idxmax()
        print("The producer with the most entries is: ", maxprod)

    # * What is the mosts common and least common "Processing Method"
    elif column_name == "Processing Method":
        most_common = counts.idxmax()
        least_common = counts.idxmin()
        print("Most common processing method: ", most_common, "Least common processing method: ", least_common)



