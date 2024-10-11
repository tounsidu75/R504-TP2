import unittest
from fizzbuzz import affiche  # Assurez-vous que fizzbuzz est le bon nom de fichier

class TestFizzBuzz(unittest.TestCase):

    def test_affiche(self):
        # Cas de test pour n = 15
        expected_output_15 = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        result = affiche(15)  # Appel de la fonction
        print(result)  # Afficher le résultat de la fonction
        self.assertEqual(result, expected_output_15)

if __name__ == '__main__':
    unittest.main()
