import streamlit as st
import numpy as np
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Datos faltantes')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            El manejo de datos faltantes es una parte crítica del análisis de datos con Pandas.
             Los datos faltantes son comunes en conjuntos de datos del mundo real y pueden afectar significativamente los resultados de tus análisis.
             Aprenderemos cómo identificar y manejar datos faltantes en Pandas.

            #### Identificación de Datos Faltantes
            Supongamos que tenemos un DataFrame con algunos datos faltantes:
            """)
st.code("""
        import pandas as pd
        import numpy as np

        data = {
            'A': [1, 2, np.nan, 4, 5],
            'B': [10, np.nan, np.nan, 40, 50]
        }

        df = pd.DataFrame(data)
        """)
st.markdown("""
            La constante [np.nan](https://numpy.org/doc/stable/reference/constants.html#) es la representación de valor **no numérico** (o faltante).
            
            Para identificar los valores faltantes en un DataFrame, podemos usar el método 
            [isna()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)
             o [isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html):
            """)
st.code("""
        # Identificar valores faltantes en el DataFrame
        valores_faltantes = df.isna()

        print(valores_faltantes)
        """)
# Generación de DataFrame Ejemplo
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, np.nan, 40, 50]
}
df = pd.DataFrame(data)
with st.expander("mostrar resultado:"):
    valores_faltantes = df.isna()
    st.dataframe(valores_faltantes)

st.markdown("""
            #### Conteo de Datos Faltantes
            Para obtener el recuento de valores faltantes en cada columna,
             podemos usar sum() después de isna():
            """)

st.code("""
        # Conteo de valores faltantes por columna
        conteo_faltantes_por_columna = df.isna().sum()

        print(conteo_faltantes_por_columna)
        """)
with st.expander("mostrar resultado:"):
    conteo_faltantes_por_columna = df.isna().sum()
    st.dataframe(conteo_faltantes_por_columna)


st.markdown("""
            #### Eliminación de Filas o Columnas con Datos Faltantes
            En algunos casos, podemos optar por eliminar filas o columnas que contengan datos faltantes.
            Para eliminar filas con al menos un valor faltante:
            """)
st.code("""
        # Eliminar filas con valores faltantes
        df_sin_faltantes_filas = df.dropna()

        print(df_sin_faltantes_filas)
        """)
st.write("Para eliminar columnas con al menos un valor faltante:")
st.code("""
        # Eliminar columnas con valores faltantes
        df_sin_faltantes_columnas = df.dropna(axis=1)

        print(df_sin_faltantes_columnas)
        """)

st.markdown("""
            #### Relleno de Datos Faltantes
            En lugar de eliminar datos faltantes, a veces es más apropiado rellenarlos con valores específicos.
             Para rellenar los valores faltantes con ceros:
            """)
st.code("""
        # Rellenar valores faltantes con ceros
        df_con_ceros = df.fillna(0)

        print(df_con_ceros)
        """)
with st.expander("mostrar resultado:"):
    df_con_ceros = df.copy()
    df_con_ceros = df.fillna(0)
    st.dataframe(df_con_ceros)

st.markdown("""
            #### Interpolación de Datos Faltantes
            La interpolación es útil cuando deseas estimar valores faltantes basados en los valores existentes en una serie de tiempo o secuencia.
             Por ejemplo:
            """)
st.code("""
        # Interpolación lineal para llenar valores faltantes
        df_interpolado = df.interpolate()

        print(df_interpolado)
        """)
with st.expander("mostrar resultado:"):
    df_interpolado = df.copy()
    df_interpolado = df.interpolate()
    st.dataframe(df_interpolado)

st.markdown("""
            #### Reemplazo de Datos Faltantes por Valor Específico
            Puedes reemplazar valores faltantes con un valor específico, como la dfesviación estándar de la columna:
            """)
st.code("""
        # Reemplazar valores faltantes con la media de la columna
        media = df['A'].mean()
        df['A'].fillna(media, inplace=True)

        print(df)
        """)
with st.expander("mostrar resultado:"):
    df_reemplazo = df.copy()
    desviacion_estandar = df_reemplazo['A'].std()
    df_reemplazo['A'].fillna(desviacion_estandar, inplace=True)
    st.dataframe(df_reemplazo)

st.markdown("""
            Manejar datos faltantes de manera efectiva es esencial para garantizar que tus análisis y resultados sean precisos.
             La elección de cómo manejar datos faltantes depende del contexto y los objetivos de tu análisis.
             Experimenta con diferentes enfoques para abordar datos faltantes en tus conjuntos de datos.
             ¡Sigue explorando y aprendiendo más sobre Pandas!
            """)