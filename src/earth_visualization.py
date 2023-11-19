import pandas as pd
import plotly.graph_objs as go

def load_data(filename):
    """Load data from a CSV file."""
    return pd.read_csv(filename)

def plot_3d_earth(data):
    """Create a 3D plot of the Earth with data points."""
    trace = go.Scattergeo(
        lon = data['longitude'],
        lat = data['latitude'],
        mode = 'markers',
        marker = dict(size = data['magnitude']*10)
    )

    layout = go.Layout(
        title = '3D Earth Visualization',
        geo = dict(showland = True, projection = dict(type = 'orthographic'))
    )

    fig = go.Figure(data = [trace], layout = layout)
    fig.show()

if __name__ == "__main__":
    data = load_data('data/data.csv') 
    plot_3d_earth(data)