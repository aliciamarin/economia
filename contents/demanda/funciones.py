# -*- coding: utf-8 -*-
# %%
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from datascience import *
import numpy as np
import plotly.graph_objects as go


# %%
def pintar_funcion_demanda(cantidad, precio):
    fig = go.Figure(data=go.Scatter(
    go.Scatter(
        x=cantidad,
        y=precio,
        line=dict(color="#00CED1", width=4), 
        marker=dict(size=15, color='#fabada'),
        name="Función de la demanda")))

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(cantidad)]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(precio)]),
        title="Función de la demanda"
    )

    fig.show()


# %%
def pintar_funcion_demanda_multiple(valores):
    fig = go.Figure()
    
    for valor in valores:
        traza = go.Scatter(
            x=valor[0], 
            y=valor[1], 
            line=dict( width=4), 
            marker=dict(size=10),
            name=valor[2])

        fig.add_trace(traza)
    
    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, 20]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, 1.5]),
        title="Función de la demanda"
    )

    fig.show()


# %%
def pintar_funcion_demanda_otros_factores(cantidad, precio, min_value, max_value, funcion, maxX = None, maxY = None):
    active = int(round((min_value + max_value)/2))

    values = range(min_value, max_value + 1)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=cantidad, y=precio, mode='lines', line=dict(color="#00CED1", width=4), name="Función original"))

    for step in values:
        preciosVariacion = [funcion(P, step) for P in precio]
        fig.add_trace(go.Scatter(visible=False, x=preciosVariacion, y=precio,mode='lines', line=dict(color="#fabada", width=4), name="Función con variación"))
    
    steps = []
    for i in range(len(values)):
        step = dict(
            method="update",
            args=[{"visible": [False] * (len(values)+ 2)}, {"title": "Variación: " + str(i + min_value)}],
        )
        step["args"][0]["visible"][0] = True # funcion de la oferta
        step["args"][0]["visible"][i + 1] = True # precio actual
        steps.append(step)
        
    sliders = [dict(
        active=(len(values) - 1)/2,
        currentvalue={"prefix": "Variación: "},
        steps=steps
    )]
    
    if (maxX is None):
        maxX = max(cantidad)
        
    if (maxY is None):
        maxY = max(precio)

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, maxX]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, maxY]),
        title="Variación:" + str(active),
        sliders=sliders
    )

    fig.show()
