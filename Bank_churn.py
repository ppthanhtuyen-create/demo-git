import os

os.system("cls")   # Windows
import pandas as pd
df=pd.read_csv("Bank_Churn.csv")
print(df.head())