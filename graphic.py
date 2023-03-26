import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

#Chargement des données et mise en forme CSV
df = pd.read_csv('projetGitLinuxPython/prices.txt', sep = ',', names = ['prix', 'temps'])
df['prix'] = df['prix'].str.replace('$', '',regex=False)
df['prix'] = df['prix'].str.replace(' ', '',regex=False).astype('float')

with open("metrics.txt", "r") as f:
    metrics_text = f.read()

#Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Evolution du Wrapped Bitcoin'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['temps'], 'y': df['prix'], 'type': 'line', 'name': 'Donnees'},
            ],
            'layout': {
                'title': 'Evolution du prix'
            }
        }
     ),
        html.H1('Metrics'),
        html.Pre(metrics_text)

])


#Main
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True)


