import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv(r'C:\Users\Lorenzo\Desktop\ORDER_L8R\Data_Analysis\TripleTen\Sprints\Sprint_4\Notebooks\Capitulo_7\proyecto_sprint_4\vehicles_us.csv', sep=',')

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # Si la casilla de verificación del histograma está seleccionada
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odómetro")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter_plot = st.checkbox('Construir gráfico de dispersión')

if build_scatter_plot: # Si la casilla de verificación del gráfico de dispersión está seleccionada
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)