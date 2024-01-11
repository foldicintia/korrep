"""
Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
·	az épület építésének az éve, pl.1949
Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.
A megoldás mintája:
III/A, B:
            	Az épületek száma: 8
III/C:
            	Az 555 lábnál magasabb épületek száma: 2.
III/D:
            	A legöregebb épület országa: Lengyelország.            	
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a epulet.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
C.	Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)
"""

import epuletek
epuletek_lista=epuletek.fajlbeolvas()

epuletek.epuletek_szama(epuletek_lista)
print("III/A, B:")
print(f"\tAz épületek száma: {len(epuletek_lista)}")

db=epuletek.magas_epuletek_szama(epuletek_lista)
print("III/C:")
print(f"\tA magas épületek száma: {db}")

legoregebb_index=epuletek.legoregebb(epuletek_lista)
print("III/D:")
print(f"\tA legidősebb épület országa: {epuletek_lista[legoregebb_index].orszag}")

legtobbemelet_index=epuletek.legtobb_emelet(epuletek_lista)
print("III/E:")
print(f"\tA legtöbb emeletszámmal rendelkező épület {epuletek_lista[legtobbemelet_index].nev}, {epuletek_lista[legtobbemelet_index].varos}-ban található.")