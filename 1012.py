# problem 1012
A , B , C = map(float , input().split())
pi = 3.14159
Area_TRI = (A*C)/2
Area_CIR = C *C * pi
Area_TRA = ((A+B)*C) / 2
Area_QUA = B**2
Area_RET = A * B
print("TRIANGULO: %.3f" %(Area_TRI))
print("CIRCULO: %.3f" %(Area_CIR))
print("TRAPEZIO: %.3f" %(Area_TRA))
print("QUADRADO: %.3f" %(Area_QUA))
print("RETANGULO: %.3f" %(Area_RET))
