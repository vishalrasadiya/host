from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("Hi Thiresh, this is running on web for free !!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value=5, type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    input_value = int(input_value)
    input_value = input_value*input_value
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)