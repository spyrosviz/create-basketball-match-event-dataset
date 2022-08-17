from helpers import plot_basketball_court
import math
import numpy as np
import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc,html
from dash import dash_table
from datetime import date

# Set scale of basketball court. Default is in feet so we set it equal to 1.
# For meters set it equal to 0.3048 and for yards set it equal to 1/3
scale = 0.3048

# Add a scatter plot filled everywhere with transparent data points,
# in order to use clickData event to get the coordinates from graph
fig = px.scatter()
fig.add_traces(
    px.scatter(
        x=np.repeat(np.linspace(0, 100*scale, 500), 100), y=np.tile(np.linspace(0, 50*scale, 500), 100)
    )
    .update_traces(marker_color="rgba(0,0,0,0)")
    .data
)

# Use the function created in plot_basketball_court.py file to draw basketball court
# on top of the scatter plot
plot_basketball_court(fig,scaling_factor=scale,half_court=False)

# Initiate an empty dataframe to connect it with dash-table add inputs as rows
df = pd.DataFrame(columns=['team_name','player_name','event','made_or_missed','period',
                           'pressure','x_coordinate','y_coordinate','distance_from_hoop'])

# Initiate app and set bootstrap theme
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY],prevent_initial_callbacks=True,
                suppress_callback_exceptions=True,
                meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale=1.0'}])

server = app.server

# Build app layout
app.layout = dbc.Container([

# Make a date input and a type of tournament input
dbc.Row([
    dbc.Col([
        dcc.DatePickerSingle(
            id='date',
            initial_visible_month=date(2022, 3, 18),
            date=date(2022, 3, 18)
        )
        ]),
    dbc.Col([
        dcc.Input(id='tournament',placeholder='Insert tournament type',value='',style={'padding':2})
        ]),
    dbc.Col([
        dcc.Input(id='match_id',placeholder='Insert match id',value='',style={'padding':2})
        ])

    ]),
html.Br(),

# Construct team inputs

dbc.Row([
    dbc.Col([
        dcc.Input(id='team 1',placeholder='Insert home team',value='',style={'padding':2})
        ]),
    dbc.Col([
        dcc.Input(id='team 2',placeholder='Insert away team',value='',style={'padding':2})
        ]),

    ]),
html.Br(),

# Construct player inputs
dbc.Row([
        dbc.Col([
        dcc.Input(id='team 1 player',placeholder='Insert player',value='',style={'padding':2}),
        html.Br(),
        html.Button('Insert player for team 1',id='team 1 insert player button',n_clicks=0)
        ]),

        dbc.Col([
        dcc.Input(id='team 2 player',placeholder='Insert player',value='',style={'padding':2}),
        html.Br(),
        html.Button('Insert player for team 2',id='team 2 insert player button',n_clicks=0)
        ]),
    ]),

# Remove player inputs
dbc.Row([
        dbc.Col([
        dcc.Input(id='remove team 1 player',placeholder='Remove player',value='',style={'padding':2}),
        html.Br(),
        html.Button('Remove player for team 1',id='team 1 remove player button',n_clicks=0)
        ]),

        dbc.Col([
        dcc.Input(id='remove team 2 player',placeholder='Remove player',value='',style={'padding':2}),
        html.Br(),
        html.Button('Remove player for team 2',id='team 2 remove player button',n_clicks=0)
        ]),
    ]),

html.Br(),

# Construct team Tabs
dbc.Row([
        dbc.Col([
        html.H6('Select Team'),
        dcc.Tabs(id='select team',value='team1',children=[
        dcc.Tab(id='tab team 1',label='team1',value='team1',
                style={"background": "#323130",'text-transform': 'uppercase','color': 'white',
                        'border': 'grey','font-size': '11px','font-weight': 600,'align-items': 'center',
                        'justify-content': 'center','border-radius': '4px','padding':'6px'
                    },
                selected_style={
                    "background": "grey",'text-transform': 'uppercase','color': 'white',
                    'font-size': '11px','font-weight': 600,'align-items': 'center',
                    'justify-content': 'center','border-radius': '4px','padding':'6px'
                    }
                ),
        dcc.Tab(id='tab team 2',label='team2',value='team2',
                style={"background": "#323130",'text-transform': 'uppercase','color': 'white',
                        'border': 'grey','font-size': '11px','font-weight': 600,'align-items': 'center',
                        'justify-content': 'center','border-radius': '7px','padding':'6px'
                    },
                selected_style={
                    "background": "grey",'text-transform': 'uppercase','color': 'white',
                    'font-size': '11px','font-weight': 600,'align-items': 'center',
                    'justify-content': 'center','border-radius': '7px','padding':'6px'
                    }
                )
            ],style={'zIndex': 99,"background": "#323130",'border': 'grey', 'border-radius': '7px'}
                 )
        ])
    ]),

html.Div(id='tabs-output'),

# Construct player names radioitem input
dbc.Row([dbc.Col([
        dcc.RadioItems(id='players team 1',options=[],value='')
        ]),
        dbc.Col([
        dcc.RadioItems(id='players team 2',options=[],value='')
        ]),
    ]),

dbc.Row([dbc.Col([
        html.Div(id='team 1 player output')
        ]),
        dbc.Col([
        html.Div(id='team 2 player output')
        ]),
    ]),

html.Br(),

# Construct radio items components with kind of shot, made or missed shot and period of the game
dbc.Row([dbc.Col([
        html.Header(id='events',children='Type of event',style={'color':'orange','font-size':'20px'}),
        dcc.RadioItems(id='radio-events',options=[{'label':'3point Shot','value':'3 point Shot'},
                                                {'label':'2point Shot','value':'2 point Shot'},
                                                {'label':'Free Throw','value':'Free Throw'},
                                                {'label':'Lay-up','value':'Lay-up'},
                                                {'label':'Dunk','value':'Dunk'},
                                                {'label':'Long Shot','value':'Long Shot'}],value='2 point Shot')
        ],width=3),
        dbc.Col([
        html.Header(id='mademissed',children='Made or Missed Shot',style={'color':'orange','font-size':'20px'}),
        dcc.RadioItems(id='radio-mademissed',options=[{'label':'Made','value':'Made'},
                                                {'label':'Missed','value':'Missed'}],value='Made')

        ],width=3),
        dbc.Col([
        html.Header(id='period',children='Number of Period',style={'color':'orange','font-size':'20px'}),
        dcc.RadioItems(id='radio-period',options=[{'label':'1st Period','value':'1st Period'},
                                                {'label':'2nd Period','value':'2nd Period'},
                                                {'label':'3rd Period','value':'3rd Period'},
                                                {'label':'4th Period','value':'4th Period'}],value='1st Period')

        ],width=3),
        dbc.Col([
        html.Header(id='pressure',children='Event type of pressure',style={'color':'orange','font-size':'20px'}),
        dcc.RadioItems(id='radio-pressure',options=[{'label':'Guarded','value':'Guarded'},
                                                {'label':'Unguarded','value':'Unguarded'},
                                                {'label':'Time pressure','value':'Time Pressure'},
                                                ],value='Guarded')

        ],width=3)

    ]),

# Construct the graph component
dbc.Row([
    dbc.Col([
    dcc.Graph(id="graph", figure=fig),
    html.Div(id="where"),
    html.H6('X coordinate'),
    html.Div(id='x'),
    html.H6('Y coordinate'),
    html.Div(id='y'),
    html.H6('Distance from hoop'),
    html.Div(id='distance')
        ],width=10),

# Create button to insert input data into the table and a notification
# for letting us know that have been successfully saved
    dbc.Col([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Insert to table',id='insert_to_table_button',n_clicks=0)
        ],width=2)

    ]),

dbc.Row([dbc.Col([
    html.Button('Save table to excel',id='save to excel button',n_clicks=0),
    dcc.Download(id='save to excel'),
        ],width=2)
    ]),

html.Br(),

dbc.Row([

    dbc.Col([
        html.Div(id='No of records')
    ]),

    dbc.Col([
        html.Div(id='score_output',children=['Match score: 0-0'])
    ])

]),

dbc.Row([
    dash_table.DataTable(id='table',columns=[
                                             {'name':'team_name','id':'team_name','type':'text'},
                                             {'name':'player_name','id':'player_name','type':'text'},
                                             {'name':'event','id':'event','type':'text'},
                                             {'name':'made_or_missed','id':'made_or_missed','type':'text'},
                                             {'name':'period','id':'period','type':'text'},
                                             {'name':'pressure','id':'pressure','type':'text'},
                                             {'name':'x_coordinate','id':'x_coordinate','type':'numeric'},
                                             {'name':'y_coordinate','id':'y_coordinate','type':'numeric'},
                                             {'name':'distance_from_hoop','id':'distance_from_hoop','type':'numeric'}
    ],
                         data=df.to_dict('records'),editable=True,sort_action='native',filter_action='native',sort_mode='single',row_deletable=True,
                         page_action='native',page_current=0,page_size=5,style_header={'backgroundColor':'lightblue'},
                         style_data={'backgroundColor':'lightgreen'}
                         )
    ])

],fluid=True)

# Callback with input the click in the graph and output the coordinates
# from the point on graph clicked
@app.callback(
    [Output('x', 'children'),Output('y', 'children'),Output('distance', 'children')],
    Input('graph', 'clickData'),
    State('radio-events','value')
)
def click_on_graph(clickData,event):
    if not clickData:
        raise dash.exceptions.PreventUpdate
    else:
        raw_x = round(clickData['points'][0]['x'], 2)
        raw_y = round(clickData['points'][0]['y'], 2)
        if event == 'Long Shot':
            if raw_x < 45.93 * scale:

                x = 91.86 * scale - raw_x
                y = 49.21 * scale - raw_y
                d = round(math.sqrt((x-5.2*scale)**2+(y-24.605*scale)**2),2)
                return x,y,d

            else:
                x = raw_x
                y = raw_y
                d = round(math.sqrt((x - 5.2 * scale) ** 2 + (y - 24.605 * scale) ** 2), 2)
                return x, y, d

        else:

            if raw_x > 45.93 * scale:
                x = 91.86 * scale - raw_x
                y = 49.21 * scale - raw_y
                d = round(math.sqrt((x - 5.2 * scale) ** 2 + (y - 24.605 * scale) ** 2), 2)
                return x, y, d
            else:
                x = raw_x
                y = raw_y
                d = round(math.sqrt((x - 5.2 * scale) ** 2 + (y - 24.605 * scale) ** 2), 2)
                return x, y, d

# Callback with input the teams user input values and output the tab labels
@app.callback(
    [Output('tab team 1','label'),Output('tab team 2','label')],
    [Input('team 1','value'),Input('team 2','value')]
)
def update_tabs(team1,team2):
    return team1,team2

# Callback with input the teams user input values and output the tab values
@app.callback(
    [Output('tab team 1','value'),Output('tab team 2','value')],
    [Input('team 1','value'),Input('team 2','value')]
)
def update_tabs(team1,team2):
    return team1,team2

# Callback with input the insert player for team 1 button and output the options of
# radio item containing players names
@app.callback(
    Output('players team 1', 'options'),
    Input('team 1 insert player button', 'n_clicks'),
    Input('team 1 remove player button', 'n_clicks'),
    [State('players team 1', 'options'),
    State('remove team 1 player','value'),
    State('team 1 player','value')]
)
def team1_players_radio_item(n_clicks_ins,n_clicks_rem,options,removed_player,inserted_player):
    ctx = dash.callback_context
    change_no_clicks = [p['prop_id'] for p in ctx.triggered][0] #To determine if n_clicks is changed.

    if 'team 1 insert player button' in change_no_clicks:

        options.append({'label': inserted_player, 'value': inserted_player})
        return options

    if 'team 1 remove player button' in change_no_clicks:

        options.remove({'label': removed_player, 'value': removed_player})
        return options

# Callback with input the insert player for team 2 button and output the options of
# radio item containing players names
@app.callback(
    Output('players team 2', 'options'),
    Input('team 2 insert player button', 'n_clicks'),
    Input('team 2 remove player button', 'n_clicks'),
    [State('players team 2', 'options'),
    State('remove team 2 player', 'value'),
     State('team 2 player', 'value')]
)
def team2_players_radio_item(n_clicks_ins,n_clicks_rem,options,removed_player,inserted_player):
    ctx = dash.callback_context
    change_no_clicks = [p['prop_id'] for p in ctx.triggered][0]  # To determine if n_clicks is changed.

    if 'team 2 insert player button' in change_no_clicks:

        options.append({'label': inserted_player, 'value': inserted_player})
        return options

    if 'team 2 remove player button' in change_no_clicks:

        options.remove({'label': removed_player, 'value': removed_player})
        return options

# Callback with input the value team from tabs and output the value
@app.callback(
    Output('tabs-output','children'),
    Input('select team','value')
)
def selected_player_team1(team):
    return team

# Callback with input the value of radio item for team 1 and output the value
@app.callback(
    Output('team 1 player output','children'),
    Input('players team 1','value')
)
def selected_player_team1(player):
    return player

# Callback with input the value of radio item for team 2 and output the value
@app.callback(
    Output('team 2 player output','children'),
    Input('players team 2','value')
)
def selected_player_team1(player):
    return player

# Callback with input the insert to table button and output to append input values as dash table row
@app.callback(
    Output('table','data'),
    Input('insert_to_table_button','n_clicks'),
    [State('select team','value'),
     State('team 1','value'),
     State('team 2','value'),
     State('players team 1','value'),
     State('players team 2','value'),
     State('radio-events','value'),
     State('radio-mademissed','value'),
     State('radio-period','value'),
     State('radio-pressure','value'),
     State('x','children'),
     State('y','children'),
     State('distance','children'),
     ]
)
def insert_inputs_into_table(n_clicks,team,team1,team2,player1,player2,event,mademissed,period,pressure,x,y,distance):
    ctx = dash.callback_context
    button_change_id = [p['prop_id'] for p in ctx.triggered][0]  # To determine if n_clicks is changed.

    if 'insert_to_table_button' in button_change_id:

        global df

        if team == team1:

            dictionary = {'team_name':[team],'player_name':[player1],'event':[event],'made_or_missed':[mademissed],
                          'period':[period],'pressure':[pressure],'x_coordinate':[x],
                          'y_coordinate':[y],'distance_from_hoop':[distance]}
            df_new = pd.DataFrame(dictionary)
            df = pd.concat([df,df_new])
            return df.to_dict('records')

        if team == team2:

            dictionary = {'team_name':[team],'player_name':[player2],'event':[event],'made_or_missed':[mademissed],
                          'period':[period],'pressure':[pressure],'x_coordinate':[x],
                          'y_coordinate':[y],'distance_from_hoop':[distance]}
            df_new = pd.DataFrame(dictionary)
            df = pd.concat([df,df_new])
            return df.to_dict('records')

# Callback with input the data of dash datatable and output the total number or records in table
@app.callback(
    Output('No of records','children'),
    Input('table','data')
)
def display_number_of_records(data):

    if data is not None:
        return f'Number of records inserted is {len(data)}'

# Callback with input the save to excel button and output the downloaded excel file with table data
@app.callback(
    Output('save to excel','data'),
    Input('save to excel button','n_clicks'),
    [State('team 1','value'),
     State('team 2','value'),
     State('date','date'),
     State('tournament','value'),
     State('match_id','value')]
)
def save_to_excel(n_clicks,team1,team2,date,tournament,match_id):

    ctx = dash.callback_context
    save_button_change_id = [p['prop_id'] for p in ctx.triggered][0]

    if 'save to excel button' in save_button_change_id:

        return dcc.send_data_frame(df.to_excel, f'{tournament}_{match_id}_{team1}vs{team2}_{date}.xlsx', sheet_name='court_coordinates_data')

# Callback with input the data of dash datatable and output the score output div
@app.callback(
    Output('score_output','children'),
    Input('table','data'),
    State('team 1','value'),
    State('team 2','value')
)
def display_score(data,hometeam,awayteam):

    if data is not None:
        dff = pd.DataFrame.from_records(data)
        score_points = []

        for i, z in zip(dff['event'].values, dff['made_or_missed'].values):

            # If missed then 0 points
            if z == 'Missed':
                score_points.append(0)
            # If made then 3 possible outcomes
            else:
                # If event is 3 point shot or long shot then it is 3 points
                if i == '3 point Shot' or i == 'Long Shot':
                    score_points.append(3)
                # If event is free throw then it is 1 point
                elif i == 'Free Throw':
                    score_points.append(1)
                # If event is 2 point shot, dunk or lay-up then it is 2 points
                else:
                    score_points.append(2)

        dff['scored_points'] = np.array(score_points)

        # Compute match score
        dff_home_made = dff[(dff['made_or_missed'] == 'Made') & (dff['team_name'] == hometeam)]
        home_points = np.sum(dff_home_made['scored_points'].values)
        dff_away_made = dff[(dff['made_or_missed'] == 'Made') & (dff['team_name'] == awayteam)]
        away_points = np.sum(dff_away_made['scored_points'].values)
        score = f'{home_points}-{away_points}'
        return f'Match score: {score}'

if __name__ == "__main__":

    # Run app
    app.run_server(debug=False)
