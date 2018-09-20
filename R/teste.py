import numpy as np
#import matplotlib.pyplot as plt
#matplotlib.style.use('ggplot')

from matplotlib import pyplot as plt
plt.style.use('ggplot')

# Using numpy we can use the function loadtxt to load your CSV file.
# We ignore the first line with the column names and use ',' as a delimiter.
data = np.loadtxt('/home/maisa/UTFPR/Tcc/Arquivos gerados/treino_total.csv', delimiter=',', skiprows=1)

# You can access the columns directly, but let us just define them for clarity.
# This uses array slicing/indexing to cut the correct columns into variables.
classe = data[:,0]

mediaxacc = data[:,1]
mediayacc = data[:,2]
mediazacc = data[:,3]

medianaxacc = data[:,4]
medianayacc = data[:,5]
medianazacc = data[:,6]

modaxacc = data[:,7]
modayacc = data[:,8]
modazacc = data[:,9]

minxacc = data[:,10]
minyacc = data[:,11]
minzacc = data[:,12]

maxxacc = data[:,13]
maxyacc = data[:,14]
maxzacc = data[:,15]

# With matplotlib we define a new subplot with a certain size (10x10)
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(classe, mediaxacc, label='mediaxacc')
ax.plot(classe, mediayacc, label='mediayacc')
ax.plot(classe, mediazacc, label='mediazacc')

ax.plot(classe, medianaxacc, label='medianaxacc')
ax.plot(classe, medianayacc, label='medianayacc')
ax.plot(classe, medianazacc, label='medianazacc')

ax.plot(classe, modaxacc, label='modaxacc')
ax.plot(classe, modayacc, label='modayacc')
ax.plot(classe, modazacc, label='modazacc')

ax.plot(classe, minxacc, label='minxacc')
ax.plot(classe, minyacc, label='minyacc')
ax.plot(classe, minzacc, label='minzacc')

ax.plot(classe, maxxacc, label='maxxacc')
ax.plot(classe, maxyacc, label='maxyacc')
ax.plot(classe, maxzacc, label='maxzacc')

# Show the legend
plt.legend()
fig.savefig('/home/maisa/UTFPR/Tcc/Arquivos gerados/temp.png', dpi=fig.dpi)
