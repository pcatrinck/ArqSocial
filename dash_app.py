import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Create fake data
np.random.seed(0)
neighborhoods = ['Bonfim', 'Consolação', 'C. Carapina', 'Engenharia', 'Irararé', 'S. Benedito', 'Da Penha']
data = {
    'Neighborhood': np.tile(neighborhoods, 3),
    'Measurement': ['C. by Woman'] * 7 + ['Avg age'] * 7 + ['Humidity'] * 7,
    'Value': np.random.rand(21) * 100
}
df = pd.DataFrame(data)

def create_dash_app(flask_app):
    dash_app = dash.Dash(server=flask_app, name="DashApp", url_base_pathname="/dashs/")
    dash_app.layout = html.Div([
        dcc.Checklist(
            id='measurement-checklist',
            options=[
                {'label': 'C. by Woman', 'value': 'C. by Woman'},
                {'label': 'Avg age', 'value': 'Avg age'},
                {'label': 'Humidity', 'value': 'Humidity'}
            ],
            value=['C. by Woman']
        ),
        dcc.Graph(id='example-graph')
    ])

    @dash_app.callback(
        Output('example-graph', 'figure'),
        [Input('measurement-checklist', 'value')]
    )
    def update_graph(selected_measurements):
        filtered_df = df[df['Measurement'].isin(selected_measurements)]
        fig = px.line(filtered_df, x='Neighborhood', y='Value', color='Measurement', markers=True)
        return fig

    return dash_app
