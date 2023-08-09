import unittest
from functions import sayName
from unittest.mock import patch


class TestPrint(unittest.TestCase):

    def test_non_empty_input(self):
        self.assertEqual(sayName("jorge"), "Hola Jorge")
        self.assertEqual(sayName("RoBeRtO"), "Hola Roberto")
        self.assertEqual(sayName(" "), "Hola  ")
    
    @patch('builtins.input', side_effect=['', 'juanJO'])
    def test_empty_input(self, mock_input):
        expected_output = "Dejaste el nombre vacio"
        with patch('builtins.print') as mock_print:
            result = sayName('')
            mock_print.assert_called_with(expected_output)
            self.assertEqual(result, "Hola Juanjo")

# Añadir test loop 
        
if __name__ == '__main__':
    unittest.main()