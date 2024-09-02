class NumeroComplejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = '+' if self.imaginario >= 0 else ''
        return f"{self.real} {signo}{self.imaginario}i"

    def __add__(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imaginario + otro.imaginario)

    def __sub__(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imaginario - otro.imaginario)

    def __mul__(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

# Ejemplo de uso
complejo1 = NumeroComplejo(3, 2)
complejo2 = NumeroComplejo(1, 7)

print(f"Suma: {complejo1 + complejo2}")
print(f"Resta: {complejo1 - complejo2}")
print(f"Multiplicación: {complejo1 * complejo2}")
print(f"División: {complejo1 / complejo2}")
