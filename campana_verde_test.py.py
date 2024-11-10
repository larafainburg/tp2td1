import unittest
from campanaverde import CampanaVerde
class TestCampanaVerde(unittest.TestCase):

     def test_atributos (self):
        campana1 = CampanaVerde(-34.5893377789048, -58.4436445327415, "AGUIRRE 1447", "CHACARITA", 15, {"Papel","Cartón"}, "Los materiales deben estar limpios y secos")
        self.assertAlmostEqual(campana1.latitud, -34.5893377789048)
        self.assertAlmostEqual(campana1.longitud, -58.4436445327415)
        self.assertEqual(campana1.direccion, "AGUIRRE 1447")
        self.assertEqual(campana1.barrio, "CHACARITA")
        self.assertEqual(campana1.comuna, 15)
        self.assertEqual(campana1.materiales, {"Papel","Cartón"})
        self.assertEqual(campana1.info, "Los materiales deben estar limpios y secos")
        
        campana2 = CampanaVerde(-58.4191009755841, -34.6310015644028, "CASTRO 1538", "BOEDO", 5, {"Papel","Cartón","Plastico","Metal","Vidrio"}, "Los materiales deben estar limpios y secos")
        self.assertAlmostEqual(campana2.latitud, -58.4191009755841)
        self.assertAlmostEqual(campana2.longitud, -34.631001564402)
        self.assertEqual(campana2.direccion, "CASTRO 1538")
        self.assertEqual(campana2.barrio, "BOEDO")
        self.assertEqual(campana2.comuna, 5)
        self.assertEqual(campana2.materiales, {"Papel","Cartón","Plastico","Metal","Vidrio"})
        self.assertEqual(campana2.info, "Los materiales deben estar limpios y secos")
        
        campana3 = CampanaVerde(-58.4129892741202, -34.6451594110446, "CACHI 163", "NUEVA POMPEYA", 4, {"Papel","Cartón","Plastico","Metal","Vidrio"}, "Los materiales deben estar limpios y secos")
        self.assertAlmostEqual(campana3.latitud, -58.4129892741202)
        self.assertAlmostEqual(campana3.longitud, -34.6451594110446)
        self.assertEqual(campana3.direccion, "CACHI 163")
        self.assertEqual(campana3.barrio, "NUEVA POMPEYA")
        self.assertEqual(campana3.comuna, 4)
        self.assertEqual(campana3.materiales,  {"Papel","Cartón","Plastico","Metal","Vidrio"})
        self.assertEqual(campana3.info, "Los materiales deben estar limpios y secos")


     def test_distancia(self):
        campana1 = CampanaVerde(-34.5893377789048, -58.4436445327415, "AGUIRRE 1447", "CHACARITA", 15, {"Papel","Cartón"}, "Los materiales deben estar limpios y secos")
        lat = -34.5893377789048
        lng = -58.4436445327415
        distancia_exacta = 0.0
        self.assertAlmostEqual(campana1.distancia(lat, lng), distancia_exacta)

        campana2 = CampanaVerde(-34.6223361926404, -58.5056729127257, "BERMUDEZ 1697", "MONTE CASTRO", 10, {"Papel","Cartón"}, "Los materiales deben estar limpios y secos")
        lat = -34.6133309251926
        lng = -58.5056729127257 
        distancia_exacta = 1001.34  #distancia entre campana2 y ese punto usando haversine 
        self.assertAlmostEqual(campana2.distancia(lat, lng), distancia_exacta, places=2)

        campana3 = CampanaVerde(-34.6310015644028, -58.4191009755841, "CASTRO 1538", "BOEDO", 5,{"Papel","Cartón","Plastico","Metal","Vidrio"}, "Los materiales deben estar limpios y secos")
        lat = -34.567000
        lng = -58.418000
        distancia_exacta = 7117.37  #distancia entre campana 3 y ese punto usando haversine
        self.assertAlmostEqual(campana3.distancia(lat, lng), distancia_exacta, places=2)

     
     def test_repr(self):
        campana1 = CampanaVerde(-34.5893377789048, -58.4436445327415, "AGUIRRE 1447", "CHACARITA", 15, {"Papel","Cartón"}, "Los materiales deben estar limpios y secos")
        esperado = "<AGUIRRE 1447@Cartón/Papel@CHACARITA>"
        self.assertEqual(repr(campana1), esperado)
       

unittest.main()