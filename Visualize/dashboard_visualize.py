import pandas as pd
import plotly.express as px
from dash import Dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

# Add data source
df = pd.read_csv('crawl_data_thpt2023/Visualize/thpt_clean.csv', encoding='utf16')
df = df.drop(columns=['ID'])

# Create the Dash app
app = Dash(__name__)

app.title = "THPT 2023"
# Define the dropdown layout
app.layout = html.Div([
    html.H1(children = "Data THPT 2023"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=7),

    dcc.Dropdown(
        id='dropdown_subject',
        options=[{'label': col, 'value': col} for col in df.columns],
        value= df.columns[0],
        
    ),
    dcc.Graph('score-graph')]
)
# Define the callback function to update the graph based on the dropdown selection

@app.callback(
    Output('score-graph', 'figure'),
    [Input('dropdown_subject', 'value')],
)

def update_graph(column):
    fig = px.histogram(df, x=column)
    return fig 

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port = 6969)