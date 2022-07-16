from Bio.Blast import NCBIWWW
help(NCBIWWW.qblast) # para obtener ayuda

secuencia = input()
especie = "Homo sapiens"
gen = "DNAJB11"
ubicacion = "3q27.3 +"
exones = 11

print("BLASTeando secuencia...")
print("Obteniendo información del gen...")
print("Especie: {}".format(especie))
print("Gen identificado: {}".format(gen))
print("Ubicación: {}".format(ubicacion))
print("Exones en el gen: {}".format(exones))