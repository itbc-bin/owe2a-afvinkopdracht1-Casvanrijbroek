# Naam: Cas van Rijbroek
# Datum: 26-10-2017
# Versie: 1.4.2

def main():
    bestand = "test.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    headers, seqs = lees_inhoud(bestand)

    x = 0
    seq = ""
    zoekwoord = input("Geef een zoekwoord op: ")
    for line in headers:
        if zoekwoord in line:
            seq += seqs[x]
            print(line)
            print(seq)
            is_dna(seq)
            knipt(seq)
        x += 1
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam, "r")
    sublijst = []
    headers = []
    seqs = []
    dna = ""

    for line in bestand:
        if ">" in line:
            sublijst = line.replace("\n", "")
            headers.append(sublijst)
            dna += " "
        else:
            sublijst = line.replace("\n", "")
            dna += sublijst
        seqs = dna.split(" ")
    del seqs[0]
     
    return headers, seqs

    
def is_dna(seq):
    dna1 = False
    a = seq.count("A")
    c = seq.count("C")
    t = seq.count("T")
    g = seq.count("G")
    totaal = a + c + t + g
    if len(seq) == totaal:
        dna1 = True
    print(dna1)
    
def knipt(seq):
    bestand = open ("enzymen.txt")
    bestand = bestand.readlines()
    enzymen = []
    cor_enzymen =[]
    
    for line in bestand:
        line = line.replace("^", "").split()
        enzymen.append(line)
    for x in enzymen:
        if x[1] in seq:
            print("match met", x[0], "op positie", seq.index(x[1]))
            cor_enzymen.append(x[0])
    
main()
