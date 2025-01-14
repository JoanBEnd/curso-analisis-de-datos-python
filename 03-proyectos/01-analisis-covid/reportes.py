import matplotlib.pyplot as plt
import seaborn as sns
import extraccion
from matplotlib.colors import LinearSegmentedColormap

def Reporte_por_año_mes(df_covid, variable_anio):
    
    df_filtrado = extraccion.extraccion_fallecidos_por_anio(df_covid, variable_anio)
    
    if df_filtrado is not None:
        num_años = df_filtrado["Año"].nunique()
        palette = sns.color_palette("rocket_r", num_años)

        sns.set_theme(style="whitegrid", palette="muted")

        plt.figure(figsize=(15, 5))
        ax = sns.lineplot(x=df_filtrado["Mes"], 
                          y=df_filtrado["Fallecidos"], 
                          hue=df_filtrado["Año"],  
                          palette=palette ,
                          linewidth=2.5
                        )

        plt.title(f"Tendencia de Covid durante {"Todos los años" if variable_anio == "Todos" else "el " + str(variable_anio)} ",
                  fontsize=18,
                  fontweight="bold",
                  loc="center"  # Centrar el título
                  )
        
        sns.despine(left=True, bottom=True)
        plt.show()
         
        return "El reporte se generó correctamente." 
    else:
        return f"¡Lo sentimos! No pudimos encontrar coincidencias. Asegúrate de que la información esté correcta o prueba con una nueva búsqueda"
    

def Reporte_demografico(df_covid, variable_anio):
    
    df_covid_filtro = extraccion.extraccion_demografico(df_covid, variable_anio)
    
    if df_covid_filtro is not None:


        fig, ax = plt.subplots(figsize=(12, 6))                
        ax = sns.histplot(data=df_covid_filtro, 
                          x="EDAD_DECLARADA", 
                          bins=10,
                          color="steelblue",  # Color profesional
                          kde=True,  # Le agrega curva para una mejor visualización
                          line_kws={"linewidth": 2}  # ajusta el grosor de la curva
                          )

        plt.title(f"Demografía de Fallecidos por Covid {"todos los años" if variable_anio == "Todos" else "durante el " + str(variable_anio)} ")
        plt.xlabel("Edad Fallecidos", fontsize=12)
        plt.ylabel("Total Fallecidos", fontsize=12)
        

        sns.despine(left=True, bottom=True)
        
        plt.show()
        return  "El reporte se generó correctamente." 
    else:
        return f"¡Lo sentimos! No pudimos encontrar coincidencias. Asegúrate de que la información esté correcta o prueba con una nueva búsqueda"

def Reporte_by_genero(df_covid, variable_anio):
                              

    df_covid_filtro = extraccion.extraccion_genero(df_covid, variable_anio)
    if df_covid_filtro is not None:

        
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.set_theme(style="whitegrid", palette="pastel")
        
        colores = sns.color_palette("coolwarm", len(df_covid_filtro["Sexo"]))


        ax.pie(x=df_covid_filtro["Total"], 
            labels=df_covid_filtro["Sexo"], 
            autopct='%1.1f%%',
            startangle=90,  # Inicia el gráfico en el ángulo de las 12
            colors=colores,  # Aplicar la paleta de colores personalizada
            wedgeprops={"edgecolor": "gray", "linewidth": 1.5} # Bordes de las porciones
            )
        

        plt.title(f"Reporte Fallecidos por Género {"Todos los Años" if variable_anio == "Todos" else "durante el " + str(variable_anio)} ")
        plt.show()


        return "El reporte se generó correctamente"
    else:
        return f"¡Lo sentimos! No pudimos encontrar coincidencias. Asegúrate de que la información esté correcta o prueba con una nueva búsqueda"

def Reporte_mapa_calor_fallecidos_por_departamento(df_covid, variable_anio):
                              

    df_covid_filtro = extraccion.extraccion_fallecidos_por_departamento_mapa(df_covid, variable_anio)
    
    if df_covid_filtro is not None:
        colors = ["#A8E6A3", "#FFFACD", "#F4A2A1"]  # Verde pastel, amarillo pastel, rojo pastel
        cmap_semaforo_pastel = LinearSegmentedColormap.from_list("semaforo_pastel", colors)

        fig, ax = plt.subplots(figsize=(15, 8))
        ax= sns.heatmap(data = df_covid_filtro,
                    annot=True,
                    fmt=".0f",
                    cmap=cmap_semaforo_pastel,
                    cbar_kws={"label": "Total Fallecidos"},
                    linewidths=0.7
                    )
        
        ax.set_title(f"Mapa de Calor por Departamento - {"Todos los años" if variable_anio == "Todos" else "Durante el " + str(variable_anio)} ", fontsize=16, fontweight="bold")
        plt.show()
        return "El reporte se generó correctamente"
    else:
        return f"¡Lo sentimos! No pudimos encontrar coincidencias. Asegúrate de que la información esté correcta o prueba con una nueva búsqueda"


def Reporte_by_departamento(df_covid, variable_anio):
    
    df_covid_filtro = extraccion.extraccion_fallecidos_por_departamento(df_covid, variable_anio)

    if df_covid_filtro is not None:

        
        fig, ax = plt.subplots(figsize=(14, 8))

        #sns.set_theme(style="whitegrid", palette="pastel")
        
        ax = sns.barplot(data=df_covid_filtro, 
                         y="DEPARTAMENTO", 
                         x="Total", 
                         hue="DEPARTAMENTO",  # Asignamos hue (usamos "DEPARTAMENTO" para seguir la advertencia)
                         dodge=False,         # Para evitar barras separadas
                         palette="viridis",   # Usamos una paleta de colores agradable
                         legend=False)
        ax.set_title(
            f"Total de Fallecidos por Departamento - {variable_anio}", 
            fontsize=16, 
            weight="bold", 
            pad=15
        )
        
        ax.set_xlabel("Total de Fallecidos", fontsize=12, labelpad=10)
        ax.set_ylabel("Departamento", fontsize=12, labelpad=10)

        # Agregaremos los valores encima de las barras
        for container in ax.containers:
            ax.bar_label(container, fmt="%.0f", label_type="edge", padding=3, fontsize=9, color="black")

        sns.despine(left=True, bottom=True)
        plt.show()
        return "El reporte se generó correctamente"
    else:
        return f"¡Lo sentimos! No pudimos encontrar coincidencias. Asegúrate de que la información esté correcta o prueba con una nueva búsqueda"
