import unittest

# Importamos el codigo a testear.
from datasetcampanasverdes import DataSetCampanasVerdes

from campanaverde import CampanaVerde

####################################################################

class TestDataSetCampanasVerdes(unittest.TestCase):
  
    def exportar_por_materiales (self): 
        file_in:str = 'fileout.csv'  # archivo especialmente armado para testing
        resultado:str = leer_archivo_v1(file_in)
        valor:str = 'player,position,team,age,club\n'+ \
                    'Aaron Mooy,MF,Australia,32-094,Celtic\n'+ \
                    'Aaron Ramsey,MF,Wales,31-357,Nice\n'+ \
                    'Abdelhamid Sabiri,MF,Morocco,26-020,Sampdoria\n'+ \
                    'Abdelkarim Hassan,DF,Qatar,29-112,Al Sadd SC\n'+ \
                    'Abderrazak Hamdallah,FW,Morocco,32-001,Al-Ittihad\n'
        self.assertEqual(resultado, valor)

unittest.main()

import unittest, os

from jugadores import leer_archivo_v1, leer_archivo_v2, filtrar_por_pais

class TestJugadores(unittest.TestCase):
  
    def test_leer_archivo_v1(self):
        file_in:str = 'test.csv'  # archivo especialmente armado para testing
        resultado:str = leer_archivo_v1(file_in)
        valor:str = 'player,position,team,age,club\n'+ \
                    'Aaron Mooy,MF,Australia,32-094,Celtic\n'+ \
                    'Aaron Ramsey,MF,Wales,31-357,Nice\n'+ \
                    'Abdelhamid Sabiri,MF,Morocco,26-020,Sampdoria\n'+ \
                    'Abdelkarim Hassan,DF,Qatar,29-112,Al Sadd SC\n'+ \
                    'Abderrazak Hamdallah,FW,Morocco,32-001,Al-Ittihad\n'
        self.assertEqual(resultado, valor)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def test_leer_archivo_v2(self):
        file_in:str = 'test.csv'
        resultado:tuple[str, list[str]] = leer_archivo_v2(file_in)
        valor:tuple[str, list[str]] = \
            ('player,position,team,age,club',
             ['Aaron Mooy,MF,Australia,32-094,Celtic',
              'Aaron Ramsey,MF,Wales,31-357,Nice',
              'Abdelhamid Sabiri,MF,Morocco,26-020,Sampdoria',
              'Abdelkarim Hassan,DF,Qatar,29-112,Al Sadd SC',
              'Abderrazak Hamdallah,FW,Morocco,32-001,Al-Ittihad'])
        self.assertEqual(resultado, valor)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def test_filtrar_por_pais_ningun_jugador(self):
        file_in:str = 'test.csv'
        file_temp:str = 'archivo_temporario.csv'  # renombrar si hace falta
        filtrar_por_pais(file_in, file_temp, 'Argentina')
        # Ahora leo el archivo creado, que debería tener solo el encabezado,
        # porque no hay ningún jugador de Argentina en el archivo de test.
        resultado:str = leer_archivo_v1(file_temp)
        valor:str = 'player,position,team,age,club\n'
        self.assertEqual(resultado, valor)
        os.remove(file_temp)
        
    def test_filtrar_por_pais_un_jugador(self):
        file_in:str = 'test.csv'
        file_temp:str = 'archivo_temporario.csv'  # renombrar si hace falta
        filtrar_por_pais(file_in, file_temp, 'Qatar')
        # Ahora leo el archivo creado, que debería tener el encabezado
        # y un jugador de Qatar.
        resultado:str = leer_archivo_v1(file_temp)
        valor:str = 'player,position,team,age,club\n'+ \
                    'Abdelkarim Hassan,DF,Qatar,29-112,Al Sadd SC\n'
        self.assertEqual(resultado, valor)
        os.remove(file_temp)
        
    def test_filtrar_por_pais_dos_jugadores(self):
        file_in:str = 'test.csv'
        file_temp:str = 'archivo_temporario.csv'  # renombrar si hace falta
        filtrar_por_pais(file_in, file_temp, 'Morocco')
        # Ahora leo el archivo creado, que debería tener el encabezado
        # y dos jugadores de Marruecos.
        resultado:str = leer_archivo_v1(file_temp)
        valor:str = 'player,position,team,age,club\n'+ \
                    'Abdelhamid Sabiri,MF,Morocco,26-020,Sampdoria\n'+ \
                    'Abderrazak Hamdallah,FW,Morocco,32-001,Al-Ittihad\n'
        self.assertEqual(resultado, valor)
        os.remove(file_temp)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
if __name__ == '__main__':
    unittest.main()

        
        
        
        





        
        
        
        
        
    

