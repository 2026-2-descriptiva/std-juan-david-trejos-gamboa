import os

import pandas as pd

INPUT_FILE = "PRE_04_limpieza/data/ventas.csv"
OUTPUT_FILE = "PRE_04_limpieza/submission/ventas.csv"

def strip_whitespace(series):
    return series.str.strip()

def to_lowercase(series):
    return series.str.lower()

def replace_space_with_underscore(series):
    return series.str.replace(" ", "_")

def clean_column_names(df):
    df.columns = strip_whitespace(df.columns)
    df.columns = to_lowercase(df.columns)
    df.columns = replace_space_with_underscore(df.columns)
    return df


def clean_supplier_column(series):
    series = strip_whitespace(series)
    return series

def main():

    df = pd.read_csv(INPUT_FILE)

    df = clean_column_names(df)
    
    df["supplier"] = clean_supplier_column(df["supplier"])
    
    df.to_csv(OUTPUT_FILE, index=False)

    

if __name__ == "__main__":
    main()
    
    