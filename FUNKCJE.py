# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:51:49 2021

@author: Bartosz Terka
"""
import random, math, matplotlib.pyplot as plt

def losuj_poczatek():
    """
    Funkcja, która tworzy listę zawierającą warunki początkowe.
    Generuje położenie punktu początkowego.
    Warunki poczatkowe: poczatek=[x0,y0,Vx0,Vy0,typ rzutu]
    Returns
    -------
    poczatek : lista z warunkami początkowymi

    """
    poczatek=[] 
    poczatek.append(random.randint(-5,5))
    poczatek.append(random.randint(0,10))
    return poczatek

def wybierz_rzut(poczatek):
    """
    Funkcja, która wywietla użytkownikowi informację o możliwosciach do wyboru i po pobraniu danych z klawaitury
    dopisuje do listy warunków początkowych składowe prędkosci poczatkowe oraz typ wybranego rzutu.

    Parameters
    ----------
    poczatek : lista z warunkami początkowymi

    Returns
    -------
    poczatek : lista z warunkami początkowymi

    """
    typ=input("WYbierz typ rzutu: 1-poziomy 2-pionowy 3-spadajacy  4-ukosny")
    if typ=="1":
        if poczatek[1]==0:
            poczatek[1]=random.randint(1,10)
        poczatek.append(random.choice([10,-10]))
        poczatek.append(0)
        poczatek.append(1)
    elif typ=="2":
        poczatek.append(0)
        poczatek.append(random.choice([random.randint(-10,-1),random.randint(1,10)]))
        if poczatek[1]==0 and poczatek[3]<0:
            poczatek[1]=random.randint(1,10)
        poczatek.append(2)
    elif typ=="3":
        if poczatek[1]==0:
            poczatek[1]=random.randint(1,10)
        poczatek.append(0)
        poczatek.append(-0)
        poczatek.append(3)
    elif typ=="4":
        pr_x=random.choice([random.randint(-9,-1),random.randint(1,9)])
        poczatek.append(pr_x)
        pr_y=random.choice([math.sqrt(100-(pr_x*pr_x)),-math.sqrt(100-(pr_x*pr_x))])
        pr_y=round(pr_y,2)
        poczatek.append(pr_y)
        poczatek.append(4)
    else:
        print("nieprawidłowa liczba")
    return poczatek

    
def rysuj(x,y):
    """
    Funkcja, ktora generuje wykres trajektorii lotu f(x)=y, gdzie x,y to współrzędne położenia 

    Parameters
    ----------
    x : lista, zawierająca wartosci współrzędnej x co dt=0.001s
    y : lista, zawierająca wartosci współrzędnej y co dt=0.001s
    Returns
    -------
    None.

    """
    plt.plot(x,y)
    plt.show()

def test_losuj_poczatek():
    poczatek=losuj_poczatek()
    assert poczatek[0] is not None and poczatek[1] is not None, "cos jest nie tak"

def test_wybierz_rzut():
    poczatek=losuj_poczatek()
    print("podczas testu wpisz 1 gdy bedzie to potrzebne")
    poczatek=wybierz_rzut(poczatek)
    assert poczatek[4]==1, "cos jest nie tak"

if __name__ == "__main__":
    test_losuj_poczatek()
    test_wybierz_rzut()

    


