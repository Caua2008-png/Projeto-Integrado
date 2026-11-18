import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_raca = pd.read_csv('ibge_trabalho_raca_2012_2022.csv',delimiter=";")

fig, ax = plt.subplots(figsize=(10, 10))

sns.barplot(
    data=df_raca,
    x="Cor_Raca",
    y="Taxa_Desocupacao_Pct",
    hue="Ano",
    palette="Set2",
    errorbar=None,
    ax=ax,
)
plt.tight_layout()
plt.show()
