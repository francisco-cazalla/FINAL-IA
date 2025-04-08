import streamlit as st
import openai
from openai import OpenAI  # Nueva forma de importar
import time

# Configuración de OpenAI (versión actualizada)
# Configuración CORRECTA (nuevo formato)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]["key"])  # Clave desde Secrets

# Interfaz de usuario (manteniendo tu diseño nutricional)
st.title("🍏 NutriGen - Planificador Nutricional")
with st.expander("ℹ️ Instrucciones"):
    st.write("Complete sus preferencias y haga clic en Generar")

dieta = st.selectbox("Tipo de dieta:", ["General", "Vegetariana", "Vegana", "Keto"])
objetivo = st.selectbox("Objetivo:", ["Perder peso", "Mantener peso", "Ganar músculo"])

if st.button("Generar Plan"):
    with st.spinner("Creando tu plan..."):
        try:
            # Prompt mejorado para nutrición
            prompt = f"""Como nutricionista certificado, genera un plan para:
            - Dieta: {dieta}
            - Objetivo: {objetivo}
            Incluye desayuno, almuerzo y cena con:
            1. Nombre del plato
            2. Ingredientes
            3. Valor nutricional destacado
            Formato: Lista por días"""
            
            # Llamada API actualizada
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800
            )
            
            # Mostrar resultado
            st.success("¡Plan listo!")
            st.markdown(response.choices[0].message.content)

        except Exception as e:  # Captura todos los errores
            st.error(f"Error: {str(e)}")
            st.info("🔍 Verifique su conexión o API Key en Settings > Secrets")