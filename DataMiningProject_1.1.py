#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


f=open('C:\Data\Eleonore\GrandEst\GrandEst.csv',newline = '')
reader=csv.reader(f, delimiter = ';')
liste=[]
for row in reader:
    liste.append(row)
print(liste[0])


# In[57]:


len(liste),len(liste[0])


# In[122]:


f1=open('C:\Data\Eleonore\GrandEst\QueLesBonnesColonnes.csv', 'w',newline = '')
writer1=csv.writer(f1, delimiter = ';')
#with open('eggs.csv', 'w', newline='') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',
                           # quotechar='|', quoting=csv.QUOTE_MINIMAL)
   # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
EnsColAGarder=[0,6,10,12,15,16,17,18,22,23,24,25,26,29,31,32,33,34,35,36,38,39,44,45,47,48,49,58,59,60,66,69,70,71,76,77,79,80,83,85,95,96]
for r in range (0,len(liste)):
    writer1.writerow([liste[r][i] for i in EnsColAGarder])
f.close()
f1.close()


# In[125]:


for i in EnsColAGarder : 
    print(liste[0][i])


# In[5]:


AGER20 = ['mineur','jeune','adulte','senior']
ANARR =['0','1','2','3','4','5','6','7','8','9','Z']
ANEMR = ['00','01','02','03','04','05','06','07','09','99','Z']
ASCEN = ['1','2','Z']
BAIN = ['1','2','X','Z']
BATI = ['1','2','3','4','X','Z']
CATL = ['1','2','3','4','Z']
CHOS = ['1','2','X','Z']
CLIM = ['1','2','X','Z'] 
CMBL = ['1','2','3','4','5','6','X','Z']
COUPLE = ['1','2']
CS1 = ['1','2','3','4','5','6','7','8']
CUIS = ['1','2','X','Z']
DEROU = ['0','1','2','3','U','X','Z']
DIPL_15 = ['A','B','C','D','Z']
EAU=['1','2','3','X','Z']
EGOUL = ['1','2','3','4','X','Z']
ELEC = ['1','2','X','Z']
EMPL = ['11','12','13','14','15','16','21','22','23','ZZ']
ETUD = ['1','2']
GARL = ['1','2','Z']
ILTUU = ['1','2','3','4','5','Z']
IMMI = ['1','2']
INAT = ['11','12','21']
INFAM = ['0','1','2','Z']
INPER = ['Y','Z']
MOCO = ['11','12','21','22','23','31','32','40']
MODV = ['11','12','20','31','32','33','40','50','60','70']
NA38 = ['AZ','BZ','CA','CB','CC','CD','CE','CF','CG','CH','CI','CJ','CK','CL','CM','DZ','EZ','FZ','GZ','HZ','IZ','JA','JB','JC','KZ','LZ','MA','MB','MC','NZ','OZ','PZ','QA','QB','RZ','SZ','TZ','UZ','ZZ']
NATC = ['0','1','2','3','4','5','6','7']
NATNC = ['1','2','3','4','5','6','7','Z']
NBPI = ['01','02','03','04','05','06','09','10','11','12','13','14','15','16','17','18','19','20','ZZ']
NPERR = ['1','2','3','4','5','6','Z']
RECH = ['0','1','2','9','Z']
SANI = ['0','1','2','X','Z']
SEXE= ['1','2']
SFM = ['11','12','21','22','30','31','32','33','34','40','51','52','53','54','61','62','70','ZZ']
STOCD = ['00','10','21','22','23','30','ZZ']
TACT = ['11','12','21','22','23','24','25']
VOIT = ['0','1','2','3','X','Z']
WC = ['1','2','X','Z']
Valeurs = AGER20+ANARR+ANEMR+ASCEN+BAIN+BATI+CATL+CHOS+CLIM+CMBL+COUPLE+CS1+CUIS+DEROU+DIPL_15+EAU+EGOUL+ELEC+EMPL+ETUD+GARL+ILTUU+IMMI+INAT+INFAM+INPER+MOCO+MODV+NA38+NATC+NATNC+NBPI+NPERR+RECH+SANI+SEXE+SFM+STOCD+TACT+VOIT+WC
TailleGroupe= [len(AGER20),len(ANARR),len(ANEMR),len(ASCEN),len(BAIN),len(BATI),len(CATL),len(CHOS),len(CLIM),len(CMBL),len(COUPLE),len(CS1),len(CUIS),len(DEROU),len(DIPL_15),len(EAU),len(EGOUL),len(ELEC),len(EMPL),len(ETUD),len(GARL),len(ILTUU),len(IMMI),len(INAT),len(INFAM),len(INPER),len(MOCO),len(MODV),len(NA38),len(NATC),len(NATNC),len(NBPI),len(NPERR),len(RECH),len(SANI),len(SEXE),len(SFM),len(STOCD),len(TACT),len(VOIT),len(WC)]


# In[ ]:





# In[7]:


BDD=open('C:\Data\Eleonore\GrandEst\QueLesBonnesColonnes.csv',newline = '')
readerBDD=csv.reader(BDD, delimiter = ';')
listeBDD=[]
for row in readerBDD : 
    listeBDD.append(row)
listef=[[0]*len(Valeurs)]*len(listeBDD)
    #for r in range (0,len(liste)):
    #writer1.writerow([liste[r][i] for i in EnsColAGarder])


# In[34]:


print(len(Valeurs)) 
print(len(listeBDD))
print(listeBDD[2][1])
print(TailleGroupe)


# In[38]:


TailleGroupe[3]


# In[ ]:


for i in range (1,len(listeBDD)):
    if int(listeBDD[i][1])<=18 :
        (listef[i][0],listef[i][1],listef[i][2],listef[i][3])=(1,0,0,0)
    elif int(listeBDD[i][1])>18 and int(listeBDD[i][1])<=35 :
        (listef[i][0],listef[i][1],listef[i][2],listef[i][3])=(0,1,0,0)
    elif int(listeBDD[i][1])>35 and int(listeBDD[i][1])<=60 :
        (listef[i][0],listef[i][1],listef[i][2],listef[i][3])=(0,0,1,0)
    else :
        (listef[i][0],listef[i][1],listef[i][2],listef[i][3])=(0,0,0,1)


# In[ ]:


for ligne in range(1,10):
    colonneDansValeursDebut = 0
    for colonne in range(2,len(listeBDD[1])):
        numerogroupe=colonne-1
        colonneDansValeursDebut = colonneDansValeursDebut+TailleGroupe[numerogroupe-1]
        colonneDansValeursFin = colonneDansValeursDebut+TailleGroupe[numerogroupe]
        listeComparaison = Valeurs[colonneDansValeursDebut:colonneDansValeursFin]
        print(numerogroupe,colonneDansValeursDebut,colonneDansValeursFin,listeComparaison)
        for i in range(0,len(listeComparaison)):
            if listeBDD[ligne][colonne] == listeComparaison[i]:
                listef[ligne][colonneDansValeursDebut+i] = 1
print(listef) 
        


# In[ ]:


for colonne in range(2,len(listeBDD[1])):
    numerogroupe=colonne-1
    colonneDansValeursDebut = colonneDansValeursDebut+TailleGroupe[numerogroupe-1]
    colonneDansValeursFin = colonneDansValeursDebut+TailleGroupe[numerogroupe]
    listeComparaison = Valeurs[colonneDansValeursDebut:colonneDansValeursFin]
    print(numerogroupe,colonneDansValeursDebut,colonneDansValeursFin,listeComparaison)
    for i in range(0,len(listeComparaison)):
        if listeBDD[ligne][colonne] == listeComparaison[i]:
                listef[ligne][colonneDansValeursDebut+i] = 1


# In[25]:


ligne=1
colonne = 2
numerogroupe=1
colonneDansValeursDebut = 4
colonneDansValeursFin = colonneDansValeursDebut+TailleGroupe[numerogroupe]
listeComparaison = Valeurs[colonneDansValeursDebut:colonneDansValeursFin]
while numerogroupe<len(TailleGroupe):    
print(listeComparaison)
for i in range(0,len(listeComparaison)):
if listeBDD[ligne][colonne] == listeComparaison[i]:
listef[ligne][colonneDansValeursDebut+i] = 1
    numerogroupe=numerogroupe+1
    print(numerogroupe)
    colonneDansValeursDebut = colonneDansValeursFin+1
    colonneDansValeursFin = colonneDansValeursDebut+TailleGroupe[numerogroupe]-1
    listeComparaison = Valeurs[colonneDansValeursDebut:colonneDansValeursFin]
print(listef) 


# In[26]:


i=0
for colone in Valeurs:
    while i<3:
        i=i+1
        print(i)


# In[ ]:


ff = open('C:\Data\Eleonore\GrandEst\BDDTransformee.csv', 'w',newline = '')
writerf=csv.writer(ff, delimiter = ';')


# In[96]:


writer1.writerow([1])
#writer1.writerow( ['Spam'] * 5 + ['Baked Beans'])


# In[ ]:


f2=open('C:\Data\Eleonore\GrandEst\GrandEst.csv',newline = '')
reader=csv.DictReader(f2, delimiter=';')
for row in reader:
    print(row['REGION'][1])


# In[ ]:




