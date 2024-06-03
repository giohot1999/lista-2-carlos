def converterparasegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

horas = 2
minutos = 40
segundos = 10

totalsegundos = converterparasegundos(horas, minutos, segundos)
print(f"{horas}h, {minutos}min e {segundos}seg correspondem a {totalsegundos} segundos.")