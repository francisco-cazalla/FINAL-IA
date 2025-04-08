import streamlit as st
import openai
import time

# Configuración
openai.api_key = st.secrets["OPENAI_API_KEY"]

# UI
st.title("Asistente de IA 🤖")
query = st.text_input("Escribe tu pregunta:")

if st.button("Generar respuesta"):
    if not query:
        st.warning("⚠️ Escribe una pregunta primero!")
        st.stop()
    
    with st.spinner("Procesando..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente útil. Responde de forma concisa."},
                    {"role": "user", "content": query}
                ],
                temperature=0.5,
                max_tokens=500
            )
            
            if response.choices:
                respuesta = response.choices[0].message['content']
                st.subheader("Respuesta:")
                st.markdown(f"```\n{respuesta}\n```")
                st.balloons()
            else:
                st.error("No se recibió respuesta de la IA")
                
        except openai.error.AuthenticationError:
            st.error("Error de autenticación. Verifica tu API Key.")
        except openai.error.RateLimitError:
            st.error("Límite de uso alcanzado. Espera 20 segundos.")
            time.sleep(20)
        except Exception as e:
            st.error(f"Error inesperado: {str(e)}")