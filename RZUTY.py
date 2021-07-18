# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:57:38 2021

@author:Bartosz Terka
"""

import FUNKCJE as fun, math

def rzut_poziomy(x,y,poczatek):
    """
    Funkcja, generująca położenia punktu dla rzutu poziomego. Funkcja korzsyta ze wzorów fizycznych.

    Parameters
    ----------
    x : lista, zawierająca wartosci współrzędnej x co dt=0.001s
    y : lista, zawierająca wartosci współrzędnej y co dt=0.001s
    poczatek : lista z warunkami początkowymi

    Returns
    -------
    None.

    """
    x.append(poczatek[0])
    y.append(poczatek[1])
    licz_x=1
    licz_y=1
    t=0.001
    while(y[licz_y-1]>=0):
        x.append(x[licz_x-1] +0.001*poczatek[2])
        licz_x+=1
        y.append(y[0]-((9.8*t*t)/2))
        licz_y+=1
        t+=0.001
    fun.rysuj(x,y)
    zasieg=math.fabs(x[licz_x-1]-x[0])
    zasieg=round(zasieg,2)
    print("zasięg rzutu to:" + str(zasieg)+"m")
    print("Siła w momencie uderzenia to ziemię to:9.8N")

def rzut_pionowy(x,y,poczatek):
    """
    Funkcja, generująca położenia punktu dla rzutu pionowego. Funkcja korzsyta ze wzorów fizycznych.

    Parameters
    ----------
    x : lista, zawierająca wartosci współrzędnej x co dt=0.001s
    y : lista, zawierająca wartosci współrzędnej y co dt=0.001s
    poczatek : lista z warunkami początkowymi

    -------
    None.

    """
    if poczatek[3] >0:
        for i in range(2):
            x.append(poczatek[0])
        h_max=(poczatek[3]*poczatek[3])/(2*9.8)
        y.append(h_max)
        y.append(0)
    else:
        y.append(poczatek[1])
        y.append(0)
        for i in range(2):
            x.append(poczatek[0])
    print("zasięg rzutu to:0m")
    print("Siła w momencie uderzenia to ziemię to:9.8N")
    fun.rysuj(x,y)
    
def rzut_spadajacy(x,y,poczatek):
    """
    
Funkcja, generująca położenia punktu dla rzutu spadającego. Funkcja korzsyta ze wzorów fizycznych.

    Parameters
    ----------
    x : lista, zawierająca wartosci współrzędnej x co dt=0.001s
    y : lista, zawierająca wartosci współrzędnej y co dt=0.001s
    poczatek : lista z warunkami początkowymi

    Returns
    -------
    None.

    """
    y.append(poczatek[1])
    y.append(0)
    for i in range(2):
        x.append(poczatek[0])
    fun.rysuj(x,y)
    print("zasięg rzutu to:0m")
    print("Siła w momencie uderzenia to ziemię to:9.8N")
    
def rzut_ukosny(x,y,poczatek):
    x.append(poczatek[0])
    y.append(poczatek[1])
    licz_x=1
    licz_y=1
    t=0.001
    t2=0.001
    flaga=0
    h_max=poczatek[1]+(poczatek[3]*poczatek[3])/(2*9.8)
    if poczatek[3]>0:
        while y[licz_y-1]>=0:
            if flaga==0:
                y.append(y[0]+poczatek[3]*t+-9.8*t*t/2)
                licz_y+=1
                t+=0.001
            else:
                y.append(h_max-((9.8*t2*t2)/2))
                t2+=0.001
                licz_y+=1
            if y[licz_y-1]>=h_max:
                flaga=1
            x.append(x[licz_x-1] +0.001*poczatek[2])
            licz_x+=1
    elif poczatek[3]<0:
        while y[licz_y-1]>=0:
         y.append(y[0]+poczatek[3]*t-9.8*t*t/2)
         licz_y+=1
         t+=0.001
         x.append(x[licz_x-1] +0.001*poczatek[2])
         licz_x+=1
    fun.rysuj(x,y)
    zasieg=math.fabs(x[licz_x-1]-x[0])
    zasieg=round(zasieg,2)
    print("zasięg rzutu to:" + str(zasieg)+"m")
    print("Siła w momencie uderzenia to ziemię to:9.8N")
        
    
    
    
    
    
    
    
    
    
    
    
    
    