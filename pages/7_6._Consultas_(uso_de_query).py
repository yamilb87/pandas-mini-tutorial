import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Consultas (uso de "query")')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            Las consultas en Pandas son una forma poderosa de filtrar y seleccionar datos de un DataFrame basándonos en condiciones lógicas de una manera más legible y expresiva.
             Vamos a explorar cómo utilizar la función [query()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) para realizar consultas en nuestros DataFrames.

            #### Consultas Simples
            Supongamos que tenemos un DataFrame df con información sobre estudiantes y sus calificaciones:
            """)
st.code("""
        import pandas as pd

        data = {
            'Nombre': ['Ana', 'Juan', 'Luis', 'María'],
            'Edad': [20, 22, 21, 23],
            'Promedio': [85.5, 90.0, 88.0, 92.5]
        }

        df = pd.DataFrame(data)
        """)
st.write("Para realizar una consulta simple y seleccionar a los estudiantes mayores de 21 años:")
st.code("""
        # Realizar una consulta para seleccionar estudiantes mayores de 21 años
        consulta_resultado = df.query('Edad > 21')

        print(consulta_resultado)
        """)

st.markdown("""
            #### Consultas con Operadores Lógicos
            Pandas nos permite combinar condiciones utilizando operadores lógicos como & (and) y | (or).
             Por ejemplo, para seleccionar estudiantes mayores de 20 años con un promedio mayor o igual a 90:
            """)
st.code("""
        # Consulta con operadores lógicos
        consulta_resultado = df.query('Edad > 20 & Promedio >= 90')

        print(consulta_resultado)
        """)

st.markdown("""
            #### Usando Variables en Consultas
            También podemos utilizar variables en nuestras consultas. 
            Supongamos que queremos seleccionar estudiantes con un promedio mayor o igual a una calificación mínima,
             donde la calificación mínima es una variable:
            """)
st.code("""
        # Definir la calificación mínima
        calificacion_minima = 88.0

        # Realizar una consulta con una variable
        consulta_resultado = df.query('Promedio >= @calificacion_minima')

        print(consulta_resultado)
        """)

st.markdown("""
            #### Consultas con Texto
            Para consultas basadas en texto, podemos usar comillas simples o dobles dentro de la consulta.
             Por ejemplo, para seleccionar a los estudiantes cuyos nombres contienen la letra 'a':
            """)
st.code("""
        # Consulta con texto
        consulta_resultado = df.query('Nombre.str.contains("a")', engine='python')

        print(consulta_resultado)
        """)

st.markdown("""
        La función _[query()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)_
        en Pandas es una herramienta poderosa para realizar filtrados avanzados de datos de manera clara y concisa.
        Experimenta con diferentes condiciones y practica las consultas para mejorar tus habilidades en el análisis de datos con Pandas.
        ¡Sigue explorando y aprendiendo!
            """)