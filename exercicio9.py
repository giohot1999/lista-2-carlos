import math

def calcularvolumeesfera(raio):
    return (4/3) * math.pi * raio ** 3

raioesfera = float(input("Digite o raio da esfera: "))
volumeesfera = calcularvolumeesfera(raioesfera)
print("O volume da esfera é:", volumeesfera)