import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/maisa/UTFPR/Tcc/Arquivos gerados/teste_a.csv')
#frame.plot() # Vertex is the x-axis
#ax = frame.plot()
#fig = ax.get_figure()
#fig.savefig('/home/maisa/UTFPR/Tcc/Arquivos gerados/temp.png', dpi=fig.dpi)

#import pandas
#df = pd.DataFrame({'Values': np(10), 'Categories': list('12345678910')}, index=range(10))
#df.set_index('classes', append=True).unstack().interpolate().plot(subplots=True)

#groups = df.groupby('classe')

#fig, ax = plt.subplots()
#for name, group in groups:
#    ax.plot(group['classe'], group['mediaxacc','mediayacc'], label=name)
#ax.legend(loc='media_a')

x = df['classe']
y1 = df['mediaxacc']
y2 = df['mediayacc']
y3 = df['mediazacc']
y4 = df['medianaxacc']
y5 = df['medianayacc']
y6 = df['medianazacc']


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)

plt.show()
