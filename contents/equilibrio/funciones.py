# -*- coding: utf-8 -*-
from datascience import *
import numpy as np
import plotly.graph_objects as go

def pintar_funcion_equilibrio(cantidadOferta, precioOferta, cantidadDemanda, precioDemanda, equilibrio):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=cantidadDemanda,
        y=precioDemanda,
        mode='lines', 
        line=dict(color="#00CED1", width=4), 
        name="Función de la demanda"))

    fig.add_trace(go.Scatter(
        x=cantidadOferta, 
        y=precioOferta,
        mode='lines', 
        line=dict(color="#fabada", width=4), 
        name="Función de la oferta"))

    fig.add_trace(go.Scatter(
        x=[equilibrio[0]], 
        y=[equilibrio[1]],
        marker=dict(size=20, color='#FF9900'), 
        name="Equilibrio de mercado"))

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(max(cantidadDemanda), max(cantidadOferta))]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(max(precioDemanda), max(precioOferta))]),
        title="Equilibrio de mercado"
    )

    fig.show()


def pintar_funcion_equilibrio_variacion_precio(cantidadOferta, precioOferta, funcionOferta, cantidadDemanda, precioDemanda, funcionDemanda, equilibrio, values= 80, active = 20):
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=cantidadDemanda,
        y=precioDemanda,
        mode='lines', 
        line=dict(color="#00CED1", width=4), 
        name="Función de la demanda"))

    fig.add_trace(go.Scatter(
        x=cantidadOferta, 
        y=precioOferta,
        mode='lines', 
        line=dict(color="#fabada", width=4), 
        name="Función de la oferta"))

    fig.add_trace(go.Scatter(
        x=[equilibrio[0]], 
        y=[equilibrio[1]],
        marker=dict(size=20, color='#FF9900'), 
        name="Equilibrio de mercado"))
    
    for step in np.arange(0, values, 1):
        fig.add_trace(go.Scatter(visible=False, x=[funcionDemanda(active + step)], y=[active + step], marker=dict(size=20, color='#C0ADDB'), name="Variación"))
    for step in np.arange(0, values, 1):
        fig.add_trace(go.Scatter(visible=False, x=[funcionOferta(active + step)], y=[active + step], marker=dict(size=20, color='#C0ADDB'), name="Variación"))
       
    steps = []
    for i in range(values):
        step = dict(
            method="update",
            args=[{"visible": [False] * ((values * 2) + 3)}, 
                  {"title": "Precio: " + str(active + i)}],
        )
        
        step["args"][0]["visible"][0] = True # funcion de la demanda
        step["args"][0]["visible"][1] = True # funcion de la oferta
        step["args"][0]["visible"][2] = True # Equilibrio
        step["args"][0]["visible"][i + 3] = True
        step["args"][0]["visible"][i + values + 3] = True 
        
        steps.append(step)

    sliders = [dict(
        active=active,
        currentvalue={"prefix": "Precio: "},
        steps=steps
    )]

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(max(cantidadDemanda), max(cantidadOferta))]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(max(precioDemanda), max(precioOferta))]),
        title="Precio:" + str(active),
        sliders=sliders
    )

    fig.show()


def pintar_funcion_equilibrio_variacion_otros_oferta(cantidadOferta, precioOferta, funcionOferta, cantidadDemanda, precioDemanda, funcionDemanda, funcionEquilibrio):
    
    min_value = -20
    max_value = 20
    
    active = int(round((min_value + max_value)/2))

    values = range(min_value, max_value + 1)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=cantidadDemanda,
        y=precioDemanda,
        mode='lines',
        line=dict(color="#00CED1", width=4), 
        name="Función de la demanda"))

    for step in values:
        variacionOferta = [funcionOferta(P, step) for P in precioOferta]
        fig.add_trace(go.Scatter(visible=False, x=variacionOferta, y=precioOferta,mode='lines', line=dict(color="#fabada", width=4), name="Función de la oferta"))
    
    for step in values:
        y = funcionEquilibrio(0, step)
        x = funcionOferta(y,step)
        fig.add_trace(go.Scatter(visible=False, x=[x], y=[y], marker=dict(size=20, color='#FF9900'), name="Equilibrio de mercado"))
 
    fig.data[round((len(values))/2) + 1].visible = True
    fig.data[round((len(values) + (len(values))/2) + 1)].visible = True
    
    steps = []
    for i in range(len(values)):
        step = dict(
            method="update",
            args=[{"visible": [False] * ((2 * len(values)) + 1)}, 
                  {"title": "Variación oferta: " + str(i + min_value)}],
        )
        
        step["args"][0]["visible"][0] = True # funcion de la oferta
        step["args"][0]["visible"][i + 1] = True
        step["args"][0]["visible"][len(values) + i + 1] = True 
        steps.append(step)
    
    sliders = [dict(
        active=(len(values) - 1)/2,
        currentvalue={"prefix": "Variación oferta: "},
        steps=steps
    )]
    
    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(max(cantidadDemanda), max(cantidadOferta))]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(max(precioDemanda), max(precioOferta))]),
        title="Variación oferta:" + str(0),
        sliders=sliders
    )

    fig.show()


def pintar_funcion_equilibrio_variacion_otros_demanda(cantidadOferta, precioOferta, funcionOferta, cantidadDemanda, precioDemanda, funcionDemanda, funcionEquilibrio):
    min_value = -20
    max_value = 20
    
    active = int(round((min_value + max_value)/2))

    values = range(min_value, max_value + 1)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=cantidadOferta, 
        y=precioOferta,
        mode='lines', 
        line=dict(color="#fabada", width=4), 
        name="Función de la oferta"))

    for step in values:
        variacionDemanda = [funcionDemanda(P, step) for P in precioDemanda]
        fig.add_trace(go.Scatter(visible=False, x=variacionDemanda, y=precioDemanda,mode='lines', line=dict(color="#00CED1", width=4), name="Función de la demanda"))
    
    for step in values:
        y = funcionEquilibrio(step, 0)
        x = funcionDemanda(y,step)
        fig.add_trace(go.Scatter(visible=False, x=[x], y=[y], marker=dict(size=20, color='#FF9900'), name="Equilibrio de mercado"))
    
    fig.data[round((len(values))/2) + 1].visible = True
    fig.data[round((len(values) + (len(values))/2) + 1)].visible = True
    
    steps = []
    for i in range(len(values)):
        step = dict(
            method="update",
            args=[{"visible": [False] * ((2 * len(values)) + 1)}, 
                  {"title": "Variación demanda: " + str(i + min_value)}],
        )
        
        step["args"][0]["visible"][0] = True # funcion de la demanda
        step["args"][0]["visible"][i + 1] = True
        step["args"][0]["visible"][len(values) + i + 1] = True 
        steps.append(step)
    
    sliders = [dict(
        active=(len(values) - 1)/2,
        currentvalue={"prefix": "Variación demanda: "},
        steps=steps
    )]

    fig.update_layout(
        xaxis_title="Cantidad", 
        xaxis=dict(range=[0, max(max(cantidadDemanda), max(cantidadOferta))]),
        yaxis_title="Precio",
        yaxis=dict(range=[0, max(max(precioDemanda), max(precioOferta))]),
        title="Variación demanda:" + str(0),
        sliders=sliders
    )

    fig.show()
