import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("data/processed/anomalies.csv", parse_dates=["timestamp", "block_time"])

app = Dash(__name__)

# Plot transactions colored by anomaly
fig = px.scatter(
    df,
    x="timestamp",
    y="amount",
    color="anomaly_flag",
    color_discrete_map={True: "red", False: "blue"},
    title="Transactions with Anomaly Flags"
)

app.layout = html.Div([
    html.H1("BlockBridge Anomaly Detection"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
