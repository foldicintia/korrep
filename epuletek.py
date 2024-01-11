from Epulet import Epulet

def fajlbeolvas():
    epuletek_lista=[]
    fajl=open("epulet.txt","r",encoding="utf-8")
    fajl.readline()
    fajl_lista=fajl.readlines()
    fajl.close()

    for i in range(0,len(fajl_lista),1):
        aktsor=fajl_lista[i].replace(",",".").strip().split("$")
        epuletem=Epulet(aktsor[0],aktsor[1],aktsor[2],aktsor[3],aktsor[4],aktsor[5])
        # print(epuletem.nev,epuletem.varos,epuletem.orszag,epuletem.em_szam,epuletem.epult)
        epuletek_lista.append(epuletem)
    return epuletek_lista

def epuletek_szama(lista):

    return len(lista)

def magas_epuletek_szama(lista):
    gyujto = 0
    meter:int= 555/3.280839895
    for i in range(0,len(lista),1):
        epulet_magassag=float(lista[i].magassag.replace(",", "."))
        if epulet_magassag > meter:
            gyujto+=1
    return gyujto

  
def legoregebb(lista):
    max_index = 0 
    for i in range(0,len(lista),1):
        #osszehasonlitom az akt elemet es az eddigi maxot
        if lista[i].epult < lista[max_index].epult:
            max_index=i

    return max_index


# a legtobb emelettel rendelkezo epulet neve es varosa

def legtobb_emelet(lista):
    max_index = 0
    for i in range(0,len(lista),1):
        if lista[i].em_szam > lista[max_index].em_szam:
            max_index=i
    
    return max_index


   