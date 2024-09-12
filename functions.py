import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

def clean_columns(df):  # Cambia los nombres de las columnas a minúsculas y los espacios por _
    df.columns = df.columns.str.lower().str.replace(" ", "_") 

    df.drop("last_update", axis = 1, inplace = True)
    df.drop("freq", axis = 1, inplace = True)
    df.drop("unit", axis = 1, inplace = True)
    df.drop("obs_flag", axis = 1, inplace = True)
    df.drop("dataflow", axis = 1, inplace = True)
    return df

def column_names_education(df):
    df.rename(columns = {"isced11": "level_education"}, inplace = True)
    df.rename(columns = {"geo": "country"}, inplace = True)
    df.rename(columns = {"time_period": "year"}, inplace = True)
    df.rename(columns = {"obs_value": "value_education"}, inplace = True)
    return df

def column_names_unemployment(df):
    df.rename(columns = {"isced11": "level_education"}, inplace = True)
    df.rename(columns = {"geo": "country"}, inplace = True)
    df.rename(columns = {"time_period": "year"}, inplace = True)
    df.rename(columns = {"obs_value": "value_unemployment"}, inplace = True)
    return df

def change_value(df):  # Iguala los valores de género, edad y nivel educativo en ambas tablas
    gender_map = {"F:Females": "Females", "M:Males": "Males", "T:Total": "Total", "F": "Females", "M": "Males", "T": "Total"}
    df["sex"] = df["sex"].map(gender_map)

    age_map = {"Y15-29": "15-29", "Y15-29:From 15 to 29 years": "15-29"}
    df["age"] = df["age"].map(age_map)

    level_edu_map = {"ED0-2": "ESO", "ED3_4": "BACH-FP", "ED3_4GEN": "BACH", "ED3_4VOC": "FP", "ED5-8": "UNIVERSIDAD", "TOTAL": "TOTAL",
                     "ED0-2:Less than primary, primary and lower secondary education (levels 0-2)": "ESO", 
                     "ED3_4:Upper secondary and post-secondary non-tertiary education (levels 3 and 4)": "BACH-FP",
                     "ED3_4GEN:Upper secondary and post-secondary non-tertiary education (levels 3 and 4) - general": "BACH",
                     "ED3_4VOC:Upper secondary and post-secondary non-tertiary education (levels 3 and 4) - vocational": "FP",
                     "ED5-8:Tertiary education (levels 5-8)": "UNIVERSIDAD"                     
                    }
    df["level_education"] = df["level_education"].map(level_edu_map)

    return df

def change_name_country_education(df):  #Cambia los valores en la columna country para la tabla education
    geo_map = {"AT:Austria" : "Austria", "BA:Bosnia and Herzegovina": "Bosnia and Herzegovina", "BE:Belgium": "Belgium",
               "BG:Bulgaria": "Bulgaria", "CH:Switzerland": "Switzerland", "CY:Cyprus": "Cyprus", "CZ:Czechia": "Czechia",
               "DE:Germany": "Germany", "DK:Denmark": "Denmark", "EE:Estonia": "Estonia", "EL:Greece": "Greece", "ES:Spain": "Spain",
               "FI:Finland": "Finland", "FR:France" :"France", "HR:Croatia": "Croatia", "HU:Hungary": "Hungary", "IE:Ireland": "Ireland",
               "IS:Iceland": "Iceland", "IT:Italy": "Italy", "LT:Lithuania": "Lithuania", "LU:Luxembourg": "Luxembourg", "LV:Latvia": "Latvia",
               "ME:Montenegro": "Montenegro", "MK:North Macedonia": "North Macedonia", "MT:Malta": "Malta", "NL:Netherlands": "Netherlands",
               "NO:Norway": "Norway", "PL:Poland": "Poland", "PT:Portugal": "Portugal", "RO:Romania": "Romania", "RS:Serbia": "Serbia",
               "SE:Sweden": "Sweden", "SI:Slovenia": "Slovenia", "SK:Slovakia": "Slovakia", "TR:Türkiye": "Türkiye", 
               "UK:United Kingdom": "United Kingdom"}
    df["country"] = df["country"].map(geo_map)
    return df

def change_name_country_unemployment(df): #Cambia los valores en la columna country para la tabla unemployment
    geo_map = {"AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "CH": "Switzerland", "CY": "Cyprus", "CZ": "Czechia",
               "DE": "Germany", "DK": "Denmark", "EE": "Estonia", "EL": "Greece", "ES": "Spain", "FI": "Finland", "FR": "France", 
               "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IS": "Iceland", "IT": "Italy", 
               "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia",
               "ME": "Montenegro", "MK": "North Macedonia", "MT": "Malta", "NL": "Netherlands",
               "NO": "Norway", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "RS": "Serbia",
               "SE": "Sweden", "SI": "Slovenia", "SK": "Slovakia", "TR": "Türkiye", 
               "UK": "United Kingdom"}
    df["country"] = df["country"].map(geo_map)
    return df

def drop_duplicates(df):
    df = df.drop_duplicates(subset=["sex", "level_education", "age", "country", "year"])
    return df

def comb_merg(df1, df2):
    df_limpio = pd.merge(df1, df2, on = ["sex", "level_education", "age", "country", "year"], how = "right")
    return df_limpio

def nulos(df):
    df = df.dropna(how = "any")
    return df

def fill_nan(df):
    df.loc[(df["country"] == "Cyprus") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Cyprus") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Estonia") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Estonia") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Estonia") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Estonia") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Croatia") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Croatia") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Ireland") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Ireland") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Lithuania") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Latvia") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Latvia") & (df["level_education"] == "BACH-FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Latvia") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Latvia") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Latvia") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Poland") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Slovenia") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Slovenia") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Slovenia") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Slovakia") & (df["level_education"] == "ESO"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Slovakia") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Slovakia") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Iceland") & (df["level_education"] == "BACH-FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Iceland") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Iceland") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Iceland") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Norway") & (df["level_education"] == "BACH-FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Norway") & (df["level_education"] == "BACH"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Norway") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Norway") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Bulgaria") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    df.loc[(df["country"] == "Bulgaria") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Denmark") & (df["level_education"] == "FP"), "value_unemployment"] = df["value_unemployment"].ffill()
    
    df.loc[(df["country"] == "Finland") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Hungary") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    df.loc[(df["country"] == "Romania") & (df["level_education"] == "UNIVERSIDAD"), "value_unemployment"] = df["value_unemployment"].ffill()

    return df

def drop_rows(df):

    df = df[df["country"] != "Bosnia and Herzegovina"]
    df = df[df["country"] != "Luxembourg"]
    df = df[df["country"] != "Montenegro"]
    df = df[df["country"] != "Malta"]

    df = df[df["level_education"] != "TOTAL"]

    return df

def create_csv(df):
    df.to_csv('df_limpio.csv', index=False)
