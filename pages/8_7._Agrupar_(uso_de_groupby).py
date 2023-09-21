import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('7. Agrupar (uso de "groupby")')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            La agrupación de datos es esencial para realizar análisis de datos agregados en Pandas.
             La función _[groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)_
             nos permite agrupar filas de un DataFrame en función de los valores de una o varias columnas.
             A continuación, exploraremos cómo utilizar _[groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)_
             para realizar operaciones de agregación en los grupos.

            #### Creación de un DataFrame de Ejemplo
            Supongamos que tenemos un DataFrame con información de ventas por región y producto:
            """)
st.code("""
        import pandas as pd

        data = {
            'Producto': ['A', 'B', 'A', 'B', 'A', 'B'],
            'Region': ['Norte', 'Norte', 'Sur', 'Sur', 'Este', 'Este'],
            'Ventas': [100, 150, 120, 80, 200, 250]
        }

        df = pd.DataFrame(data)
        """)

# Generación de Dataframe Ejemplo
data = {
            'Producto': ['A', 'B', 'A', 'B', 'A', 'B'],
            'Region': ['Norte', 'Norte', 'Sur', 'Sur', 'Este', 'Este'],
            'Ventas': [100, 150, 120, 80, 200, 250]
        }

df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("""
            #### Agrupar Datos por una Columna
            Para agrupar los datos por una columna, como 'Region', y calcular la suma de las ventas en cada región:
            """)
st.code("""
        # Agrupar por la columna 'Region' y calcular la suma de las ventas
        ventas_por_region = df.groupby('Region')['Ventas'].sum()

        print(ventas_por_region)
        """)
with st.expander("mostrar resultado:"):
    ventas_por_region = df.groupby('Region')['Ventas'].sum()
    st.dataframe(ventas_por_region)    

st.markdown("""
            #### Agrupar por Múltiples Columnas
            También podemos agrupar por múltiples columnas. Por ejemplo, si queremos ver las ventas por producto y región:
            """)
st.code("""
        # Agrupar por 'Producto' y 'Region' y calcular la suma de las ventas
        ventas_por_producto_region = df.groupby(['Producto', 'Region'])['Ventas'].sum()

        print(ventas_por_producto_region)
        """)
with st.expander("mostrar resultado:"):
    ventas_por_producto_region = df.groupby(['Producto', 'Region'])['Ventas'].sum()
    st.dataframe(ventas_por_producto_region)

st.markdown("""
            #### Aplicar Múltiples Funciones de Agregación
            Pandas nos permite aplicar varias funciones de agregación a los grupos.
             Por ejemplo, podemos calcular tanto la suma como el promedio de ventas por producto:
            """)
st.code("""
        # Aplicar múltiples funciones de agregación
        agregaciones = {
            'Ventas': ['sum', 'mean']
        }

        resultados = df.groupby('Producto').agg(agregaciones)

        print(resultados)
        """)
with st.expander("mostrar resultado:"):
    agregaciones = {'Ventas': ['sum', 'mean']}
    resultados = df.groupby('Producto').agg(agregaciones)
    st.dataframe(resultados)

st.markdown("""
            #### Resetear el Índice después de la Agrupación
            A veces, después de agrupar, es útil restablecer el índice del DataFrame resultante.
             Esto se puede hacer utilizando reset_index():
            """)
st.code("""
        # Resetear el índice después de la agrupación
        resultados_reset = resultados.reset_index()

        print(resultados_reset)
        """)

st.markdown("""
            ##### Comparación con **SQL**:

            El ejemplo anterior, es equivalente a ejecutar el siguiente código en [SQL](https://es.wikipedia.org/wiki/SQL)            
            """)
st.code("""
        SELECT
            Producto,
            SUM(Ventas) AS Suma_Ventas,
            AVG(Ventas) AS Promedio_Ventas
        FROM
            NombreDeTabla
        GROUP BY
            Producto;
        """,
        language="sql")

st.markdown("""
            La agrupación es una herramienta poderosa en Pandas para realizar análisis de datos agregados y resúmenes.
             Experimenta con diferentes combinaciones de columnas y funciones de agregación para comprender mejor tus datos
             y responder preguntas específicas sobre ellos.
             ¡Sigue explorando y aprendiendo más sobre Pandas!
            """)