import pdfplumber
import pandas as pd

pdf = pdfplumber.open("pdfs/Indiana.pdf")
page = pdf.pages[0]
table = page.extract_table()

columns = [col.replace('\n', ' ') for col in table[0]]
df = pd.DataFrame(table[1:], columns=columns)
print(df)