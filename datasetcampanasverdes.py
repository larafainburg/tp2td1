from campanaverde import CampanaVerde
import csv
from typing import TextIO
from haversine import haversine , Unit

class DataSetCampanasVerdes:
    def __init__(self, archivo:str):
        '''inicializa un dataset de campanas verdes con el archivo csv de entrada'''
        self.campanas:list[CampanaVerde]= []
        f:TextIO= open(archivo, encoding= "utf-8")
        dataset:csv.DictReader= csv.DictReader(f,delimiter=";")
        for linea in dataset:
            distancia=(linea["WKT"]).split(" ")
            latitud=float(distancia[1][1:])
            longitud=float(distancia[2][:-1])
            direccion= linea["direccion"]
            barrio= linea["barrio"]
            comuna= int(linea["comuna"])
            materiales= set(linea["materiales"].split(" / "))
            info=linea['mas_info']
            c:CampanaVerde = CampanaVerde(latitud,longitud,direccion,barrio,comuna,materiales,info)
            self.campanas.append(c)
        f.close()
        
    
    def tamano(self) -> int: #O(1)
       '''Devuelve la cantidad de campanas verdes'''
       cantidad:int= len(self.campanas) #O(1)
       return cantidad #O(1)

    def barrios(self) -> set: #O(N*B)
        '''Devuelve el conjunto de todos los barrios existentes'''
        barrios:set[str]=set() #O(1)
        for campana in self.campanas: #O(N)
            barrios.add(campana.barrio) #O(B)
        return barrios #O(1)
    
    def campanas_del_barrio(self,barrio) -> list:
       '''Devuelve una lista con las campanas verdes que 
       están en el barrio indicado'''
       campanas:list[CampanaVerde]=[]
       for campana in self.campanas:
           if campana.barrio == barrio:
               campanas.append(campana)
       return campanas

    def cantidad_por_barrio(self, material) -> dict[str,int]: #tiene que ser O(N*B)
        '''Devuelve un diccionario que indica la cantidad
        de campanas verdes en cada barrio en las que se
        puede depositar el material indicado'''
        cant_campanas_verdes:dict[str,int]={} #O(1)
        for campana in self.campanas: #O(N)
            if material in campana.materiales: 
                barrio = campana.barrio
                if barrio in cant_campanas_verdes:
                    cant_campanas_verdes[barrio]=cant_campanas_verdes [barrio] + 1
                else:
                    cant_campanas_verdes[barrio]=1
        return cant_campanas_verdes #O(1)
        

    def tres_campanas_cercanas(self, lat, lng) -> tuple:
        '''Devuelve una tupla con las 3 campanas verdes más cercanas al punto ingresado'''
        if len(self.campanas) < 3:
            return tuple(self.campanas)  # Devuelve todas las campanas si hay menos de tres
        
        trescampanas = [self.campanas[0], self.campanas[1], self.campanas[2]] # Inicializamos trescampanas con las primeras tres campanas de self.campanas

        if trescampanas[0].distancia(lat, lng) > trescampanas[1].distancia(lat, lng):  # Ordenamos las primeras tres campanas por distancia al punto (lat, lng)
            trescampanas[0], trescampanas[1] = trescampanas[1], trescampanas[0]
        if trescampanas[1].distancia(lat, lng) > trescampanas[2].distancia(lat, lng):
            trescampanas[1], trescampanas[2] = trescampanas[2], trescampanas[1]
        
        # Iteramos sobre las demás campanas para encontrar las más cercanas
        for d in self.campanas[3:]:
            # Comparamos la distancia con la última campana en trescampanas
            if d.distancia(lat, lng) < trescampanas[2].distancia(lat, lng):
                trescampanas[2] = d
                # Reordenamos trescampanas si es necesario
                if trescampanas[2].distancia(lat, lng) < trescampanas[0].distancia(lat, lng):
                    trescampanas[0], trescampanas[2] = trescampanas[2], trescampanas[0]
                elif trescampanas[2].distancia(lat, lng) < trescampanas[1].distancia(lat, lng):
                    trescampanas[1], trescampanas[2] = trescampanas[2], trescampanas[1]
        return tuple(trescampanas)
        
    
    def exportar_por_materiales(self, materiales,archivo_csv) -> None:
        '''genera un nuevo archivo con
        nombre archivo_csv que contiene las campanas verdes en el dataset d en las que se pueda
        depositar todos los materiales del conjunto materiales, conjunto indicado como input del
        método. El archivo generado contiene únicamente las columnas DIRECCION y BARRIO .
        '''
        f:TextIO= open(archivo_csv, 'w', encoding= "utf-8")
        columnas:str ='DIRECCION,BARRIO\n'
        f.write(columnas)
        for campana in self.campanas:
            if materiales & campana.materiales == materiales:
                campanas=str({campana.direccion}) +',' + str({campana.barrio}) +'\n'
                f.write(campanas)
        f.close
    