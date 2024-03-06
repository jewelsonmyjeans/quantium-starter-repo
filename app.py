from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("data-clean.csv")

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div([
    html.Div([
        html.H1(children='Sales of Pink Morsels', style={'text-align': 'center'}),
        dcc.Graph(
            id='Pink Morsel Sales',
            figure=fig
        )
    ], style={'background-color': 'white', 'padding': '20px', 'border-radius': '10px', 'box-shadow': '0 4px 8px rgba(0,0,0,0.1)'}),
    html.Div([
        dcc.RadioItems(
            id='region-select',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            labelStyle={'margin-right': '10px'}
        )
    ], style={'width': '60%', 'margin': '20px auto'}),
], style={'background-color': 'pink', 'width': '100%', 'height': '100%', 'padding': '20px'})

@app.callback(
    Output('Pink Morsel Sales', 'figure'),
    Input('region-select', 'value'))
def update_graph(region_select):
    if region_select == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region_select]

    updated_fig = px.line(filtered_df, x="date", y="sales", color="region")

    updated_fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
        hovermode='closest',
        xaxis_title='Date',
        yaxis_title='Sales'
    )

    return updated_fig

if __name__ == '__main__':
    app.run_server(debug=True)

