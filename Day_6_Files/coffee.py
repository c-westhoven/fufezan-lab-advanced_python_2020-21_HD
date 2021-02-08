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


# plotting: how do you plot this? these aren't numbers
# make columns into lists
countries = df_thin_name["Country of Origin"].dropna().unique()
prod = df_thin_name["Producer"].unique().tolist()
process = df_thin_name["Processing Method"].unique().tolist()

# print(countries)

number_countries = df_thin_name["Country of Origin"].value_counts()
number_producers = df_thin_name["Producer"].value_counts()
number_process = df_thin_name["Processing Method"].value_counts()

print(type(number_countries)) # Series

yvalues = []
for country in countries:
    yvalues.append(number_countries.loc[country])


# country against country
data = [
    go.Bar(
        x=countries,
        y=yvalues
    )
]
fig = go.Figure(data=data)
fig.update_layout(title_text="coffee arabica",
                  xaxis=dict(
                      title="countries"
                  ),
                  yaxis=dict(
                      title="# of countries"
                  ))
fig.show()

