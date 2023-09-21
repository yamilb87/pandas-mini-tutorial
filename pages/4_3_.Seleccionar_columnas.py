import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('3. Seleccionar columnas')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este punto, nos centraremos en cómo seleccionar y trabajar con columnas específicas de un DataFrame.
             Aprenderemos a acceder a los datos que necesitamos para realizar análisis y operaciones relevantes.
            
            #### Acceder a una Columna por Nombre
            Supongamos que tenemos un DataFrame llamado 'df' que contiene datos sobre ventas de productos:
            """)
st.code("""
        import pandas as pd
        # Crear un DataFrame de ejemplo
        data = {
                'Producto': ['A', 'B', 'C', 'D','E', 'F', 'G'],
                'Ventas_Enero': [100, 150, 120, 80, 170, 165, 110],
                'Ventas_Febrero': [120, 130, 100, 90, 102, 150, 136]
                }

        df = pd.DataFrame(data)
        """,
        language="python")

# Generacion del DataFrame ejemplo
data = {
    'Producto': ['A', 'B', 'C', 'D','E', 'F', 'G'],
    'Ventas_Enero': [100, 150, 120, 80, 170, 165, 110],
    'Ventas_Febrero': [120, 130, 100, 90, 102, 150, 136]
}
df = pd.DataFrame(data)

st.markdown("""
            Para acceder a una columna específica, simplemente utilizamos la notación de corchetes o el operador de punto:
            """)

st.code("""
        # Acceder a la columna 'Producto' usando notación de corchetes
        productos = df['Producto']

        # Acceder a la columna 'Ventas_Enero' usando el operador de punto
        ventas_enero = df.Ventas_Enero

        print(productos)
        print(ventas_enero)
        """,
        language="python")

with st.expander("mostrar resultados"):
    tab1, tab2 = st.tabs(["Corchetes", "Punto"])

    with tab1:
        st.markdown("##### Acceso a columna utilizando notación de corchetes")
        st.success("Código ejecutado:  df['Producto']")
        st.dataframe(df['Producto'])

    with tab2:
        st.markdown("##### Acceso a columna utilizando notación de punto")
        st.success("Código ejecutado:  df.Ventas_Enero")
        st.dataframe(df.Ventas_Enero)


st.markdown("""
            #### Seleccionar Múltiples Columnas
            A menudo, necesitamos seleccionar más de una columna. Esto se puede hacer proporcionando una lista de nombres de columna:
            """)
st.code("""
        # Seleccionar múltiples columnas
        ventas = df[['Ventas_Enero', 'Ventas_Febrero']]

        print(ventas)
        """)

st.markdown("""
            #### Crear un Nuevo DataFrame con Columnas Seleccionadas
            Pandas nos permite crear un nuevo DataFrame que contenga solo las columnas que necesitamos:
            """)
st.code("""
        # Crear un nuevo DataFrame con columnas seleccionadas
        df_seleccionado = df[['Producto', 'Ventas_Enero']]

        print(df_seleccionado)
        """)

st.markdown("""
            #### Filtrar Filas Basadas en Valores de una Columna
            A veces, es necesario filtrar filas basadas en los valores de una columna. 
            Por ejemplo, si deseamos ver solo las filas donde las ventas de febrero superan cierto valor:
            """)
st.code("""
        # Filtrar filas donde las ventas de febrero son mayores que 110
        ventas_mayores_110 = df[df['Ventas_Febrero'] > 110]

        print(ventas_mayores_110)
        """)

with st.expander("mostrar resultado"):
    mes = st.selectbox("Seleccionar mes de ventas: ",options=df.columns[1:])
    limite_ventas = st.number_input("Ingresar valor límite: ",
                                    min_value=df[mes].min(),
                                    max_value=df[mes].max(),
                                    value=110)
    operador = st.selectbox("Seleccionar operador: ",options=["<","<=",">",">=","==","!="])
    st.dataframe(eval(f"df[df['{mes}']{operador}{limite_ventas}]"))

st.markdown("""
            #### Acceder a Datos Únicos en una Columna
            Para obtener valores únicos de una columna, podemos usar el método 
            _[unique()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html)_:
            """)
    
st.code("""
        # Obtener valores únicos de la columna 'Producto'
        productos_unicos = df['Producto'].unique()

        print(productos_unicos)
        """)    

st.markdown("""
            Estos ejemplos te ayudarán a comenzar a seleccionar y trabajar con columnas específicas en Pandas.
             A medida que avancemos en este tutorial, exploraremos técnicas más avanzadas
             para realizar análisis de datos y manipulaciones complejas en DataFrames.
             ¡Sigamos explorando y aprendiendo juntos!
            """)