import unittest
def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)
    
class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    
    def test_fizz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(2), "2")

if __name__ == "__main__":
    unittest.main()
