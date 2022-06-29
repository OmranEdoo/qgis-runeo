import pandas as pd
import plotly_express as px

url = "https://www.dropbox.com/s/15gisj8hx218rn1/street-pole-sample.csv?dl=1"
df = pd.read_csv(url)
df.head()

px.scatter_mapbox(df, lat="Y", lon="X", zoom=15)

df["geom"] = df["Y"].map(str) + ',' + df['X'].map(str)
df["geom"][0]

