import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(url):
    df = pd.read_csv(url)
    return df


def nivel_educ_gene(df):
    # Generar el gráfico de barras agrupadas por nivel de educación y género
    df_filtrado = df[df["sex"] != 'Total']
    grupo_genero_educacion = df_filtrado.groupby(["level_education", "sex"])["value_education"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x = "level_education", y = "value_education", hue = "sex", data = grupo_genero_educacion, palette = "rocket")

    plt.title('Tasa de Educación por Nivel de Educación y Género')
    plt.ylabel('Tasa de Educación (%)')
    plt.xlabel('Nivel de Educación')

    # Mostrar el gráfico
    plt.show()

def pais_genero_educ(df):
    df_filtrado = df[df["sex"] != 'Total']
    grupo_pais_genero_educacion = df_filtrado.groupby(["country", "level_education"])["value_education"].mean().reset_index()

    # Crear el gráfico de barras agrupadas por país, género y nivel de educación
    plt.figure(figsize = (12, 8))
    sns.barplot(x = "country", y = "value_education", hue = "level_education", data = grupo_pais_genero_educacion, palette = "rocket", errorbar = None)

    plt.title('Tasa de Educación por Nivel de Educación y País')
    plt.ylabel('Tasa de Educación (%)')
    plt.xlabel('País')

    plt.xticks(rotation = 70)  # Rotar las etiquetas del eje x para mejor visibilidad
    plt.tight_layout()
    plt.show()

def ind_educ_genero(df):
    df_total_sex = df[df["sex"] != "Total"]

    df_grouped = df_total_sex.groupby(["country", "sex"])["indice_educativo"].mean().reset_index()
    # Crear el gráfico de barras agrupadas por país y sexo
    plt.figure(figsize=(14, 8))
    sns.barplot(x ="country", y ="indice_educativo", hue ="sex", data=df_grouped, palette = "rocket")

    plt.title('Índice Educativo por País y Sexo')
    plt.ylabel('Índice Educativo')
    plt.xlabel('País')

    # Rotar las etiquetas del eje X para mayor visibilidad
    plt.xticks(rotation = 90)

    plt.tight_layout()
    plt.show()

def porcen_desempl_genero(df):
    df_filtrado = df[df["sex"] != 'Total']
    grupo_genero_desempleo_year = df_filtrado.groupby(["sex", "year"])["value_unemployment"].mean().reset_index()

    # Crear el gráfico de barras para el porcentaje de desempleo por género
    plt.figure(figsize = (8, 5))
    sns.barplot(x = "year", y = "value_unemployment", hue = "sex", data = grupo_genero_desempleo_year, palette = "rocket")

    plt.title('Tasa de Desempleo Promedio por Género y Año')
    plt.ylabel('Tasa de Desempleo (%)')
    plt.xlabel('Género')

    plt.show()

def desemp_gener_pais(df):
    df_filtrado = df[df["sex"] != 'Total']
    grupo_genero_desempleo_country = df_filtrado.groupby(["sex", "country"])["value_unemployment"].mean().reset_index()

    # Crear el gráfico de barras para el porcentaje de desempleo por género
    plt.figure(figsize = (8, 5))
    sns.barplot(x = "country", y = "value_unemployment", hue = "sex", data = grupo_genero_desempleo_country, palette = "rocket")

    plt.title('Tasa de Desempleo Promedio por Género y Pais')
    plt.ylabel('Tasa de Desempleo (%)')
    plt.xlabel('Género')
    plt.xticks(rotation = 80)
    plt.tight_layout()

    plt.show()

def educa_desempl_genero(df):
    df_total_sex = df[df["sex"] != "Total"]
    df_grouped = df_total_sex.groupby(["country", "sex"]).agg({
        "indice_educativo": "mean",
        "value_unemployment": "mean"
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Graficar el índice educativo con barras
    sns.barplot(x = "country", y = "indice_educativo", hue = "sex", data = df_grouped, palette = "rocket", ax = ax1, alpha = 0.6)

    # Crear un segundo eje Y para la tasa de desempleo
    ax2 = ax1.twinx()
    sns.lineplot(x = "country", y = "value_unemployment", hue = "sex", data = df_grouped, ax = ax2, palette = "rocket", marker = "o")

    # Añadir títulos y etiquetas
    ax1.set_title('Índice Educativo y Tasa de Desempleo por Sexo')
    ax1.set_xlabel('País')
    ax1.set_ylabel('Índice Educativo')
    ax2.set_ylabel('Tasa de Desempleo (%)')

    # Rotar las etiquetas del eje X para mayor visibilidad
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation = 90)

    ax1.legend(loc = "upper left", bbox_to_anchor = (1, 1))
    ax2.legend(loc = "upper left", bbox_to_anchor = (1, 0.9))

    plt.tight_layout()
    plt.show()

def ind_educativo_año(df):
    df_grouped_year = df.groupby("year").agg({
    "indice_educativo": "mean",
    "value_unemployment": "mean"
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Graficar el índice educativo con una línea
    sns.lineplot(x = "year", y = "indice_educativo", data = df_grouped_year, ax = ax1, color = "purple", marker = "o", label = "Índice Educativo")
    ax1.set_ylabel("Índice Educativo", color = "purple")
    ax1.tick_params(axis = "y", labelcolor = "purple")

    # Crear un segundo eje Y para la tasa de desempleo
    ax2 = ax1.twinx()
    sns.lineplot(x = "year", y = "value_unemployment", data = df_grouped_year, ax = ax2, color = "coral", marker = "o", label = "Tasa de Desempleo")
    ax2.set_ylabel("Tasa de Desempleo (%)", color = "coral")
    ax2.tick_params(axis = "y", labelcolor = "coral")

    plt.title('Índice Educativo y Tasa de Desempleo por Año')
    ax1.set_xlabel('Año')

    # Ajustar la leyenda
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc = "upper left")

    plt.tight_layout()
    plt.show()

def educacion_vs_desempleo(df):
    df_grouped_country = df.groupby("country").agg({
    "indice_educativo": "mean",
    "value_unemployment": "mean"
    }).reset_index()

    plt.figure(figsize=(14, 8))

    # Graficar el índice educativo en el eje X y la tasa de desempleo en el eje Y
    sns.scatterplot(x="indice_educativo", y="value_unemployment", data=df_grouped_country, hue="country", palette="tab20", s=100)

    plt.title('Índice Educativo vs. Tasa de Desempleo por País')
    plt.xlabel('Índice Educativo')
    plt.ylabel('Tasa de Desempleo (%)')

    # Ajustar la leyenda
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

    plt.tight_layout()
    plt.show()