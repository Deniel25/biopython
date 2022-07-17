from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys
import warnings
warnings.filterwarnings("ignore")

# Bladimir Pardo
# Daniel Diaz
# Nicol Huaiquil
# Felipe Lagos

def main():
    #Validacion de Argumentos
    if len(sys.argv) != 2:
        print(f'USO: {sys.argv[0]} <Hebra>')
        sys.exit()
    seq = sys.argv[1]
    
    #Blasteo
    print('BLASTeando secuencia...')
    result_handle = NCBIWWW.qblast("blastn", "nt", seq)
    with open("resultado_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    resultados = open("resultado_blast.xml")
    blast_record = NCBIXML.read(resultados)

    for alineamiento in blast_record.alignments:  # alignments se refiere a los hits
        for hsp in alineamiento.hsps: # recore HSPs
            hit_seq = (alineamiento.title.split('|'))[1]
            break
        break
    resultados.close()

    #Descarga de Datos
    print('Obteniendo información del gen...')   
    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=hit_seq) as handle:
        seq_record = SeqIO.read(handle, "gb")
        print(f'Especie: {seq_record.annotations["organism"]}')
        print(f'Gen identificado: {seq_record.name} ')
        print(f'Ubicación: {seq_record.features[0].location}')
        print(f'Exones en el gen: {len(seq_record.features)}')

main()