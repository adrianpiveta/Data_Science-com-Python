from pandas_datareader import data as web
import matplotlib.pyplot as plt
import pandas as pd
COTACAO_CASH3 =  web.DataReader('CASH3.SA', 'yahoo', start='10-01-2022', end="11-02-2022")

print(COTACAO_CASH3)

COTACAO_CASH3["Adj Close"].plot()
plt.show()

df = pd.DataFrame(COTACAO_CASH3)
with pd.ExcelWriter("D:\\GitHub\\Utilitarios\\planilha2.xlsx") as writer:
    df.to_excel(writer)
