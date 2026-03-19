import streamlit as st
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier  # o el modelo que uses

st.set_page_config(page_title="Cifrado IA", page_icon="🔐")

st.title("🔐 Aplicación de Cifrado con IA")
st.write("Bienvenido a la aplicación de cifrado")

# Cargar modelo
try:
    modelo = joblib.load("modelo_entrenado.pkl")
    st.success("✅ Modelo cargado correctamente")
except Exception as e:
    st.error(f"❌ Error al cargar el modelo: {e}")

# Interfaz simple
texto = st.text_input("Ingresa texto para procesar:")
if st.button("Procesar"):
    st.write(f"Procesando: {texto}")