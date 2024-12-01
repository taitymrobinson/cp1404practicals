"""
CP1404 Practical 10
Testing code using assert and doctest
"""
import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not pass test when "

    car = Car()
    assert car.fuel == 0, "Car does not pass test when "

run_tests()


doctest.testmod()
def format_phrase(phrase):
    """
    Format phrase into a sentence, starting with a capital and ending with a full stop.
    >>> format_phrase("hello.")
    'Hello.'
    >>> format_phrase("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase("sad face.")
    'Sad face.'
    """
    sentence = phrase[0].upper() + phrase[1:]
    if sentence[-1] != ".":
        sentence += "."
    return sentence

