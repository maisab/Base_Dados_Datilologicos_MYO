import csv
import matplotlib.pyplot as plt
import os

#os.chdir(r"'/home/maisa/UTFPR/Tcc/Arquivos gerados/'")  #path of your csv file

S1=[]
S2=[]
S3=[]
HWS=[]
with open('/home/maisa/UTFPR/Tcc/Arquivos gerados/teste_a.csv','r') as csvFile:
    reader=csv.reader(csvFile,delimiter=',')
    next(reader)

    for row in reader:
        temp=row[0]
        S1.append(temp)
        temp=row[1]
        S2.append(temp)
        temp=row[2]
        S3.append(temp)
        temp=row[3]
        HWS.append(temp)

plt.plot(HWS,S1)
plt.plot(HWS,S2)
plt.plot(HWS,S3)
plt.show()
