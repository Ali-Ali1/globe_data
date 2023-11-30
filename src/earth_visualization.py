# import pandas as pd
# import plotly.graph_objs as go

# def load_data(filename):
#     """Load data from a CSV file."""
#     return pd.read_csv(filename)

# def create_hover_text(row):
#     """Create a text string for hovering."""
#     return f"<b>{row['name']}:</b><br>Number of incidents: {row['incidents']}</br>"

# def plot_3d_earth(us_states_data):
#     """Create a map focused on the USA with data points."""

#     # Add more details to hover text
#     us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

#     # US States Trace
#     us_states_trace = go.Scattergeo(
#         lon = us_states_data['longitude'],
#         lat = us_states_data['latitude'],
#         hoverinfo = 'text',
#         text = us_states_data['hover_text'],
#         mode = 'markers',
#         marker = dict(size = 1, color = 'black'),
#         name = 'US States'
#     )

#     layout = go.Layout(
#         title = 'Map Focused on the USA Extremeist Incidents [~ 1970-2020]',
#         geo = dict(
#             scope = 'usa',
#             showland = True,
#             landcolor = 'green',
#             showocean = True,
#             oceancolor = 'lightblue',
#             showcountries = True,
#             countrycolor = 'black',
#             showsubunits = True,
#             subunitcolor = 'black'
#         ),
#         showlegend = False
#     )

#     fig = go.Figure(data = [us_states_trace], layout = layout)
#     fig.show()

# if __name__ == "__main__":
#     us_states_data = load_data('data/us_states_data_2.csv') # CSV with additional data for each state
#     plot_3d_earth(us_states_data)


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px  # For the color scale

def load_data(filename):
    """Load data from a CSV file."""
    return pd.read_csv(filename)

def create_hover_text(row):
    """Create a text string for hovering."""
    return f"<b>{row['state']}:</b><br><b>Number of incidents: </b>{row['incidents']}</br><br><b>Most Common Extremist Group:</b> {row['PERPETRATOR GROUP']} </br><br><b>Most Common Weapons Type:</b> {row['WEAPON TYPE']} </br> </br><br><b>Most Common Target:</b> {row['Target Type']} </br> </br><br><b>Most Common Weapons Attack Type:</b> {row['Attack Type']} </br>"

def plot_3d_earth(us_states_data, gtd):
    """Create a map focused on the USA with data points."""

    # Add more details to hover text
    us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

    # Define a color scale
    color_scale = px.colors.sequential.Blues  # You can choose any appropriate color scale

    # US States Trace with color based on 'incidents'
    us_states_trace = go.Scattergeo(
        lon = us_states_data['longitude'],
        lat = us_states_data['latitude'],
        hoverinfo = 'text',
        text = us_states_data['hover_text'],
        mode = 'markers',
        marker = dict(
            size = 20,  # Adjust size for visibility
            color = us_states_data['incidents'],  # Color depends on the number of incidents
            colorscale = color_scale,
            colorbar_title = 'Number of Incidents',
            showscale = True  # Show the color scale legend
        ),
        name = 'US States'
    )


    layout = go.Layout(
        title = 'Map Focused on the USA Extremeist Incidents [~ 1970-2020]',
        geo = dict(
            scope = 'usa',
            showland = True,
            landcolor = 'lightseagreen',
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
    us_states_data = load_data('data/GTD_display.csv') # CSV with additional data for each state
    gtd = load_data('data/GTD.csv')
    plot_3d_earth(us_states_data, gtd)



