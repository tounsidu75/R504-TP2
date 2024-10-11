# test_fizzbuzz.py
import unittest
from io import StringIO
import sys
from fizzbuzz import affiche  # Assurez-vous d'importer la fonction à tester

class TestFizzBuzz(unittest.TestCase):

    def test_affiche(self):
        expected_output = (
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz18FizzBuzz"
            "1920Fizz21Fizz22Fizz24Buzz2526Fizz28FizzBuzz2930Fizz31"
            "32Fizz34FrisBee3637Fizz38FizzBuzz3940Fizz41Fizz42"
            "44Buzz4546Fizz48FizzBuzz4950Fizz51Fizz52Fizz54Buzz"
            "5556Fizz58FizzBuzz5960Fizz61Fizz62"
            "64Buzz6566Fizz68FizzBuzz6970Fizz71Fizz72"
            "74FrisBee7677Fizz78FizzBuzz79"
            "81Fizz82Fizz84Buzz8586Fizz88FizzBuzz"
            "9192Fizz94Buzz9596Fizz98FizzBuzz"
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        affiche()  # Appel de la fonction sans paramètres
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
