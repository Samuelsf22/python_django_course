class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "No se puede dividir entre cero"

    def factorial(self, valor):
        if valor == 0:
            return 1
        else:
            fact = 1
            for i in range(1, valor + 1):
                fact *= i
            return fact

    def radicacion(self):
        return self.valor1 ** (1 / self.valor2)


try:
    num1 = int(input("Ingrese el primer valor entero: "))
    num2 = int(input("Ingrese el segundo valor entero: "))

    calculadora = Calculadora(num1, num2)

    print("\nOperaciones")
    print(f"Suma: {calculadora.suma()}")
    print(f"Resta: {calculadora.resta()}")
    print(f"Multiplicación: {calculadora.multiplicacion()}")
    print(f"División: {calculadora.division():.2f}")
    print(f"Factorial de {num1}: {calculadora.factorial(num1)}")
    print(f"Factorial de {num2}: {calculadora.factorial(num2)}")
    print(f"Radicación: {calculadora.radicacion():.2f}")

except ValueError:
    print("Por favor ingrese valores numéricos válidos.")
