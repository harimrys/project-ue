import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_") 
    return df

def change_value(df):

    gender_map = {"F:Females": "Females", "M:Males": "Males", "T:Total": "Total", "F": "Females", "M": "Males", "T": "Total"}
    df["sex"] = df["sex"].map(gender_map)


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

def change_name_country_education(df):
    geo_map = {"AT:Austria" : "Austria", "BA:Bosnia and Herzegovina": "Bosnia and Herzegovina", "BE:Belgium": "Belgium",
               "BG:Bulgaria": "Bulgaria", "CH:Switzerland": "Switzerland", "CY:Cyprus": "Cyprus", "CZ:Czechia": "Czechia",
               "DE:Germany": "Germany", "DK:Denmark": "Denmark", "EE:Estonia": "Estonia", "EL:Greece": "Greece", "ES:Spain": "Spain",
               "FI:Finland": "Finland", "FR:France" :"France", "HR:Croatia": "Croatia", "HU:Hungary": "Hungary", "IE:Ireland": "Ireland",
               "IS:Iceland": "Iceland", "IT:Italy": "Italy", "LT:Lithuania": "Lithuania", "LU:Luxembourg": "Luxembourg", "LV:Latvia": "Latvia",
               "ME:Montenegro": "Montenegro", "MK:North Macedonia": "North Macedonia", "MT:Malta": "Malta", "NL:Netherlands": "Netherlands",
               "NO:Norway": "Norway", "PL:Poland": "Poland", "PT:Portugal": "Portugal", "RO:Romania": "Romania", "RS:Serbia": "Serbia",
               "SE:Sweden": "Sweden", "SI:Slovenia": "Slovenia", "SK:Slovakia": "Slovakia", "TR:Türkiye": "Türkiye", 
               "UK:United Kingdom": "United Kingdom"}
    df["geo"] = df["geo"].map(geo_map)
    return df

def change_name_country_unemployment(df):
    geo_map = {"AT": "Austria", "BE:": "Belgium", "BG": "Bulgaria", "CH": "Switzerland", "CY": "Cyprus", "CZ": "Czechia",
               "DE": "Germany", "DK": "Denmark", "EE": "Estonia", "EL": "Greece", "ES:": "Spain", "FI": "Finland", "FR": "France", 
               "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IS": "Iceland", "IT": "Italy", 
               "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia",
               "ME": "Montenegro", "MK": "North Macedonia", "MT": "Malta", "NL": "Netherlands",
               "NO": "Norway", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "RS": "Serbia",
               "SE": "Sweden", "SI": "Slovenia", "SK": "Slovakia", "TR": "Türkiye", 
               "UK": "United Kingdom"}
    df["geo"] = df["geo"].map(geo_map)
    return df