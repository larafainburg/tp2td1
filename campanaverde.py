from haversine import haversine, Unit

class CampanaVerde:
    
    def __init__(self,lat,lng,d,b,c,m,i):
        ''' Inicializa una campanaverde con direccion d, barrio b, comuna c, materiales m, longitud y latitud l. '''
        
        self.latitud:float= float(lat)
        self.longitud:float= float(lng)
        self.direccion:str= d
        self.barrio:str= b
        self.comuna:int= int(c)
        self.materiales:set[str]= m
        self.info= i
        
    def distancia(self,lat,lng)-> float:
        ''' devuelve la distancia entre la CampanaVerde y el punto ingresado'''
        punto1:tuple[float,float]= (self.latitud,self.longitud)
        punto2:tuple[float,float]= (lat,lng)
        distancia= haversine(punto1,punto2, unit= Unit.METERS)
        return distancia
    
    def __repr__(self) -> str:
        ''' Devuelve una representación string de la campanaverde '''
        return "<" + self.direccion + "@" + "/".join(sorted(list(self.materiales))) + "@" + self.barrio + ">"
