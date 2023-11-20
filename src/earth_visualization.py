import pandas as pd
import plotly.graph_objs as go

def load_data(filename):
    """Load data from a CSV file."""
    return pd.read_csv(filename)

def create_hover_text(row):
    """Create a text string for hovering."""
    return f"<b>{row['name']}:</b><br>Yellow ... testing</br>"

def plot_3d_earth(us_states_data):
    """Create a map focused on the USA with data points."""

    # Add more details to hover text
    us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

    # US States Trace
    us_states_trace = go.Scattergeo(
        lon = us_states_data['longitude'],
        lat = us_states_data['latitude'],
        hoverinfo = 'text',
        text = us_states_data['hover_text'],
        mode = 'markers',
        marker = dict(size = 1, color = 'black'),
        name = 'US States'
    )

    layout = go.Layout(
        title = 'Map Focused on the USA',
        geo = dict(
            scope = 'usa',
            showland = True,
            landcolor = 'green',
            showocean = True,
            oceancolor = 'lightblue',
            showcountries = True,
            countrycolor = 'black',
            showsubunits = True,
            subunitcolor = 'black'
        ),
        showlegend = False
    )

    fig = go.Figure(data = [us_states_trace], layout = layout)
    fig.show()

if __name__ == "__main__":
    us_states_data = load_data('data/us_states_data.csv') # CSV with additional data for each state
    plot_3d_earth(us_states_data)