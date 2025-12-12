#solución utilizando el paradigma de POO.
#clase que represente la información diaria del clima.
#métodos de la clase para ingresar datos y calcular el promedio semanal.
#conceptos como encapsulamiento, herencia o polimorfismo

# Clase base que maneja datos numéricos (herencia y reutilización de código)
class DatosNumericos:
    def __init__(self):
        self._valores = []  # Encapsulado mediante atributo protegido

    def agregar_valor(self, valor):
        self._valores.append(valor)

    def calcular_promedio(self):
        if len(self._valores) == 0:
            return 0
        return sum(self._valores) / len(self._valores)


# Clase que representa la información diaria del clima (hereda de DatosNumericos)
class ClimaSemanal(DatosNumericos):
    def __init__(self):
        super().__init__()  # Llamada al constructor de DatosNumericos
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Método para ingresar temperaturas de todos los días
    def ingresar_temperaturas(self):
        print("Ingrese la temperatura para cada día de la semana:")
        for dia in self.dias:
            temp = float(input(f"Temperatura del {dia}: "))
            self.agregar_valor(temp)   # Uso del método heredado

    # Polimorfismo: sobreescribimos calcular_promedio si se quisiera manejar datos especiales
    def calcular_promedio(self):
        print("\nCalculando promedio semanal de temperaturas...")
        return super().calcular_promedio()  # reutiliza la lógica base


# Función principal que organiza el uso de la clase
def main():
    clima = ClimaSemanal()

    # Ingreso de temperaturas
    clima.ingresar_temperaturas()

    # Cálculo del promedio semanal
    promedio = clima.calcular_promedio()

    # Salida de resultados
    print("\nTemperaturas registradas:", clima._valores)
    print(f"Promedio semanal: {promedio:.2f} °C")


# Ejecutar programa
if __name__ == "__main__":
    main()
