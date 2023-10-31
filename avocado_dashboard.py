#Import Libraries
from dash import Dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
import pandas as pd
import plotly.express as px


#Load the Dataset

avocado = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Avocado.csv')

# Create the Dash App

app = Dash(__name__)

#setting up the app layout

app.layout = html.Div(children=[
    html.H1('Avocado Prices Dashboard'),
    dcc.Dropdown(id='reg-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in avocado['region'].unique()],
                 value='NewYork'),

    dcc.Graph(id='price-graph')
])

#Set up the callback fuction
@app.callback(
Output(component_id='price-graph', component_property='figure'),
    Input(component_id='reg-dropdown', component_property='value')


)
def update_graph(selected_region):
    filtered_avocado = avocado[avocado['region'] == selected_region]
    line_fig = px.line(filtered_avocado,
                       x='Date', y='AveragePrice',
                        color='type',
                        title=f'Avocado prices in {selected_region}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)
