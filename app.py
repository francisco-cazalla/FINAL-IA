import streamlit as st
import openai

# Configuración de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Título y descripción
st.title("NutriAI: Planificador de Comidas Inteligente")
st.markdown("""
🍎 ¡Planifica tus comidas semanales con IA!
Esta aplicación genera planes de alimentación personalizados considerando:
- Preferencias dietéticas
- Restricciones alimentarias
- Objetivos nutricionales
""")

# Entradas de usuario
dietas = st.multiselect("Selecciona tu dieta:", ["Vegetariana", "Vegana", "Sin gluten", "Keto", "Baja en carbohidratos"])
alergias = st.text_input("Alergias alimentarias:")
objetivos = st.selectbox("Tu objetivo principal:", ["Perder peso", "Mantener peso", "Ganar masa muscular"])
dias = st.slider("Días a planificar:", 1, 7, 5)

# Botón de acción
if st.button("Generar Plan Nutricional"):
    with st.spinner("Creando tu plan personalizado..."):
        try:
            prompt = f"""
            Crea un plan de comidas para {dias} días que sea {', '.join(dietas)}.
            Considera estas alergias: {alergias}. Objetivo principal: {objetivos}.
            Incluye desayuno, almuerzo, merienda y cena.
            Formato: Lista con días, comidas e ingredientes principales.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            st.success("¡Plan generado con éxito!")
            st.markdown("### Tu Plan Nutricional Personalizado")
            st.write(response.choices[0].message['content'])
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Sección "Cómo funciona"
st.markdown("---")
st.subheader("📌 Cómo funciona:")
st.write("""
1. Selecciona tus preferencias dietéticas
2. Especifica alergias o restricciones
3. Elige tu objetivo principal
4. ¡Genera tu plan con un clic!
""")