import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
from client import OPCClient
from Initialization_Parametrs import Parametrs
import datetime

t = datetime.datetime.now()

X = deque(maxlen=30)
X.append(1)
Y = deque(maxlen=30)
Y.append(1)

opcc = OPCClient()
opcc.run()

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1 * 1000
        ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(input_data):
    X.append(datetime.datetime.now())
    Y.append(opcc.get_value(Parametrs)[0])
    print(Y)
    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    left_bound = datetime.datetime.now() - datetime.timedelta(seconds=30)
    if datetime.datetime.now() - t <= datetime.timedelta(seconds=30):
        left_bound = t
    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[left_bound, datetime.datetime.now()]),
                                                yaxis=dict(range=[Parametrs[3].restriction[0],
                                                                  Parametrs[3].restriction[1]]), )}


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=9090, debug=True)



