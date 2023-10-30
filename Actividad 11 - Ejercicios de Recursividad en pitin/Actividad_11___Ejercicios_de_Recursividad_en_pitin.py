def imprimirTabla(numero, multiplicador=1):
    if multiplicador <= 12:
        resultado = numero * multiplicador
        print(f"{numero} * {multiplicador} = {resultado}")
        imprimirTabla(numero, multiplicador + 1)

NUM = int(input("DIGITE NÚMERO: "))
imprimirTabla(NUM)
input("Pulse una tecla: ")