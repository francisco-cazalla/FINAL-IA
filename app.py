# app.py 
import streamlit as st
import openai

# 1. Configuración inicial 
st.set_page_config(page_title="Mi App con IA", page_icon="✔")

# 2. Componentes principales 
st.title("Mi Aplicación Inteligente")
st.write("Bienvenido a mi app que resuelve [problema específico] usando IA")

# 3. Entradas de usuario 
user_input = st.text_input("Ingresa tu consulta:")
option = st.selectbox("Elige una opción", ["Opción 1", "Opción 2"])

# 4. Botón de acción 
if st.button("Ejecutar"):
    # Lógica de procesamiento con IA
    def procesar_con_ia(input, opcion):
        # Implementar lógica real de IA aquí
        return f"Procesado: {input} con {opcion}"
    
    resultado = procesar_con_ia(user_input, option)
    st.write("Resultado:", resultado)

# Componentes adicionales corregidos
texto = st.text_area("Describe tu problema:", height=150)

opciones = st.multiselect("Preferencias:", ["Vegetariano", "Vegano", "Sin gluten"])

archivo = st.file_uploader("Sube tu documento:", type=["pdf", "txt"])

nivel = st.slider("Nivel de detalle:", 1, 5, 3)

# Columnas 
col1, col2 = st.columns(2)
with col1:
    st.number_input("Edad:", min_value=18, max_value=100)

# Expanders 
with st.expander("Ver instrucciones"):
    st.markdown("1. Ingresa tus datos\n2. Presiona el botón\n3. Espera resultados")

# Progress bar 
import time
with st.spinner("Procesando..."):
    time.sleep(2)
    st.success("Listo!")

# Configuración OpenAI (agregar en secrets.toml)
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generar_respuesta(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']