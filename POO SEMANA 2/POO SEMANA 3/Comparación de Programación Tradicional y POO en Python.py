# Comparación de Programación Tradicional

# Define funciones para la entrada de datos diarios (temperaturas)
# y el cálculo del promedio semanal.

# Función para ingresar las temperaturas de la semana
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese la temperatura de cada día de la semana:")
    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Función principal que organiza el flujo del programa
def main():
    # Entrada de datos
    temps = ingresar_temperaturas()

    # Cálculo del promedio
    promedio = calcular_promedio(temps)

    # Salida de resultados
    print("\nTemperaturas registradas:", temps)
    print(f"Promedio semanal de temperatura: {promedio:.2f} °C")


# Ejecutar el programa
if __name__ == "__main__":
    main()
