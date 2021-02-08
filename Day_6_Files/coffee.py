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
print(df_thin_name)

# make columns into lists
# column_name = "Country of Origin" or "Producer" or "Processing Method"
for column_name in df_thin_name:
    column_name_simple = df_thin_name[column_name].dropna().unique()

    counts = df_thin_name[column_name].value_counts()

    yvalues = []
    for element in column_name_simple:
        yvalues.append(counts.loc[element])

    data = [
        go.Bar(
            x=column_name_simple,
            y=yvalues
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text="coffee arabica",
                      xaxis=dict(
                          title=str(column_name)
                      ),
                      yaxis=dict(
                          title="# of " + str(column_name)
                      ))
    fig.show()

