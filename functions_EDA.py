import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(url):
    df = pd.read_csv(url)
    return df