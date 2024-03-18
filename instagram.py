import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash
# Registrando a página
dash.register_page(__name__, path="/instagram", name="Instagram", svg="icons/instagram.svg")

# Função de callback para armazenar o DataFrame
@callback(
    Output('store_data1', 'data'),
    Input('data-store1', 'id')
)
def store_data1(id1):
    # Criando um DataFrame do zero
    df1 = pd.DataFrame({
        'Mês': ['Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro', 'Março', 'Abril'],
        'Seguidores': [10, 15, 7, 10, 10, 15, 7, 10, 10, 15]
    })
    return df1.to_dict('records')

@callback(
    Output('store_data2', 'data'),
    Input('data-store2', 'id')
)
def store_data2(id2):
    df2 = pd.DataFrame({
        'Mês': ['Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro'],
        'Engajamento': [18, 20, 48, 28, 35, 41]
     })
    return df2.to_dict('records')

@callback(
    Output('store_data3', 'data'),
    Input('data-store3', 'id')
)
def store_data3(id3):
    df3 = pd.DataFrame({
        'Mês': ['Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro'],
        'Alcance': [18, 20, 48, 28, 35, 41]
     })
    return df3.to_dict('records')
# Função de callback para atualizar o gráfico
@callback(
    Output('exemplo-grafico1', 'figure'),
    Input('store_data1', 'data')
)
def update_graph1(data):
    df1 = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig1 = px.bar(df1, x='Mês', y='Seguidores', title='Gráfico de Barras Simples')
    return fig1

@callback(
    Output('exemplo-grafico-2', 'figure'),
    Input('store_data2', 'data')
)
def update_graph_2(data):
    df2 = pd.DataFrame(data)
    fig2 = px.line(df2, x='Mês', y='Engajamento', title='Gráfico de Linhas Simples')
    return fig2

@callback(
    Output('exemplo-grafico-3', 'figure'),
    Input('store_data3', 'data')
)
def update_graph_3(data):
    df3 = pd.DataFrame(data)
    fig3 = px.bar(df3, x='Mês', y='Alcance', title='Gráfico de Barras')
    return fig3

# Layout do dashboard
layout = html.Div([
    html.H1("Instagram"),
    dcc.Graph(id='exemplo-grafico1'),
    dcc.Graph(id='exemplo-grafico-2'),
    dcc.Graph(id='exemplo-grafico-3'),
    dcc.Store(id='store_data1'),
    dcc.Store(id='store_data2'),
    dcc.Store(id='store_data3')
])