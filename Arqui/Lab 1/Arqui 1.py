
archivo = open("operaciones.txt","r")
for lineas in archivo:
    num1=lineas.split(";")[0]
    num2=lineas.split(";")[1]
    print(num1)
    print(num2)
