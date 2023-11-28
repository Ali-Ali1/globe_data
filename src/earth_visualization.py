# # import pandas as pd
# # import plotly.graph_objs as go

# # def load_data(filename):
# #     """Load data from a CSV file."""
# #     return pd.read_csv(filename)

# # def create_hover_text(row):
# #     """Create a text string for hovering."""
# #     return f"<b>{row['name']}:</b><br>Number of incidents: {row['incidents']}</br>"

# # def plot_3d_earth(us_states_data):
# #     """Create a map focused on the USA with data points."""

# #     # Add more details to hover text
# #     us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

# #     # US States Trace
# #     us_states_trace = go.Scattergeo(
# #         lon = us_states_data['longitude'],
# #         lat = us_states_data['latitude'],
# #         hoverinfo = 'text',
# #         text = us_states_data['hover_text'],
# #         mode = 'markers',
# #         marker = dict(size = 1, color = 'black'),
# #         name = 'US States'
# #     )

# #     layout = go.Layout(
# #         title = 'Map Focused on the USA Extremeist Incidents [~ 1970-2020]',
# #         geo = dict(
# #             scope = 'usa',
# #             showland = True,
# #             landcolor = 'green',
# #             showocean = True,
# #             oceancolor = 'lightblue',
# #             showcountries = True,
# #             countrycolor = 'black',
# #             showsubunits = True,
# #             subunitcolor = 'black'
# #         ),
# #         showlegend = False
# #     )

# #     fig = go.Figure(data = [us_states_trace], layout = layout)
# #     fig.show()

# # if __name__ == "__main__":
# #     us_states_data = load_data('data/us_states_data_2.csv') # CSV with additional data for each state
# #     plot_3d_earth(us_states_data)


# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px  # For the color scale

# def load_data(filename):
#     """Load data from a CSV file."""
#     return pd.read_csv(filename)

# def create_hover_text(row):
#     """Create a text string for hovering."""
#     return f"<b>{row['name']}:</b><br>Number of incidents: {row['incidents']}</br><br>PERPETRATOR GROUP: </br><br>Weapons Type: </br>"

# def plot_3d_earth(us_states_data):
#     """Create a map focused on the USA with data points."""

#     # Add more details to hover text
#     us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

#     # Define a color scale
#     color_scale = px.colors.sequential.Blues  # You can choose any appropriate color scale

#     # US States Trace with color based on 'incidents'
#     us_states_trace = go.Scattergeo(
#         lon = us_states_data['longitude'],
#         lat = us_states_data['latitude'],
#         hoverinfo = 'text',
#         text = us_states_data['hover_text'],
#         mode = 'markers',
#         marker = dict(
#             size = 20,  # Adjust size for visibility
#             color = us_states_data['incidents'],  # Color depends on the number of incidents
#             colorscale = color_scale,
#             colorbar_title = 'Number of Incidents',
#             showscale = True  # Show the color scale legend
#         ),
#         name = 'US States'
#     )

#     layout = go.Layout(
#         title = 'Map Focused on the USA Extremeist Incidents [~ 1970-2020]',
#         geo = dict(
#             scope = 'usa',
#             showland = True,
#             landcolor = 'lightseagreen',
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
import json

def load_data(filename):
    """Load data from a CSV file."""
    return pd.read_csv(filename)

def create_hover_text(row):
    """Create a text string for hovering."""
    return f"<b>{row['name']}:</b><br>Number of incidents: {row['incidents']}</br><br>PERPETRATOR GROUP: </br><br>Weapons Type: </br>"

def plot_3d_earth(us_states_data, us_states_geojson):
    """Create a map focused on the USA with data points."""

    # Add more details to hover text
    us_states_data['hover_text'] = us_states_data.apply(create_hover_text, axis=1)

    # US States Choropleth
    us_states_trace = go.Choropleth(
        geojson = us_states_geojson,
        locations = us_states_data['name'],  # State code to match geoJSON features
        z = us_states_data['incidents'],  # Data values for coloring
        colorscale = 'Blues',
        colorbar_title = 'Number of Incidents',
        hoverinfo = 'text',
        text = us_states_data['hover_text'],  # Custom hover text
        marker_line_color = 'black'  # Border color for states
    )

    layout = go.Layout(
        title = 'Map Focused on the USA - Extremist Incidents [~ 1970-2020]',
        geo = dict(
            scope = 'usa',
            showland = True,
            landcolor = 'lightseagreen',
            showocean = True,
            oceancolor = 'lightblue',
            showcountries = True,
            countrycolor = 'black'
        ),
        showlegend = False
    )

    fig = go.Figure(data = [us_states_trace], layout = layout)
    fig.show()

if __name__ == "__main__":
    us_states_data = load_data('data/us_states_data_2.csv') # Ensure this has 'state_code' and 'incidents'
    with open('data/us_geojson.json') as f:  # Load the geoJSON file
        us_states_geojson = json.load(f)
    plot_3d_earth(us_states_data, us_states_geojson)
