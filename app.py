import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv(r'C:\Users\Lorenzo\Desktop\ORDER_L8R\Data_Analysis\TripleTen\Sprints\Sprint_4\Notebooks\Capitulo_7\proyecto_sprint_4\vehicles_us.csv', sep=',')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button: # al hacer clic en el botón del histograma
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear otro botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón del gráfico de dispersión
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
