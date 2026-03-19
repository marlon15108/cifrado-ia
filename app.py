import streamlit as st
import joblib

# Cargar modelo correctamente
model = joblib.load("modelo_entrenado.pkl")

st.title("🔐 Detector de Cifrados con IA")

texto = st.text_area("Ingresa el texto:")

if st.button("Analizar"):
    if texto:
        resultado = model.predict([texto])
        st.success(f"Resultado: {resultado[0]}")
    else:
        st.warning("Ingresa un texto")