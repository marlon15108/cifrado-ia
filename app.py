import streamlit as st
import joblib

st.title("🔐 Detector de Cifrados con IA")

# Cargar modelo con control de error
try:
    model = joblib.load("modelo_entrenado.pkl")
    st.success("Modelo cargado correctamente")
except Exception as e:
    st.error(f"Error cargando modelo: {e}")
    st.stop()

texto = st.text_area("Ingresa el texto:")

if st.button("Analizar"):
    if texto:
        try:
            resultado = model.predict([texto])
            st.success(f"Resultado: {resultado[0]}")
        except Exception as e:
            st.error(f"Error en predicción: {e}")
    else:
        st.warning("Ingresa un texto")