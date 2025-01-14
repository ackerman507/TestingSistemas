import unittest
from unittest import mock
from unittest.mock import Mock, patch 
from viajes import *
    
class Test_viajes(unittest.TestCase):
    @patch.object (Practica_viajes,'viajes_disponibles')
    def test_viajes_disponibles_mock(self, mock_viajes_disponibles):
        mock_viajes_disponibles.return_value = [[1, 330], [2, 250], [3, 100], [4, 50]]

        p = Practica_viajes()
        self.assertEqual(p.clase_principal(), ['Luis - viaje 4', 'Mario - viaje 3', 'Pepe - viaje 2', 'Tom - viaje 1'])

    
    @patch.object (Practica_viajes, 'calcular_tarifa')
    @patch.object (Practica_viajes, 'extraer_conductores')
    def test_calcular_tarifas_y_extraer_conductores_mock(self, mock_extraer_conductores, mock_calcular_tarifa):
        mock_extraer_conductores.return_value = [['Juan', 3], ['Jesus', 4], ['Laila', 2], ['Pancho',7], ['Omar', 2]]
        mock_calcular_tarifa.side_effect = [300, 100, 400, 12, 34]

        p = Practica_viajes()
        self.assertEqual(p.clase_principal(), ['Luis - viaje 4', 'Mario - viaje 5', 'Pepe - viaje 2', 'Tom - viaje 1', 'Andres - viaje 3'])

    
    @patch.object (Practica_viajes, 'calcular_tarifa')
    def test_calcular_tarifas_mock(self, mock_calcular_tarifa):
        mock_calcular_tarifa.side_effect = [34, 87, 43, 45]

        p = Practica_viajes()
        self.assertEqual(p.clase_principal(), ['Luis - viaje 1', 'Mario - viaje 3', 'Pepe - viaje 4', 'Tom - viaje 2'])

    
if __name__ == "__main__":
    unittest.main()




