import streamlit as st
import pickle

# Cargar modelo
model = pickle.load(open("modelo_entrenado.pkl", "rb"))

st.title("🔐 Detector de Cifrados con IA")

texto = st.text_area("Ingresa el texto:")

if st.button("Analizar"):
    if texto:
        resultado = model.predict([texto])
        st.success(f"Resultado: {resultado[0]}")
    else:
        st.warning("Ingresa un texto")