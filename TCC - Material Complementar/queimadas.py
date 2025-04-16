import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# In[24]:
###############################################################################
### Trabalhando com a base de dados de Focos de Queimadas - INPE
### Fonte: https://terrabrasilis.dpi.inpe.br/queimadas/portal/
###############################################################################

# Importando a base de dados
queimadas = pd.read_excel("queimadas.xlsx")

# Transformar o data frame em serie de tempo (Selecionar todos os comandos)
queimad = pd.Series(queimadas['focos'].values, 
                index=pd.date_range(start='1999-01-01', 
                                    periods=len(queimadas), freq='M'))

# In[25]: Plotando o grafico (Selecionar todos os comandos)
plt.figure(figsize=(12, 6))
plt.plot(queimad)
plt.title("Numero de Focos de Queimadas - Programa Queimadas - INPE")
plt.xlabel("Mensal - jan/1999 a Set/2024")
plt.ylabel("Numero de Queimadas")
plt.grid(True)
plt.show()

# In[25.1] Grafico das queimadas por mes
import statsmodels.api as sm

sm.graphics.tsa.month_plot(queimad)

plt.show()