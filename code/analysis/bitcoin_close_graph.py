    ## Importing necessary libraries
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

import descartes
import geopandas as gpd
from shapely.geometry import Point

# Reading the dataframe from csv file
df = pd.read_csv("../../datasets/final/df_combined.csv", index_col = False)

bitcoin_close = df["close"]
time = df["date"]

#fig, ax = plt.subplots()
##plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
##plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
#ax.scatter(time, bitcoin_close)
#ax.set_title("Bitcoin close price from 2017-08-01 to 2019-21-01")
#ax.set_xlabel("Time")
#ax.set_ylabel("Bitcoin close prices (" + u"\u20BF" + ")")
##plt.gcf().autofmt_xdate()
#plt.show()

# TODO: Change legend title to "Total Volume of Tweets"
fig = px.scatter(df, x = "date", y = "close", color = "total_volume_of_tweets", size = "financial_crimes")
#fig.add_trace(go.Scatter(x = df["date"], y = df["close"], opacity = 0.3))
fig.update_layout(title = "Daily Bitcoin Close Price Between 2017-08-01 and 2019-01-21",
        xaxis_title = "Date",
        yaxis_title = "Bitcoin Closing Price ({})".format(u"\u0243"))
pio.write_html(fig, "../../diagrams/time_vs_bitcoin_close_price.html")
#fig.write_image("../../diagrams/time_vs_bitcoin_close_price.png")
#fig.show()

fig = px.scatter_3d(df, x = "date", y = "close", z = "total_volume_of_tweets", color = "total_crimes") 
#fig.show()
pio.write_html(fig, "../../diagrams/time_vs_bitcoin_close_price_vs_volume_tweets.html")

fig = px.scatter_3d(df, x = "bitcoin_close_change", y = "gold_change", z = "total_crimes", color = "total_volume_of_tweets") 
#fig.show()
pio.write_html(fig, "../../diagrams/bitcoin_close_price_change_vs_gold_price_change_vs_total_crime.html")

#fig = px.scatter(df, x = "date", y = "financial_crimes", size = "count_negatives", color = "gold_value")
#fig.show()

#fig = px.scatter(df, x = "total_crimes", y = "close")
#fig.show()

#pd.plotting.scatter_matrix(df)
#plt.show()

#plt.matshow(df.corr())
#plt.colorbar()
#plt.show()
scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
        [0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
        [0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]
        
fig = go.Figure(data = go.Scattergeo(
    lat = df["avg_latitude"],
    lon = df["avg_longitude"],
    marker = dict(
        color = df["total_crimes"],
        colorscale = scl,
        reversescale = True,
        opacity = 0.7,
        size = 2,
        colorbar = dict(
            titleside = "right",
            outlinecolor = "rgba(68, 68, 68, 0)",
            ticks = "outside",
            showticksuffix = "last",
            dtick = 0.1
        )
    )
))

fig.update_layout(
        geo = dict(
            scope = "north america",
            showland = True,
            landcolor = "rgb(212, 212, 212)",
            subunitcolor = "rgb(255, 255, 255)",
            countrycolor = "rgb(255, 255, 255)",
            showlakes = True,
            lakecolor = "rgb(255, 255, 255)",
            showsubunits = True,
            showcountries = True,
            resolution = 50,
            projection = dict(
                type = 'conic conformal',
                rotation_lon = -100
            ),
            lonaxis = dict(
                showgrid = True,
                gridwidth = 0.5,
                range= [ -140.0, -55.0 ],
                dtick = 5
            ),
            lataxis = dict (
                showgrid = True,
                gridwidth = 0.5,
                range= [ 20.0, 60.0 ],
                dtick = 5
            )
        ),
    title = "Crime in Chicago",
)

pio.write_html(fig, "../../diagrams/chicago_crime_map.html")



chicago_map = gpd.read_file("../../datasets/original/chicago_map.shp")

geometry = [Point(xy) for xy in zip( df["avg_longitude"], df["avg_latitude"] )]
geo_df = gpd.GeoDataFrame(df,
        crs = {"init", "SR-ORG:7634"},
        geometry = geometry)
fig, ax = plt.subplots()
chicago_map.plot(ax = ax, alpha = 0.4, color = "grey")
geo_df.plot(ax = ax, c = df["total_crimes"])
plt.savefig("../../diagrams/chicago_crime_map.png")


# Reading the dataframe from csv file
#df_crimes = pd.read_csv("../../datasets/original/chicago_crimes.csv", index_col = False)
#df_crimes = df_crimes.astype({"Longitude": float,
#    "Latitude": float})
#geometry = [Point(xy) for xy in zip( df_crimes["Longitude"], df_crimes["Latitude"] )]
#geo_df_crimes = gpd.GeoDataFrame(df_crimes,
#        crs = {"init", "SR-ORG:7634"},
#        geometry = geometry)
#fig, ax = plt.subplots()
#chicago_map.plot(ax = ax, alpha = 0.4)
#geo_df_crimes.plot(ax = ax)
#plt.savefig("../../diagrams/chicago_crime_map_orig.png")








