import pdfplumber
import pandas as pd
from collections import defaultdict

def flatten(t):
    return [item for sublist in t for item in sublist]

def clean_columns(columns):
    return [col.replace('\n', ' ') for col in columns]

def extract_tables(pages):
    dfs_by_columns = defaultdict(pd.DataFrame)
    tables = flatten(page.extract_tables() for page in pages)
    for table in tables:
        columns = table[0]
        df = pd.DataFrame(table[1:], columns=clean_columns(columns))
        df = df.dropna(thresh=3)
        key = str(columns)
        dfs_by_columns[key] = pd.concat([dfs_by_columns[key], df])

    return dfs_by_columns.values()

pdf_path = "pdfs/Indiana.pdf"
pdf = pdfplumber.open(pdf_path)
dfs = extract_tables(pdf.pages)
for i, df in enumerate(dfs):
    csv_path = f'{pdf_path.split(".")[0]}_{i}.csv'
    df.to_csv(csv_path)