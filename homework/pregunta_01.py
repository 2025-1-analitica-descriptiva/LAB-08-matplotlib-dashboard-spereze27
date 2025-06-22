# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os
def load_data():
    df=pd.read_csv('files/input/shipping-data.csv')
    return df
def visual_warehouse(df,ruta):
    df = df.copy()
    plt.figure()
    conteo = df['Warehouse_block'].value_counts()
    conteo.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize=8,
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # Guardar la figura
    plt.tight_layout()
    plt.savefig(os.path.join(ruta, 'shipping_per_warehouse.png'))
    plt.close() 
def visual_mode_shipment(df,ruta):
    df = df.copy()
    plt.figure()
    conteo = df['Mode_of_Shipment'].value_counts()
    conteo.plot.pie(
        title='Mode of Shipment',
        wedgeprops=dict(width=0.35),
        ylabel='',
        color=['tab:blue','tab:orange','tab:green'],
    )
    # Guardar la figura
    plt.tight_layout()
    plt.savefig(os.path.join(ruta, 'mode_of_shipment.png'))
    plt.close() 

def visual_customer_rating(df, ruta):
    # Asegura que el directorio exista
    os.makedirs(ruta, exist_ok=True)

    df = df.copy()

    # Agrupación y estadísticas descriptivas
    df = (df[['Mode_of_Shipment', 'Customer_rating']]
            .groupby('Mode_of_Shipment')
            .describe())
    df.columns = df.columns.droplevel()
    df = df[['mean', 'min', 'max']]
    plt.barh(
        y=df.index.values,
        width=df["max"].values - 1,
        left=df["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )

    # Definir colores condicionales según promedio
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange"
        for value in df["mean"].values
    ]

    # Superponer barras para los valores promedio
    plt.barh(
        y=df.index.values,
        width=df["mean"].values - 1,
        left=df["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0,
    )
    plt.title('Average customer rating')
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible('gray')
    plt.gca().spines['bottom'].set_visible('gray')

    # Guardar la figura
    plt.savefig(os.path.join(ruta, 'average_customer_rating'))
    plt.close()

def visual_Weight_in_gms(df,ruta):
    df = df.copy()
    plt.figure()
    df['Weight_in_gms'].plot.hist(
        title='Shipped Weigth Distribution',
        color='tab:orange',
        edgecolor='white',
    )
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    # Guardar la figura
    plt.tight_layout()
    plt.savefig(os.path.join(ruta, 'weight_distribution.png'))
    plt.close() 

def crear_dashboard_html(ruta):
    html = """<!DOCTYPE html>
<html>
<body>
    <h1>Shipping Dashboard Example</h1>
    <div style="width:45%;float:left">
        <img src="shipping_per_warehouse.png" alt="Fig 1">
        <img src="mode_of_shipment.png" alt="Fig 2">
    </div>
    <div style="width:45%;float:left">
        <img src="average_customer_rating.png" alt="Fig 3">
        <img src="weight_distribution.png" alt="Fig 4">
    </div>
</body>
</html>
"""
    # Ruta completa del archivo
    ruta_archivo = os.path.join(ruta, 'index.html')

    # Guardar el archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(html)



def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    ruta = "files/docs"
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    df=load_data()
    visual_warehouse(df,ruta)
    visual_mode_shipment(df,ruta)
    visual_customer_rating(df,ruta)
    visual_Weight_in_gms(df,ruta)
    crear_dashboard_html(ruta)

pregunta_01()
