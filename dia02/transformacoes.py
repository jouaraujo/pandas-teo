#%%

import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/produto.csv")
df

#%%
df.info()

#%%

df["precoAjustado"] = (df["vlPreco"] * 1.09).round(2)
df

#%%
df["txAjuste(%)"] = (100 * (df["precoAjustado"] / df["vlPreco"] - 1)).round(2)
df

#%%
# Maneira 1
df = df.drop(columns=["txAjuste"])
df

# %%
# Maneira 2
del df["txAjuste(%)"]
df 

#%%
df["logTxAjuste"] = np.log(df["txAjuste(%)"])
df

#%%
df["expTxAjuste"] = np.exp(df["txAjuste(%)"])
df

#%%

def teozinho(x):
    total = 1
    for i in range(2, int(x)+1):
        total *= i
    return total

#%%
df["precoAjustado"].apply(teozinho)
