import pytest
from roman_numbers import DecimalNumber, RomanNumber, DecimalRomanConvertor

def test_decimal_number_1():
    decimal_number = DecimalNumber(1)
    roman_number = DecimalRomanConvertor.convert(decimal_number)
    assert roman_number.roman_string == "I"

def test_decimal_number_2():
    decimal_number = DecimalNumber(10)
    roman_number = DecimalRomanConvertor.convert(decimal_number)
    assert roman_number.roman_string == "X"

def test_decimal_number_3():
    decimal_number = DecimalNumber(3999)
    roman_number = DecimalRomanConvertor.convert(decimal_number)
    assert roman_number.roman_string == "MMMCMXCIX"

def test_decimal_number_4():
    with pytest.raises(Exception):
        assert DecimalNumber("ABC") == "The number must be an integer"

def test_decimal_number_5():
    with pytest.raises(ValueError):
        assert DecimalNumber(4000) == "The number must be between 1 and 3999"