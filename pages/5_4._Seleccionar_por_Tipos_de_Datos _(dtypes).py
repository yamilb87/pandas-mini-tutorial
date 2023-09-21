import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Seleccionar por Tipo de Datos')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En Pandas, es común trabajar con conjuntos de datos que contienen diferentes tipos de datos en sus columnas.
             Aprender a seleccionar columnas basadas en sus tipos de datos es fundamental para el análisis de datos efectivo.
             Aquí te mostraremos cómo hacerlo:

            #### Identificar los Tipos de Datos de las Columnas
            Antes de seleccionar columnas por tipos de datos, es útil conocer los tipos de datos presentes en el DataFrame.
             Esto se puede hacer utilizando el atributo 
            [dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html):
            """)

st.code("""
        # Obtener los tipos de datos de cada columna
        tipos_de_datos = df.dtypes
        print(tipos_de_datos)
        """)

st.markdown("""
            #### Seleccionar Columnas por Tipo de Dato
            Supongamos que tenemos un DataFrame df con columnas que contienen tipos de datos mixtos,
             incluyendo números enteros, números de punto flotante y cadenas.
             Ahora, deseamos seleccionar solo las columnas numéricas.
            """)
st.code("""
        # Seleccionar solo las columnas numéricas
        columnas_numericas = df.select_dtypes(include=['int64', 'float64'])

        print(columnas_numericas)
        """)

st.markdown("""
            #### Seleccionar Columnas Excluyendo un Tipo de Dato
            A veces, es útil seleccionar todas las columnas excepto las de un tipo de dato en particular.
             Supongamos que queremos seleccionar todas las columnas excepto las cadenas (objetos):
            """)
st.code("""
        # Seleccionar todas las columnas excepto las de tipo objeto
        columnas_no_objeto = df.select_dtypes(exclude=['object'])

        print(columnas_no_objeto)
        """)

st.markdown("""
            #### Realizar Operaciones en Columnas Seleccionadas por Tipo de Dato
            Una vez que hayas seleccionado columnas por tipo de dato, puedes realizar operaciones específicas en ellas.
             Por ejemplo, si deseas calcular la suma de todas las columnas numéricas:
            """)
st.code("""
        # Calcular la suma de las columnas numéricas
        suma_columnas_numericas = columnas_numericas.sum()

        print(suma_columnas_numericas)
        """)

# Generamos un df ejemplo para visualizar 
data = {
    'Producto': ['A', 'B', 'C', 'D','E','F','G'],
    'Precio': [102.5, 1500.0, 1230.0, 810.8, 680.2, 459.7, 1044.6],
    'Costo': [50.6, 945.9, 762.5, 520.2, 402.3, 292.4, 684.6]
}
df = pd.DataFrame(data)

with st.expander("mostrar resultado"):
    st.write("Utilizando el siguiente dataframe como ejemplo:")
    st.dataframe(df)
    
    operaciones = {'suma': "sum",
                   'promedio': "mean",
                   'desviación estándar': "std"}
    operacion = st.selectbox("Seleccionar operación: ",options=operaciones)
    columnas_numericas = df.select_dtypes(exclude=['object'])
    st.dataframe(columnas_numericas.agg(operaciones[operacion]))


st.markdown("""
            #### Trabajar con Datos Seleccionados
            Una vez que tengas las columnas seleccionadas por tipo de dato, puedes realizar análisis estadísticos,
             visualizaciones o cualquier otra operación específica que necesites en esas columnas.

            Este conocimiento te permitirá trabajar de manera más efectiva con conjuntos de datos heterogéneos y
             seleccionar las columnas que son relevantes para tu análisis.
             ¡Continúa explorando y practicando estas técnicas para mejorar tus habilidades en Pandas!
            """)