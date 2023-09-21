import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Combinar Datos (usos de "concat" y "merge")')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este capítulo, exploraremos cómo combinar y unir conjuntos de datos utilizando Pandas.
             Aprenderemos sobre las funciones [join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html),
             [concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html), y
             [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html),
             y cómo se utilizan para combinar datos de diferentes fuentes.

            #### La Función [join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html) en Pandas
            La función join en Pandas se utiliza para combinar dos DataFrames basados en una columna común,
             similar a cómo se hace en **SQL** con la operación JOIN.
             A continuación, se muestra un ejemplo de cómo usar join:
            """)
st.code("""
        import pandas as pd

        # Crear dos DataFrames
        df1 = pd.DataFrame({'clave': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
        df2 = pd.DataFrame({'clave': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

        # Usar join para combinar los DataFrames en función de la columna 'clave'
        resultado = df1.join(df2.set_index('clave'), on='clave')

        print(resultado)
        """)

# Generacion de DataFrames para ejemplo
df1 = pd.DataFrame({'clave': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
df2 = pd.DataFrame({'clave': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

with st.expander("mostrar resultado"):
    # Usar join para combinar los DataFrames en función de la columna 'clave'
    resultado = df1.join(df2.set_index('clave'), on='clave')
    st.dataframe(resultado)

st.markdown("""
            En este ejemplo, hemos creado dos DataFrames, df1 y df2,
             y luego utilizamos join para combinarlos en función de la columna 'clave'.
             El resultado será un nuevo DataFrame que contiene las columnas de ambos DataFrames,
             alineadas por la columna 'clave'.
            
            #### La Función [concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) en Pandas
            
            La función concat en Pandas se utiliza para concatenar (unir) DataFrames a lo largo de un eje (fila o columna).
             Aquí tienes un ejemplo de cómo usar concat para unir DataFrames a lo largo de filas:
            """)

st.code("""
        import pandas as pd

        # Crear dos DataFrames
        df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
        df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

        # Usar concat para unir los DataFrames a lo largo de filas (eje 0)
        resultado = pd.concat([df1, df2])

        print(resultado)
        """)
# Crear dos DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

with st.expander("mostrar resultado"):
    # Usar concat para unir los DataFrames a lo largo de filas (eje 0)
    resultado = pd.concat([df1, df2])
    st.dataframe(resultado)


st.markdown("""
            En este ejemplo, hemos creado dos DataFrames, df1 y df2, y luego utilizamos concat para unirlos a lo largo de filas. El resultado es un nuevo DataFrame que contiene las filas de ambos DataFrames.

            #### La Función [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) en Pandas
            La función merge en Pandas es similar a una operación de join en SQL.
             Se utiliza para combinar DataFrames en función de columnas específicas,
             pero ofrece una mayor flexibilidad y control para definir cómo se realiza la combinación
             (por ejemplo, utilizando diferentes tipos de uniones: 'inner', 'outer', 'left', 'right').
             Aquí tienes un ejemplo de cómo usar _merge_:
            """)


st.code("""
        import pandas as pd

        # Crear dos DataFrames
        df1 = pd.DataFrame({'clave': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
        df2 = pd.DataFrame({'clave': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

        # Usar merge para combinar los DataFrames en función de la columna 'clave'
        resultado = pd.merge(df1, df2, on='clave', how='inner')

        print(resultado)
        """)

 # Crear dos DataFrames
df1 = pd.DataFrame({'clave': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
df2 = pd.DataFrame({'clave': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

# Usar merge para combinar los DataFrames en función de la columna 'clave'
resultado = pd.merge(df1, df2, on='clave', how='inner')

with st.expander("mostrar resultado"):
    st.dataframe(resultado)

st.markdown("""
            En este ejemplo, hemos creado dos DataFrames, df1 y df2, y luego utilizamos merge para combinarlos en función de la columna 'clave' utilizando una unión interna ('inner'). El resultado contiene solo las filas con claves comunes en ambos DataFrames.

            ---

            #### Diferencias entre _'join', 'concat' y 'merge'_
            Es importante comprender las diferencias clave entre join, concat y merge en Pandas:

            **[join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)**: Se utiliza para combinar DataFrames basados en índices o columnas específicas.
             Es especialmente útil cuando quieres combinar DataFrames en función de una columna común.

            [**concat**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html): Se utiliza para concatenar (unir) DataFrames a lo largo de un eje (fila o columna).
             No requiere una columna común y simplemente apila DataFrames uno encima del otro o uno al lado del otro.

           **[merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)**: Es similar a una operación de join en SQL.
             Se utiliza para combinar DataFrames en función de columnas específicas,
             pero ofrece una mayor flexibilidad y control para definir cómo se realiza la combinación (por ejemplo, utilizando diferentes tipos de uniones: 'inner', 'outer', 'left', 'right').

            En resumen, si deseas combinar DataFrames en función de columnas específicas,
             **join** y **merge** son las opciones más adecuadas.
             Si solo deseas apilar DataFrames sin una columna común, concat es la elección adecuada.

            ---

            _**Conclusiones**_

            _En este capítulo, hemos explorado las funciones **join, concat y merge en Pandas
             y hemos discutido cómo se utilizan para combinar y unir conjuntos de datos.
             Cada una de estas funciones tiene su propio propósito y
             uso en la combinación de conjuntos de datos en Pandas._            
            """)