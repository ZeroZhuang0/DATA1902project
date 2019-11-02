    ## Importing necessary libraries

import pandas as pd
from scipy.stats import pearsonr

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

#import descartes
#import geopandas as gpd
#from shapely.geometry import Point

#import seaborn as sns

from dateutil import parser


# Reading the dataframe from csv file
df = pd.read_csv("../../datasets/final/df_combined.csv", index_col = False)


'''
Bitcoin Close Price VS Date
Coloured by Volume of Bitcoin Tweets
Size by Number of Financial Crimes
'''

# Two plots for the size legend and the main scatter plot
fig = make_subplots(rows = 8, cols = 7,
        specs = [
            [None, {"colspan": 6, "rowspan": 8}, None, None, None, None, None],
            [{"colspan": 1, "rowspan": 7}, None, None, None, None, None, None],
            [None] * 7,
            [None] * 7,
            [None] * 7,
            [None] * 7,
            [None] * 7,
            [None] * 7
        ]
        )

sizeref = 2.0 * max(df.financial_crimes) / (25.0 ** 2) # Setting the reference size for each point

# Creating the trace for Bitcoin closing price over time
price_date = go.Scatter(x = df.date, y = df.close,
        hovertext = ["Date: {}<br>Price: {}{:.1f}<br>Financial Crimes: {}<br>Tweets: {}"
                    .format(parser.parse(line["date"]).strftime("%-d %b, %Y"), 
                        u"\u0243",
                        line["close"],
                        line["financial_crimes"],
                        line["total_volume_of_tweets"])\
                    
                    for index, line in df.iterrows()],
        hoverinfo = "text",
        mode = "lines+markers", 
        showlegend = False,
        marker = dict(
            colorbar = dict(
                title = dict(
                    text = "Number of Tweets<br>Mentioning Bitcoin"
                    )
                ),
            color = df.total_volume_of_tweets,
            colorscale = "Viridis",
            size = df.financial_crimes,
            sizemode = "area",
            sizeref = sizeref,
            line_width = 0.3,
            opacity = 0.6
            ),
        line = dict(
            color = "rgb(220,220,220)",
            width = 3,
            shape = "spline",
            smoothing = 1.3
            )
        )

fig.update_xaxes(title_text = "Date", row = 1, col = 2)
fig.update_yaxes(title_text = "Bitcoin Closing Price ({})".format(u"\u0243"),
        row = 1, col = 2)
fig.add_trace(price_date, row = 1, col = 2)

min_fin_crimes = 10
max_fin_crimes = round(max(df.financial_crimes), -1)
legend_size = list(range(min_fin_crimes, max_fin_crimes + 1, 10))

legend = go.Scatter(x = [1] * len(legend_size), y = legend_size, 
        hoverinfo = "none",
        mode = "markers",
        showlegend = False,
        marker = dict(
            color = "rgb(220,220,220)",
            sizemode = "area",
            sizeref = sizeref,
            size = legend_size
            )
        )

fig.update_xaxes(showgrid = False,
        showline = False,
        showticklabels = False,
        title = dict(
            text = "Number of Financial<br>Crimes in Chicago",
            font = dict(size = 12)
            ),
        side = "top",
        fixedrange = True,
        row = 2, col = 1)
fig.update_yaxes(showline = False,
        side = "left",
        fixedrange = True,
        tickvals = legend_size,
        row = 2, col = 1)
fig.add_trace(legend, row = 2, col = 1)

layout = go.Layout(
        title = dict(
            text = "Daily Bitcoin Close Price",
            x = 0.5
            ),
        shapes = [
	    go.layout.Shape( # White-filled rectangle for aesthetic purposes
		type="rect",
                xref = "paper",
                yref = "paper",
                x0 = 0,
		y0 = 0,
                x1 = 0.13,
		y1 = 1,
		line = dict(
		    width = 0,
		),
		fillcolor = "white",
                layer = "below"
	    )
	])

fig.update_layout(layout)

pio.write_html(fig, "../../diagrams/bitcoin_close_price_vs_time.html")


'''
Date VS Bitcoin Close Price VS Volume of Bitcoin Tweets
Coloured by Total Number of Crimes 
'''

fig = go.Scatter3d(x = df["date"], y = df["close"], z = df["total_volume_of_tweets"],
        hovertext = ["Date: {}<br>Price: {}{:.1f}<br>Tweets: {}<br>Crimes: {}"
                    .format(parser.parse(line["date"]).strftime("%-d %b, %Y"), 
                        u"\u0243",
                        line["close"],
                        line["total_volume_of_tweets"],
                        line["total_crimes"])\
                    
                    for index, line in df.iterrows()],
        hoverinfo = "text",
        mode = "markers",
        marker = dict(
            color = df["total_crimes"],
            colorbar = dict(
                title = dict(
                    text = "Number of Crimes<br>in Chicago"
                    )
                ),
            opacity = 0.8
            )
        )

layout = go.Layout(
        title = dict(
            text = "Daily Bitcoin Close Price VS the Number of Tweets Mentioning Bitcoin",
            x = 0.5
            ),
        scene = dict(
            xaxis = dict(title = "Date"),
            yaxis = dict(
                title = "Bitcoin Closing Price ({})".format(u"\u0243"),
                range = [0, 20000]
                ),
            zaxis = dict(
                title = "Number of Tweets Mentioning Bitcoin",
                range = [0, 140000]
                )
            )
        )

fig = go.Figure(data = [fig], layout = layout)

pio.write_html(fig, "../../diagrams/time_vs_bitcoin_close_price_vs_volume_tweets.html")

print("Pearson's Correlation between Bitcoin close price and Volume of tweets: {:.3f}"\
        .format(pearsonr(df["close"], df["total_volume_of_tweets"])[0]))


'''
Daily Bitcoin Percentage Change VS Number of Domestic Crimes
Coloured by Total Number of Positive Tweets
'''

fig = go.Scatter(x = df["bitcoin_close_change"], y = df["num_domestic"],
        hovertext = ["Change in Price: {:.1f}%<br>Domestic Crimes: {}<br>Positive Tweets: {}"
                .format(line["bitcoin_close_change"],
                        line["num_domestic"],
                        line["count_positives"])\
                    
                    for index, line in df.iterrows()],
        hoverinfo = "text",
        mode = "markers",
        marker = dict(
            color = df["count_positives"],
            colorscale = "algae",
            colorbar = dict(
                title = dict(
                    text = "Number of Positive Tweets<br>Mentioning Bitcoin"
                    )
                ),
            size = 10,
            opacity = 0.8
            )
        )

layout = go.Layout(
        title = dict(
            text = "Daily Percentage Change in Bitcoin VS the Number of Domestic Crimes Committed in Chicago",
            x = 0.4
            ),
        xaxis = dict(title = "Percentage Change in Bitcoin Closing Price (%)"),
        yaxis = dict(
            title = "Number of Domestic Crimes in Chicago",
            range = [0, max(df["num_domestic"]) + 20]
            ),
        )

fig = go.Figure(data = [fig], layout = layout)

pio.write_html(fig, "../../diagrams/bitcoin_close_change_vs_crimes.html")
