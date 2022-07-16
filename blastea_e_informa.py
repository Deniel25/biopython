from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio.Blast import NCBIXML
from Bio.SeqUtils import GC

#help(NCBIWWW.qblast) # para obtener ayuda

#secuencia = input()


my_seq = Seq('CTAGCTAGCTAGCTAGTCATGCATGCTAGCTACTCGATCG')
print(type(my_seq))
print(my_seq)

print(my_seq)
print(my_seq[0])
print(my_seq[0:3])
print('--------------------')
print(my_seq.complement())
print(my_seq[::-1])                   # reverse
print(my_seq.reverse_complement())
print('--------------------')
pGC= (my_seq.count('G')+my_seq.count('C'))/len(my_seq)
print(f' %GC: {pGC}')


GC(my_seq)

print(my_seq[2:4])
nuevaSeq = my_seq[2:4] + my_seq[0:2]
print(type(nuevaSeq))
print(nuevaSeq)
print('---------------')
SeqStr = str(my_seq)
print(type(SeqStr))
print(SeqStr)

print("bandera 1")

print(my_seq)
rna = my_seq.transcribe()
dna = rna.back_transcribe()
print(rna)
print(dna)

print(len(rna))
print(rna.translate())      #se vuelve a ejecutar código
print(dna.translate())
print(dna[0:6].translate())

print("bandera 3")


'''
result_handle = NCBIWWW.qblast("blastn", "nt", secuencia)

with open("resultado_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()
print('archivo almacenado')


resultados = open("resultado_blast.xml")

# alternativa 1: solo una consulta
blast_record = NCBIXML.read(resultados)

# alternativa 2: más de una consulta
#blast_records = NCBIXML.parse(result_handle) # retorna handler
#blast_record = next(blast_records) # del handler obtiene el primer registro

# variables para limitar visualización
hits_mostrados = 0
hsps_mostrados = 0
max_hits_a_mostrar = 2
max_hsps_a_mostrar = 3

for alineamiento in blast_record.alignments:  # alignments se refiere a los hits
    for hsp in alineamiento.hsps: # recore HSPs
        print(f'=== Alineamiento  (Hit:{hits_mostrados} HSP:{hsps_mostrados}) ===================')
        print(f' Secuencia: {alineamiento.title}') # title concatena tags hit_id y hit_def
        print(f' Largo: {alineamiento.length}') # se refiere al tag hit_len
        print(f' e value: {hsp.expect}') # se refiere al tag Hsp_evalue

        # lo siguiente es solo para limitar la cantidad de registros mostrados
        hsps_mostrados += 1
        if hsps_mostrados >= max_hsps_a_mostrar:
            hsps_mostrados = 0
            break
    hits_mostrados += 1
    if hits_mostrados >= max_hits_a_mostrar:
        break

resultados.close()
'''

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