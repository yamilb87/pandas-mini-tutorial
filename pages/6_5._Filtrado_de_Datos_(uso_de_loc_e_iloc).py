import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('5. Filtrado de Datos (uso de "loc" e "iloc")')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            El filtrado de datos es una operación fundamental en el análisis de datos con Pandas.
             Permite seleccionar un subconjunto de filas y columnas basado en condiciones específicas. Vamos a explorar cómo realizar filtrados utilizando las funciones loc e iloc.

            ##### Filtrado con ["loc"](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) (Filtrado por Etiqueta)
            La función loc se utiliza para realizar filtrados basados en etiquetas de fila y columna.
             Supongamos que tenemos un DataFrame df con etiquetas de fila y nombres de columna:
            """)
st.code("""
        import pandas as pd

        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        }

        df = pd.DataFrame(data, index=['fila1', 'fila2', 'fila3', 'fila4', 'fila5'])
        """)

st.write("Con el código anterior, obtendremos el siguiente DataFrame: ")
# Generación del dataframe ejemplo
data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        }
df = pd.DataFrame(data, index=['fila1', 'fila2', 'fila3', 'fila4', 'fila5'])
st.dataframe(df)

st.write("Para filtrar filas basadas en etiquetas de fila, utilizamos loc de la siguiente manera:")
st.code("""
        # Filtrar filas por etiquetas de fila
        fila_seleccionada = df.loc['fila3']

        print(fila_seleccionada)
        """)


with st.expander("mostrar resultado:"):
    fila = st.selectbox("Seleccionar fila: ",options=df.index)
    fila_seleccionada = df.loc[fila]
    st.dataframe(fila_seleccionada)

st.write("Para filtrar filas y columnas simultáneamente:")
st.code("""
        # Filtrar filas y columnas por etiquetas
        subset = df.loc[['fila1', 'fila3'], ['A']]

        print(subset)
        """)

st.markdown("""
            #### Filtrado con ["iloc"](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html) (Filtrado por Índice Entero)
            La función iloc se utiliza para realizar filtrados basados en índices enteros de fila y columna. Por ejemplo:
            """)
st.code("""
        # Filtrar filas y columnas por índices enteros
        subset = df.iloc[1:4, 0]

        print(subset)
        """)

st.markdown("""
            #### Filtrado Basado en Condiciones Lógicas
            Una de las aplicaciones más poderosas del filtrado es seleccionar filas que cumplan ciertas condiciones lógicas.
             Supongamos que queremos seleccionar las filas donde el valor en la columna 'A' sea mayor que 3:
            """)
st.code("""
        # Filtrar filas basadas en una condición lógica
        condicion = df['A'] > 3
        filas_cumplen_condicion = df.loc[condicion]

        print(filas_cumplen_condicion)
        """)

st.markdown("""
            #### Combinación de Condiciones Lógicas
            Puedes combinar múltiples condiciones lógicas utilizando los operadores & (and) y | (or).
             Por ejemplo, para seleccionar las filas donde 'A' sea mayor que 2 y 'B' sea menor que 40:
            """)
st.code("""
        # Combinar condiciones lógicas con &
        condicion = (df['A'] > 2) & (df['B'] < 40)
        filas_cumplen_condicion = df.loc[condicion]

        print(filas_cumplen_condicion)
        """)
with st.expander("mostrar resultado:"):    
    st.dataframe((df['A'] > 2) & (df['B'] < 40))
    st.write("_Como podemos apreciar, sólo la **'Fila3'** cumple con la condición._")

st.markdown("""
            Estas técnicas de filtrado te permiten explorar y extraer datos específicos de tus DataFrames en función de tus necesidades de análisis.
             Experimenta con diferentes condiciones y práctica el filtrado de datos para mejorar tus habilidades en Pandas.
             ¡Sigue adelante y continúa aprendiendo!
            """)