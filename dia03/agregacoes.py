#%%
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 1000)

# %%
df_produto = pd.read_csv("../data/produto.csv")
df_produto

#%%
df_produto["vlPreco"].describe()

#%%
df_produto["vlPrecoInflacao"] = (df_produto["vlPreco"] * 1.09).round(2) 
df_produto.describe()

#%%
df_produto["descItemPrimeiro"] = df_produto["descItem"].apply(lambda x: x.lower().split(" ")[0]) 
df_produto[["descItem", "descItemPrimeiro"]].describe()

#%%
freq_itens = pd.value_counts(df_produto["descItemPrimeiro"])

plt.bar(freq_itens.index[:5], freq_itens.values[:5])
plt.grid(True)
plt.title("Top 5 produtos")
plt.xlabel("Produto")
plt.ylabel("Frequência")

#%%
df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco", "vlPrecoInflacao"]].mean()

#%%
df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco", "vlPrecoInflacao"]].describe()

#%%
import random

def fodase(x):
    return random.choice(x.values)    

(df_produto.groupby(by=["descItemPrimeiro"])[["vlPreco", "vlPrecoInflacao"]]
            .agg(["mean", "min", "max", fodase]))
