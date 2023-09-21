import streamlit as st
import numpy as np
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('2. Bases de los DataFrames')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            Ahora que hemos aprendido cómo cargar datos en Pandas, es esencial comprender la estructura fundamental de los DataFrames y cómo interactuamos con ellos.
             Los DataFrames son como hojas de cálculo enriquecidas que nos permiten almacenar y manipular datos de manera eficiente.
            
            #### Crear un DataFrame
            Comencemos creando un DataFrame desde cero. Supongamos que queremos almacenar información sobre algunos estudiantes:
            ```python
            import pandas as pd

            # Crear un DataFrame desde un diccionario
            data = {
                'Nombre': ['Ana', 'Juan', 'Luis', 'María'],
                'Edad': [20, 22, 21, 23],
                'Promedio': [85.5, 90.0, 88.0, 92.5]
            }

            df = pd.DataFrame(data)

            # Visualizar el DataFrame
            print(df)
            ```

            El código anterior crea un DataFrame a partir de un diccionario de datos.
             Cada clave en el diccionario se convierte en una columna en el DataFrame.
            """)

# Generación del dataframe
data = {
    'Nombre': ['Ana', 'Juan', 'Luis', 'María'],
    'Edad': [20, 22, 21, 23],
    'Promedio': [85.5, 90.0, 88.0, 92.5]
}

df = pd.DataFrame(data)

with st.expander("mostrar resultado"):
    st.dataframe(df)

st.markdown("""
            #### Explorar la Estructura del DataFrame
            Para comprender mejor nuestro DataFrame, aquí hay algunas operaciones comunes que podemos realizar:

            ##### a) Ver las primeras filas del DataFrame: 
            Con el método [head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)
            obtenemos las primeras _n filas_ (el valor por default es _n=5_)           
            """)
st.code("""
            # Mostrar las primeras 3 filas del DataFrame
            print(df.head(3))
           
        """, language="python")

with st.expander("mostrar resultado"):
    st.dataframe(df.head(3))
    st.markdown("""
             _Solo se aprecian las primeras 3 columnas. También es posible visualizar las últimas filas
             del DataFrame, con el uso del método [tail()](https://pandas.pydata.org/docs/reference/api/pandas.Series.tail.html)_
             """)


st.markdown("""
            ##### b) Obtener estadísticas descriptivas:
            
            """)
st.code("""
        # Obtener estadísticas descriptivas de las columnas numéricas
        print(df.describe())
        """,
        language="python")

with st.expander("mostrar resultado"):
    st.dataframe(df.describe())


st.markdown("""
            ##### c) Acceder a las columnas:
            """)
st.code("""
        # Acceder a la columna 'Edad'
        edades = df['Edad']
        print(edades)
        """,
        language="python"
        )

with st.expander("mostrar resultado"):
    filtro = st.selectbox("Seleccionar columna: ", options=df.columns,)
    st.success(f"Código ejecutado:  df['{filtro}']")
    st.dataframe(df[filtro])


st.markdown("""
            ##### d) Agregar una nueva columna:            
            """)
st.code("""
        # Agregar una columna 'Género'
        df['Género'] = ['F', 'M', 'M', 'F']
        print(df)
        """)

with st.expander("mostrar resultado"):
    df2 = df.copy()
    df2['Género'] = ['F', 'M', 'M', 'F']
    st.dataframe(df2)


st.markdown("""
            #### Dimensiones del DataFrame
            Podemos verificar las dimensiones de nuestro DataFrame utilizando el atributo
             [shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html): 
            """)
st.code("""
        # Obtener las dimensiones del DataFrame (filas, columnas)
        print(df.shape)
        """,
        language="python")

with st.expander("mostrar resultado"):
    st.write(f"El dataframe tiene las siguientes dimensiones: {df2.shape}")

st.markdown("""
            #### Acceder a Datos en el DataFrame
            ##### a) Acceder a una celda específica 
            (uso de método [at()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html)):
            """)
st.code("""
            # Acceder al promedio de María (fila 3, columna 'Promedio')
            promedio_maria = df.at[3, 'Promedio']
            print(promedio_maria)
        """,
        language="python")

with st.expander("mostrar resultado"):
    fila_especifica = st.number_input("Fila: ",min_value=0,max_value=df2.shape[0]-1, value=3)
    columna_especifica = st.selectbox("Seleccionar columna: ", ['Nombre','Edad','Promedio','Género'])
    st.success(f"Código ejecutado:  df.at[{fila_especifica},'{columna_especifica}']")
    st.write(f"Valor seleccionado: {df2.at[fila_especifica,columna_especifica]}")