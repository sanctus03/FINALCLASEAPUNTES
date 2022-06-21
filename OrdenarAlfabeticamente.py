#ejemplo ordenado alfabeticamente mediante sort

Nombres = ["Brais","Jorge","Sergio","María","Álvaro","Claudia","Nerea",
           "Beatriz,","Zaira","Ángela","isla","uruguay"]
#si escribimos solo con sort ordena = 1ºMayusculas,2ºMinusculas y 3ºCon tildes
Nombres.sort()
print(Nombres)
#podemos pasarlo todo minusculas si no tuviesemos tildes
Nombres.sort(key = str.lower)
print(Nombres)
#usaremos lambda
Nombres.sort(key = lambda p:p.lower().replace("á","a"). \
             replace("é","e"). \
             replace("í","i"). \
             replace("ó","o"). \
             replace("ú","u"). \
             replace("ñ","nzz"). \
             replace("ü","u"))
print(Nombres)

