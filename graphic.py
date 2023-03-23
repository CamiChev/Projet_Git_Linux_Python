import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Charger les donnees CSV
df = pd.read_csv('prices.txt', sep = ',', names = ['prix', 'temps'])
df['prix'] = df['prix'].str.replace('$', '')
df['prix'] = df['prix'].str.replace(' ', '').astype('float')

# Creer l'application Dash
app = dash.Dash(__name__)

# Creer la mise en page de l'application
app.layout = html.Div(children=[
    html.H1(children='Evolution du prix'),

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
    )
])

# Executer l'application
if __name__ == '__main__':
    app.run_server(debug=True)



