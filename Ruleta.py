import random
import statistics as st
from matplotlib import pyplot as ptl
import numpy as np

#Clases para guardar maximos de funciones
class Max (object): #Clase para guardar maximos de funcion Varianza
    maxi=0 #Inicializa
    def asig(nro): #Funcion de clase que asiga valor a maxi
        Max.maxi=nro
    def ret():#Funcion de clase que devuelve el valor de maxi
        return Max.maxi
class MaxFR (object):#Clase para guardar maximos de funcion Frecuencia relativa
    maxiFR=0.0
    def asig(nro):#Funcion de clase que asiga valor a maxiFR
        MaxFR.maxiFR=nro
    def ret():#Funcion de clase que devuelve el valor de maxiFR
        return MaxFR.maxiFR 

#Valores esperados

def PE(x): #Promemedio esperado
    return int(st.mean(range(0,37)))

def DE(x): #Desvio esperado
    return float(st.pstdev(range(0,37)))#desv_esp

def VE(x):#Varianza Esperada
    return (float(st.pstdev(range(0,37)))**2)

def FrE(x): #Frencuencia espereda
    return 1/37

#Funciones

def maxy(lista:list):#Busca el maximo de la lista para asignarlos a maxi y despues usarlo el maximo de la funcion varianza que contiene a los 8 graficos
    for l in lista:
        if l>=Max.ret():          
            nro=l+10 #el +10 para darle margen y sea mas prolijo
            Max.asig(nro)
    return Max.ret()
def maxFR(lista:list):#Busca el maximo de la lista para asignarlos a maxi y despues usarlo el maximo de la funcion Frecuencia relativa que contiene a los 8 graficos
    for l in lista:
        if l>=MaxFR.ret():          
            nro=(l*1.10) #el 1.10 (10% max del l) para darle margen y sea mas prolijo
            MaxFR.asig(nro)
    return MaxFR.ret()

def graf(figure,x,data,ylimmax,xlabel,ylabel,title,fr): #Funcion para setear valores de las graficas
    ptl.figure(figure) #Nombre figura
    ptl.plot(x,data) #Datos para graficar
    ptl.xlim(0,tiradas) #Rango del eje de las abscisas
    ptl.xlabel(xlabel) #Cartel de las abscisas
    ptl.ylabel(ylabel) #Cartel del eje ordenadas
    ptl.title(title) #Titulo del grafico
    ptl.grid() #Grilla
    ptl.ylim(0,ylimmax)
    ptl.xticks(np.arange(0,tiradas+5,50)) #Intervalo de separacion de las tiradas
    if fr==2: 
        ptl.yticks(np.arange(0, ylimmax,0.01)) #Intervalo de separacion de las frecuencias en el grafico de Frec.Relativa
        ptl.xticks(np.arange(0,tiradas,20)) #Intervalo de separacion de las tiradas en el grafico de Frec.Relativa
    elif fr==3:
        ptl.yticks(np.arange(0,ylimmax,5)) #Intervalo de separacion de las varianzas o desvios en sus respectivos graficos
    else:
        ptl.yticks(np.arange(0,ylimmax+5,1))
       #Intervalo de separacion del resto de los graficos

#Banderas para validar
band=True 
band2=True

#Programa
while band and band2:
    print("Ingrese cantidad de tiradas de la ruleta (Mayor a 0)")
    tiradas=int(input())
    if tiradas>0: #Las tiradas no pueden ser menor a 0
            print("Ingrese apuesta de la ruleta (Mayor a 0 y menor o igual a 36)")
            apuesta=int(input()) #Apuesta es el nro de vos queres que salga osea tu "apuesta"
            if apuesta>0 and apuesta<=36:  #La apuesta no puede ser menor a 0 o mayor a 36 porque no existen otros numeros en la ruleta
                band2=False
else:
    for i in range(0,10): #El 8 proque son 8 rondas
        c=0
        ListaNros=[]#Numeros que salieron en la ronda
        prom=[] #Promedios de los numeros de la ronda
        desv=[] #desvios de los numeros de la ronda
        vari=[] #varianza de los numeros de la ronda
        fr=[]   #Frencuencia relativa respecto a tu apuesta y a los numeros que salieron en la ronda
        vfr=apuesta  #Valor para calcular la frecuencia relativa 
        
        for a in range(0,tiradas):
            ListaNros.insert(a, random.randint(0, 36))#Se guardan los nro de la ronda
            prom.insert(a, st.mean(ListaNros)) #Se guardan los promedios de la ronda
            desv.insert(a, st.pstdev(ListaNros)) #Se guardan los desvios de la ronda
            vari.insert(a, st.pvariance(ListaNros)) #Se guardan las varianza de la ronda
            if(ListaNros[a]==vfr):#Compara tu apuesta con el valor que salio en la "Ruleta" (random.randint)
                c=+1
            fr.insert(a,c/(a+1))#Se guardan las Frec. Relativa de la ronda
        x=np.arange(0,tiradas,1)#Variable del eje X
        
        #frecuencia relativa
        graf('Frecuencia Relativa',x,fr,maxFR(fr),'tiradas (número de tiradas)','fr (frecuencia relativa)',
             'frn (frecuencia relativa del valor = '+str(apuesta)+' con respecto a las tiradas)',2)
        
        #promedio
        graf('Promedio',x,prom,36,'tiradas (número de tiradas)','vp (valor promedio de las tiradas)',
            'vpn (valor promedio de las tiradas con respecto a tiradas)',1)
        
        #desvío
        graf('Desvio',x,desv,15,'tiradas (número de tiradas)','vd (valor del desvío)',
            'vdn (valor del desvío de las tiradas con respecto a tiradas)',4)
        
        #varianza
        graf('Varianza',x,vari,maxy(vari),'tiradas (número de tiradas)','vv (valor de la varianza)',
            'vvn (valor de la varianza de las tiradas con respecto a tiradas)',3)
    
    #Funciones constantes
    ptl.figure('Frecuencia Relativa')#Ubicar grafico por nombre
    ptl.plot(x, [FrE(i) for i in x], color='k', label='frecuencia relativa esperada ('+str(round(FrE(1),5))+')')
    ptl.legend(loc='upper left')
   
    ptl.figure('Promedio')
    ptl.plot(x, [PE(i) for i in x], color='k', label='promedio esperado ('+str(int(PE(1)))+')')
    ptl.legend(loc='upper left')
    
    ptl.figure('Desvio')
    ptl.plot(x, [DE(i) for i in x], color='k', label='desvío esperado ('+str(round(DE(1),5))+')')
    ptl.legend(loc='upper left')
    
    ptl.figure('Varianza')
    ptl.plot(x, [VE(i) for i in x], color='k', label='varianza esperada ('+str(int(VE(1)))+')')
    ptl.legend(loc='upper left') #posicion del cartel que marca que significa la constante
    
    ptl.show()#Mostramos