import streamlit as st
import openai
import time

# Configuración de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Título y descripción
st.title("🍏 NutriGen - Tu Asistente de Nutrición con IA")
st.markdown("""
Genera planes de alimentación personalizados basados en:
- 🥗 Tipo de dieta
- 🚫 Restricciones alimentarias
- 🎯 Objetivos específicos
""")

# Entradas del usuario
col1, col2 = st.columns(2)
with col1:
    dieta = st.selectbox("Selecciona tu dieta:", 
                       ["General", "Vegetariana", "Vegana", "Keto", "Baja en carbohidratos"])
with col2:
    objetivo = st.selectbox("Tu objetivo principal:", 
                          ["Perder peso", "Mantener peso", "Ganar masa muscular"])

alergias = st.text_input("Alergias o intolerancias alimentarias:")
dias = st.slider("Días a planificar:", 1, 7, 3)

# Botón de acción
if st.button("Generar Plan Nutricional"):
    if not alergias:
        alergias = "ninguna"
    
    with st.spinner("Creando tu plan personalizado..."):
        try:
            # Construcción del prompt específico
            prompt = f"""
            Como nutricionista profesional, genera un plan de comidas para {dias} días con estas características:
            - Tipo de dieta: {dieta}
            - Objetivo principal: {objetivo}
            - Alergias/intolerancias: {alergias}
            
            Formato requerido:
            1. Día por día
            2. Cada comida debe incluir:
               - Nombre del platillo
               - Ingredientes principales
               - Información nutricional destacada
            3. Máximo 500 tokens
            """
            
            # Llamada a la API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=600
            )
            
            # Procesamiento de la respuesta
            if response.choices:
                plan_nutricional = response.choices[0].message['content']
                
                # Mostrar resultados con formato
                st.success("¡Plan generado con éxito! Aquí tienes tu guía:")
                st.markdown(f"## 📅 Plan para {dias} días ({dieta})")
                st.markdown(f"**Objetivo:** {objetivo} | **Restricciones:** {alergias}")
                st.divider()
                st.markdown(plan_nutricional)
                
                # Botón de descarga
                st.download_button(
                    label="Descargar Plan",
                    data=plan_nutricional,
                    file_name=f"plan_nutricional_{dias}dias.txt"
                )
            else:
                st.error("No se pudo generar el plan. Intenta nuevamente.")
                
        except openai.error.AuthenticationError:
            st.error("Error de autenticación. Verifica tu API Key en Settings > Secrets.")
        except Exception as e:
            st.error(f"Error inesperado: {str(e)}")

# Sección informativa
st.markdown("---")
st.subheader("📌 ¿Cómo funciona?")
st.write("""
1. Selecciona tus preferencias dietéticas
2. Especifica cualquier restricción alimentaria
3. Elige el número de días a planificar
4. ¡Obtén un plan detallado con un clic!
""")