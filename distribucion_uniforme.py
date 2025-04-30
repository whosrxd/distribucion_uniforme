import streamlit as st
import pandas as pd
import random

# Configuración para pantalla completa
st.set_page_config(layout = "wide")

st.title("Distribución Uniforme")
st.divider()

col1, col2 = st.columns([1, 2], gap = "large")

with col1:
    a = st.number_input("Ingresa el valor a", min_value = 0, step = 1)
    b = st.number_input("Ingresa el valor b", min_value = 0, step = 1)
    dias = st.number_input("Número de días", min_value = 0, step = 1)
    
    aleatorio = []
    
    for i in range(dias):
        num = random.random()
        aleatorio.append(num)
        
    # Generando Números Aleatorios
    altura = []
    
    for i in range(dias):
        num = a + (b - a) * aleatorio[i]
        altura.append(num)
  
with col2:
    if a < b and dias:
        df = pd.DataFrame({
                "Medición": [f"{i+1}" for i in range(dias)],
                "ri": aleatorio,
                "Altura": altura
        })
        
        # Agregando el promedio total
        df.loc[len(df)] = ["Promedio", None, df["Altura"].mean()]
        
        st.dataframe(df, use_container_width = True, hide_index = True)
    else:
        str.error("Por favor, ingresa valores válidos para a, b y días.", icon = ":material/warning:")
