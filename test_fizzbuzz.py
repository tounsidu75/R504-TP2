import unittest
from fizzbuzz import affiche  # Assurez-vous que fizzbuzz est le bon nom de fichier

class TestFizzBuzz(unittest.TestCase):

    def test_affiche(self):
        expected_output_15 = (
            "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz "
            "11 Fizz 13 14 FrisBee"
        )
        result = affiche(100)  # Appel de la fonction
        print(result)  # Afficher le résultat de la fonction
        self.assertEqual(result, expected_output_15.strip())

if __name__ == '__main__':
    unittest.main()
