# Naam: Cas van Rijbroek
# Datum: 26-10-2017
# Versie: 1.5.4

def main():
    sentinel = False
    while sentinel is False:
        try:
            bestand = input("geef de bestandsnaam: ")  # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
            headers, seqs = lees_inhoud(bestand)
            sentinel = True
        except FileNotFoundError:
            print("het bestand is niet gevonden, zet het bestand in de map en probeer het opnieuw")
        except PermissionError:
            print("u heeft niet de juiste rechten om dit bestand in te lezen, verkrijg deze rechten of probeer een ander bestand")
        
    zoekwoord_check = False
    while zoekwoord_check == False:
        try:
            x = 0
            seq = ""
            zoekwoord = input("Geef een zoekwoord op: ")
            for line in headers:
                if zoekwoord in line:
                    zoekwoord_check = True
                    seq += seqs[x]
                    print(line)
                    print(seq)
                    is_dna(seq)
                    knipt(seq)
                x += 1
            if zoekwoord_check == False:
                raise SyntaxError
        except SyntaxError:
            print("het gegeven zoekwoord komt niet in het bestand voor, probeer een ander woord")
    
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
    try:
        dna1 = False
        a = seq.count("A")
        c = seq.count("C")
        t = seq.count("T")
        g = seq.count("G")
        totaal = a + c + t + g
        if len(seq) == totaal:
            dna1 = True
        if dna1 == False:
            raise SyntaxError
    except SyntaxError:
        print("het gegeven bestand bestaat niet uit headers en sequenties met alleen ATCG, controleer de lay out van het bestand")        
        raise SystemExit
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
try:    
    main()
except KeyboardInterrupt:
    print()
    print("u heeft het programma onderbroken")
    
