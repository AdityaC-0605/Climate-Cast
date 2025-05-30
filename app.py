from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.utils
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read and process data
    df = pd.read_csv("dataset.csv", index_col=0)
    df["avg_temp"] = (df["JAN"] + df["FEB"] + df["MAR"] + df["APR"] + 
                      df["MAY"] + df["JUN"] + df["JUL"] + df["AUG"] + 
                      df["SEP"] + df["OCT"] + df["NOV"] + df["DEC"]) / 12
    
    # Create temperature trend plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['YEAR'], y=df['avg_temp'], mode='lines+markers', name='Average Temperature'))
    fig.update_layout(title='Temperature Trend Over Years',
                      xaxis_title='Year',
                      yaxis_title='Average Temperature (°C)')
    
    # Convert plot to JSON for rendering
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Get summary statistics
    latest_year = df['YEAR'].max()
    latest_temp = df[df['YEAR'] == latest_year]['avg_temp'].values[0]
    max_temp = df['avg_temp'].max()
    min_temp = df['avg_temp'].min()
    
    return render_template('index.html', 
                           plot_json=plot_json,
                           latest_year=latest_year,
                           latest_temp=round(latest_temp, 2),
                           max_temp=round(max_temp, 2),
                           min_temp=round(min_temp, 2))

if __name__ == '__main__':
    app.run(debug=True)
