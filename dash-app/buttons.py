import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

cat_features = ['State', 'Coverage', 'Education', 'Employment Status',
                'Gender', 'Location Code', 'Marital Status', 'Policy Type',
                'Policy', 'Renew Offer Type', 'Sales Channel', 'Vehicle Class',
                'Vehicle Size']


def button_line():

    dropdown1 = dbc.Col(html.Div(
        [
            html.Div("Categorical Features: ", className="bold font-sm"),
            dcc.Dropdown(
                id='dropdown',
                options=[{'label': i, 'value': i} for i in cat_features],
                value='State',
            ),
        ],
        className="displayColor padding16 radius12"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 0},
        lg={"size": 4, "offset": 0},
        className="bottom16"
    )

    dropdown2 = dbc.Col(html.Div(
        [
            html.Div("Numerical Features: ", className="bold font-xs"),
            dcc.Dropdown(
                id='dropdown2',
                options=[{'label': 'Total Claim Amount', 'value': 'Total Claim Amount'},
                         {'label': 'Customer Lifetime Value', 'value': 'Customer Lifetime Value'},
                         {'label': 'Income', 'value': 'Income'},
                         {'label': 'Monthly Premium Auto', 'value': 'Monthly Premium Auto'},
                         {'label': 'Months Since Last Claim', 'value': 'Months Since Last Claim'},
                         {'label': 'Months Since Policy Inception', 'value': 'Months Since Policy Inception'},
                         {'label': 'Number of Open Complaints', 'value': 'Number of Open Complaints'},
                         {'label': 'Number of Policies', 'value': 'Number of Policies'}
                         
                         ],
                value='Total Claim Amount',
            ),
        ],
        className="displayColor padding16 radius12"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 0},
        lg={"size": 4, "offset": 0},
        className="bottom16"
    )

    radiobutton = dbc.Col(html.Div(
        [
            html.Div("Distribution Form: ", className="bold font-sm"),
            dcc.RadioItems(
                id='churn-or-not',
                options=[{'label': 'Churn', 'value': 'Churn'},
                         {'label': 'General', 'value': 'Normal'},
                         # 'padding-right':'16px'
                         ], labelStyle={'display': 'inline-block', "margin": "auto 15px"
                                        },
                value='Churn',  style={'margin': '6px 0'}
            ),
        ],
        className="displayColor padding16 radius12"),
        width={"size": 10, "offset": 1},
        md={"size": 6, "offset": 3},
        lg={"size": 4, "offset": 0},
        className="bottom16")

    return dbc.Row([radiobutton, dropdown1, dropdown2])
