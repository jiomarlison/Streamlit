import datetime
import numpy as np
datas = np.arange(np.datetime64('1900-01-01'), np.datetime64(f'{datetime.date.today()}'))

lista_datas = []
anos, meses, dias = [], [], []

for x in datas:
    lista_datas.append(str(x).split("-"))
for x in range(len(lista_datas)):
    anos.append(lista_datas[x][0])
    meses.append(lista_datas[x][1])
    dias.append(lista_datas[x][2])
anos = sorted(list(dict.fromkeys(anos)), reverse=True)
meses = sorted(list(dict.fromkeys(meses)))
dias = sorted(list(dict.fromkeys(dias)))
print(dias)
print(meses)
print(anos)
