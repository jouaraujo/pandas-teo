#%%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/produto.csv")
df

#%%
df = df.rename(columns={"vlPreco": "vlPrecoReal"})
df

#%%
filtro = df["vlPrecoReal"] > 10
df[filtro]

#%%
queijos_premium = ["queijo brie", "queijo coalho", "ricota"]
filtros_queijos = df["descItem"].isin(queijos_premium)
df[filtros_queijos]

#%%
df["vlPrecoInflacao"] = (df["vlPrecoReal"] * 1.09).round(2)
df

#%%
df["vlPrecoInflacaoLog"] = np.log(df["vlPrecoInflacao"])
df