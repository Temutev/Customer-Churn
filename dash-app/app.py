# Data Libraries
import pandas as pd
import numpy as np

# App libraries
import dash_core_components as dcc
import dash_html_components as html

import dash.dependencies
import dash_auth
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
# import requests

# Visualization Libraries
#import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px


# THE COMPONENTS
## GRAPHS - LAYOUTS - BUTTONS
from graphsutils import plot_dist_churn, pie_norm, pie_churn, plot_dist_churn2
from layouts import graph_1, graph2_3, create_footer, header_logo, paragraphs
from buttons import button_line

# CSS EXTERNAL FILE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']


# Importing the dataset
data = pd.read_csv('data/Customer-Value-Analysis.csv')

# Some initial modification in the data
data['Customer Lifetime Value'] = data['Customer Lifetime Value'].apply(np.ceil)
data['Total Claim Amount'] = data['Total Claim Amount'].apply(np.ceil)
data['Churn_label'] = data.Response.copy()
data['Response'] = data.Response.replace({'Yes': 1, 'No': 0})

# App Name
app_name = 'Customer Value Analysis Dashboard'

# Instantiating our app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                meta_tags=[    
                    {
                        "name": "viewport",
                        "content": "width=device-width, initial-scale=1, maximum-scale=1",
                    }])


# Seting the name to app
app.title = app_name

server = app.server

# All functions inside a Div with a specific size
# It's all functions that I implemented on other python files


def navbar(logo="/assets/logo-placeholder.png", height="35px",  appname="PlaceHolder Name"):

    navbar = html.Div(
        [dbc.Container(
            [dbc.Row([
                dbc.Col(html.A(
                    # Use row and col to control vertical alignment of logo / brand


                        html.Div(
                            "Vince Temu.", className="trich-navbar white font-xl", ),

                        href="https://github.com/Temutev",
                        ), width=4),
                dbc.Col(dbc.NavbarBrand(
                    appname, className="font-md text-white"), className="text-right", width=8)],
                style={"align-items": "center", "min-height": "75px"}
            )
            ],
            style={"maxWidth": "1140px"})
         ],  
        className="bottom32 navbarColor",
        # style={'height': '100px', "borderBottom":".5px solid lightgrey", "padding":"18px 0px"}

        # dark=True,
    )

    return navbar


def tab_test1():
    tab1 = dbc.Container([
        dbc.Row(header_logo(), className="textBackground padding40 bottom32 top32 margin-auto",  
                ), 
        html.Div(button_line(),
                 ),
        dbc.Row(graph_1()),  
        dbc.Row(paragraphs(),
                className="textBackground padding40 bottom32 top32 margin-auto"),
        html.Div(graph2_3())  # Pie graphs
    ],  # style={"maxWidth": "960px"}
    )      
    return tab1


# main APP engine
app.layout = html.Div(children=[
    navbar(appname=app_name),  # Header of the app
    tab_test1(),  # Body of the APP
    html.Div(create_footer())],
    style={'overflow': 'hidden'}
)  # create_footer()


###################################################
## first line of graphsGraph 1 of the first line ##
###################################################
@app.callback(
    dash.dependencies.Output('Graph1', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('churn-or-not', 'value')])
def binary_ploting_distributions(cat_col, binary_selected):
    from plotly import tools
    # print(binary_selected)
    if binary_selected == 'Churn':
        return plot_dist_churn(data, cat_col)
    else:
        return plot_dist_churn2(data, cat_col)

#


@app.callback(
    dash.dependencies.Output('Graph3', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    # count_trace = df_train[df_cat].value_counts()[:limit].to_frame().reset_index()
    return pie_churn(data, val1, val2, "No-Response")

#


@app.callback(
    dash.dependencies.Output('Graph5', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def PieChart(val1, val2, limit=15):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    return pie_churn(data, val1, val2, "Response")

#


@app.callback(
    dash.dependencies.Output('Graph2', 'figure'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('dropdown2', 'value')])
def _graph_upgrade2(val1, val2):
    """
    This function helps to investigate the proportion of metrics of toxicity and other values
    """
    return pie_norm(data, val1, val2)




@app.callback(
    dash.dependencies.Output('Graph4', 'figure'),
    [dash.dependencies.Input('dropdown2', 'value'),
     dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('churn-or-not', 'value')])
def _plotly_express(cat_col, color, churn):
    # tmp = df_train.groupby(color)[cat_col].sum().reset_index()
    # tmp = tmp.sort_values(color)
    if churn == "Churn":
        fig = px.box(data, x=color, y=cat_col,  # category_orders={color:df_train[color].value_counts},
                     # legend=False,
                     color=data['Churn_label'].map({'Yes': 'Churn', 'No': 'NoChurn'}), height=450,
                     color_discrete_map={"Churn": "seagreen",
                                         "NoChurn": "indianred"},
                     category_orders={
                         str(color): data[color].value_counts().sort_index().index}
                     # opacity=.6,# height=400
                     )
        fig.update_layout(
            title=f"{cat_col} dist by <br>{color} & Churn",
            xaxis_title=dict(), showlegend=True,
            yaxis_title=f"{cat_col} Distribution",
            title_x=.5, legend_title=f'Churn:',
            xaxis={'type': 'category'},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50)
        )
    else:
        fig = px.box(data, x=color, y=cat_col,
                     height=450,  # legend=False,
                     category_orders={
                         str(color): data[color].value_counts().sort_index().index},
                     color_discrete_sequence=['seagreen']
                     # opacity=.6,# height=400
                     )

        fig.update_layout(
            title=f"Distribution of {cat_col} <br>by {color}",
            xaxis_title=dict(), showlegend=False,
            yaxis_title=f"{cat_col} Distribution",

            # width=560000,
            title_x=.5, legend_title=f'Churn:',
            xaxis={'type': 'category'},
            # legend_orientation='h',
            # legend=dict(y=-.06),
            margin=dict(t=100, l=50)
        )

    fig.update_xaxes(title='')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=4445)



