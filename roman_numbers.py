'''
    Author: Juan Manuel Abréu
    Date: 2024-06-12
    Description: Decimal-Roman numbers converter using Domain Driven Design

    Modelo de dominio: los numeros deben ser 0-3999
    Lenguaje Ubico: 
        - Roman Number: I, V, X, L, C, D, M
        - Decimanl Number: 0-9
        - Conversion: 1-3999
        - Validation: 1-3999
    Delimitador:
        - Conversion de Numeros
    Entidades:
        - DecimalNumber: cada numero decimal puede tener atributos especidficos y reglas asociadas a su conversion
    Objetos de Valor:
        - RomanNumber: representa el resultado de la conversion y no tiene identidad propia
    
    Servicio de Dominio:
        - RomanNumberConverter: es el encargado de realizar la conversion de un numero romano a decimal y viceversa
'''

class DecimalNumber:
    def __init__(self, value: int):
        self.value = value
        self.validate()

    def validate(self):
        try:
            if not (0 < self.value < 4000):
                raise ValueError("The number must be between 1 and 3999")
        except ValueError as e:
            raise e

        except Exception as exc:
            raise ValueError("The number must be an integer") from exc

class RomanNumber:
    def __init__(self, roman_string: str):
        self.roman_string = roman_string

class DecimalRomanConvertor:
    decimal_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    @staticmethod
    def convert(decimal_number: DecimalNumber) -> RomanNumber:
        result = ""
        value = decimal_number.value

        for decimal, roman in DecimalRomanConvertor.decimal_to_roman:
            while value >= decimal:
                result += roman
                value -= decimal

        return RomanNumber(result)

if __name__ == "__main__":
    decimal_number = DecimalNumber(input("Enter a number: "))
    roman_number = DecimalRomanConvertor.convert(decimal_number)
    print(roman_number.roman_string)