# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:22:57 2021

@author: Bartosz Terka
"""

import RZUTY as rz, FUNKCJE as fun
x=[]
y=[]
#poczatek:[x,y,predkosc_x,predkosc_y,typ]
#typy rzutow: 1-poziomy 2-pionowy 3-spadajacy w dol 4-ukosny
poczatek=fun.losuj_poczatek()
poczatek=fun.wybierz_rzut(poczatek) 
if poczatek[4]==1:
    rz.rzut_poziomy(x,y,poczatek)
elif poczatek[4]==2:
    rz.rzut_pionowy(x,y,poczatek)
elif poczatek[4]==3:
    rz.rzut_spadajacy(x,y,poczatek)
elif poczatek[4]==4:
    rz.rzut_ukosny(x,y,poczatek)




