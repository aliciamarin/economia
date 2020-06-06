# -*- coding: utf-8 -*-
# %%
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from datascience import *
import numpy as np
import plotly.graph_objects as go


# %%
def pintar_funcion_oferta(cantidad, precio, maxX = None):
    fig = go.Figure(data=go.Scatter(
    go.Scatter(
        x=cantidad, 
        y=precio, 
        line=dict(color="#00CED1", width=4), 
        marker=dict(size=15, color='#fabada'),
        name="Función de la oferta")))

    if (maxX is None):
        maxX = max(cantidad)

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, maxX]),
        yaxis_title="Precio",
        yaxis=dict(range=[0,  max(precio)]),
        title="Función de la oferta"
    )

    fig.show()


# %%
def pintar_funcion_oferta_precio_variable(cantidad, precio, desdePrecio, aPrecio, funcion):
    values = aPrecio
    
    active = int(round(values / 2))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=cantidad, y=precio, mode='lines', line=dict(color="#00CED1", width=4), name="Función de la oferta"))

    for step in np.arange(1, values, 1):
        fig.add_trace(go.Scatter(visible=False, x=[funcion(step)], y=[step], marker=dict(size=20, color='#fabada'), name="Precio"))

    fig.data[active].visible = True

    steps = []
    for i in range(values):
        step = dict(
            method="update",
            args=[{"visible": [False] * values}, {"title": "Precio: " + str(i)}],
        )
        step["args"][0]["visible"][0] = True # funcion de la oferta
        step["args"][0]["visible"][i] = True # precio actual
        steps.append(step)

    sliders = [dict(
        active=active,
        currentvalue={"prefix": "Precio: "},
        steps=steps
    )]

    fig.update_layout(
        xaxis_title="Cantidad", 
        yaxis_title="Precio",
        xaxis=dict(range=[0, max(cantidad)]),
        yaxis=dict(range=[0, max(precio)]),
        title="Precio:" + str(active),
        sliders=sliders
    )

    fig.show()


# %%
def pintar_funcion_oferta_otros_factores(cantidad, precio, min_value, max_value, funcion):
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

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(cantidad)]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(precio)]),
        title="Variación:" + str(active),
        sliders=sliders
    )

    fig.show()


# %%
def pintar_funcion_oferta_multiple(valores):
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
        xaxis=dict(range=[0, 100]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, 5]),
        title="Función de la oferta"
    )

    fig.show()
