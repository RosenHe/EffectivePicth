import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('unemployment.csv')

app = dash.Dash()

# Bar chart
data = [go.Bar(x=df['Month'], y=df['Total'])]
layout = go.Layout(title='Top 20 unemployment ratio', xaxis_title="Country",
                  yaxis_title="Number of Medals")
data_barchart = [go.Bar(x=df['Month'], y=df['Total'])]


# layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Unemployment though March2020 - March 2000', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),

    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of unemployment ratio month of the US.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Unemployment ratio in The US',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Number of Unemployment ratio'})
              }
              )])



def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()
