import pandas as pd

df = pd.read_csv("data.csv") 
print(df.to_string())

df=  pd.read_csv("data.csv")
new_df = df.dropna() 
print(new_df.to_string()) 

df = pd.read_csv("data.csv")
df.dropna(inplace=True) 
print(df.to_string()) 

df = pd.read_csv("data.csv")
df.fillna(300, inplace=True)
print(df.to_string()) 

df_novo = pd.read_csv("data.csv")
df_novo.fillna({"Calories": 350}, inplace=True)
print(df_novo.to_string())
print(df_novo.isna().sum())

df = pd.read_csv("data.csv")
df.fillna({"Calories": 300}, inplace=True) 
print(df.to_string())    

df = pd.read_csv("data.csv")
df.isna()   
print(df.isna().sum())

df_problema = pd.read_csv("data.csv")
print(df_problema.isna().sum())
df_problema.fillna({"Calories": 300}, inplace=True)
print(df_problema.to_string())
print(df_problema.isna().sum())

df_final = pd.read_csv("data.csv")
print(df_final.shape[0])
print(df_final.shape[1])
print(df_final.columns.tolist())
print(df_final.isna().sum())

df_final.fillna({"Calories": 300}, inplace=True)
print(df_final.isna().sum())
print(df_final.to_string())