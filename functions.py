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