import datetime
import numpy as np
datas = np.arange(np.datetime64('1900'), np.datetime64(f'{datetime.date.today().year + 1}'))
anos = [int(str(anos)) for (anos) in datas]

