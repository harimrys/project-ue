import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_") 
    return df

def change_value(df):

    gender_map = {"F:Females": "Females", "M:Males": "Males", "T:Total": "Total"}
    df["sex"] = df["sex"].map(gender_map)

    percentage_map = {"PC:Percentage": "Percentage"}
    df["unit"] = df["unit"].map(percentage_map)

    freq_map = {"A:Annual": "Anual"}
    df["freq"] = df["freq"].map(freq_map)

    return df

def drop_columns_education(df): # Elimina las columnas de la tabla educación que no son útiles para el estudio
    df.drop("last_update", axis = 1, inplace = True)
    df.drop("freq", axis = 1, inplace = True)
    df.drop("unit", axis = 1, inplace = True)
    df.drop("obs_flag", axis = 1, inplace = True)
    df.drop("dataflow", axis = 1, inplace = True)

    return df

def drop_columns_unemployment(df): # Elimina las columnas de la tabla desempleo que no son útiles para el estudio
    df.drop("last_update", axis = 1, inplace = True)
    df.drop("freq", axis = 1, inplace = True)
    df.drop("unit", axis = 1, inplace = True)
    df.drop("obs_flag", axis = 1, inplace = True)
    df.drop("dataflow", axis = 1, inplace = True)


    return df