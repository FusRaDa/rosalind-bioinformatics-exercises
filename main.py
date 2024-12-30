import re


def count_nucleotides(seq):
    result = {"A": 0, "C": 0, "G": 0, "T": 0}
    print(len(seq))
    for s in seq:
        if s == "A":
            result["A"] += 1
        if s == "C":
            result["C"] += 1
        if s == "G":
            result["G"] += 1
        if s == "T":
            result["T"] += 1
    print(result)
    return result


def dna_to_rna(seq):
    rna = re.sub("T", "U", seq)
    print(rna)
    return rna


def complement_dna(seq):
    new_seq = ""
    for s in seq:
        if s == "T":
            new_seq += "A"
        if s == "A":
            new_seq += "T"
        if s == "G":
            new_seq += "C"
        if s == "C":
            new_seq += "G"
    print(new_seq[::-1])
    return new_seq[::-1]


def fibonacci_rabbits(n, k):
    # create fib sequence first
    fib_seq = [1, 1]
    for i in range(2, n + 1):
        next_int = fib_seq[i - 1] + (fib_seq[i - 2] * k)
        fib_seq.append(next_int)

    print(fib_seq[n - 1])
    return fib_seq[n - 1]


def get_fasta_seq(filename):
    sequences = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

        current_name = None
        for line in lines:
            if line.startswith(">"):
                name = line.replace(">", "").replace("\n", "")
                current_name = name
                sequences[name] = ""
                continue

            nucleotides = line.replace("\n", "")
            sequences[current_name] += nucleotides
    return sequences


def get_highest_gc_content(filename):
    sequences = get_fasta_seq(filename)

    sequence_name = ""
    highest_gc = 0

    for key, val in sequences.items():
        total = len(val)
        count = 0
        for n in val:
            if n == "G" or n == "C":
                count += 1
        result = (count / total) * 100
        if result > highest_gc:
            sequence_name = key
            highest_gc = result

    result_str = f"{sequence_name} {highest_gc}"
    print(result_str)
    return result_str


def get_hamming_distance(seq1, seq2):
    if len(seq1) == len(seq2):
        distance = 0
        sequences = zip(seq1, seq2)

        for s1, s2 in sequences:
            if s1 != s2:
                distance += 1

        print(distance)
        return distance


def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product = product * i
    return product


def prob_dominant(k, m, n):
    total = k + m + n
    prob_kk = (k / total) * ((k - 1) / (total - 1))
    prob_km = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    prob_kn = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    prob_mm = (m / total) * ((m - 1) / (total - 1)) * 0.75
    prob_mn = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5
    total_prob_dom = prob_kk + prob_km + prob_kn + prob_mm + prob_mn
    return total_prob_dom


def rna_to_protein_seq(rna_seq):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    protein_seq = ""
    for index, nuc in enumerate(rna_seq):
        if (index + 1) % 3 == 0:
            first_nuc = rna_seq[index - 2]
            second_nuc = rna_seq[index - 1]
            third_nuc = nuc

            codon = first_nuc + second_nuc + third_nuc

            amino_acid = codon_table[codon]

            if amino_acid == "Stop":
                print(protein_seq)
                return protein_seq
            else:
                protein_seq += amino_acid

    print(protein_seq)
    return protein_seq


def get_substring_locations(dna_seq, substring):
    locations = ""
    for index, nuc in enumerate(dna_seq):
        match_seq = dna_seq[index:index + len(substring)]
        if match_seq == substring:
            locations += str(index + 1) + " "
    print(locations)
    return locations


def get_consensus_profile_seq(filename):
    sequences = get_fasta_seq(filename)

    sequences_arr = []

    for key, seq in sequences.items():
        sequences_arr.append(seq)

    print(sequences_arr)


rna = "AUGAGAUGCUCAGAGCCAUACCACAUGGAUUCUUUAAGUGAUGCACAUCCCUAUUCAUACAACGGCCUAAAAAACAAUCACUCGGAUCUCCGCCGUUGCCGAGGAAUUAUCCUUACAAAGAACUCUGUCCUCGUCAACUUAUCGCAGCUCUUUUGGGUGGACUCAUCUAGCACUAUUAAUUACGAGGAGAUUAUGCUUACCUGGGGUGGGCCCGCCGGAUACAGACUUCGCUCCUUAGGAGUGUCGCAGAGUCCAUUUAAUCGAGAGUUCGAAAACAAUUCAAUUGGUCCGCACCUUUUUAUCAGGAUAGGUGCAGCUAGUUGCCCGUGUAUCUGGUUAAGACACUUUAUUACCGGAGUGCUUGAGCCGUUCAACGCGGUGUUAUACCCUGAGUGUAGUAACCCAGGGAUGUUCCGGACAGCAUUGCGCGCCACAUCAGCGUUACAAUCACUUAUCCAAAAAUUACCUUCGGAGAGUACCAUCCACUAUCCCAUCGGGAACCAGCACAUCCGUAUGGUUUGCCGAAUAUUGAUGCCGAAGUCUUCUGUGCGAGUGAGAGGGGGUUGGAUUCAAUUAGACUCAAUUAAGCUAAUCCGUAUCGGAAUUCGUGGUAGCGACAACAACGGUUGGGGAAUGCCCCCAAGGCUGGUGGAUAGAUUUCCGAGCCCAAUCUUCCUAAGAGAUGGACGGCUACCCUCAUCUCGCACAAGCCCUAAUCUUGCGCAAACUCUAUCAUGGCGCUCCGAAUGUGUACAAAUGCGUGGGGAAGAAUCACUUUAUCCAAAAGUGGUAAUGUUCAGCUUCGUGGGAACUUCGGUCUUAGGACUCUCCUCGGGGUGCUCAAAUAAGUAUGCACCGGUGUACCGACAGGCCUGGGUGCCCAGUUCGUCACAAACCCGAUGGAAGCAUACAUUCACGGUACCUUACAGUCUCAUACUAGAUUGGCAUGACUCUGUCUCAGGCUUGUCCCGGACUUCCACGGGUGUACCCGUCAAUUCUCAUUCCCUAAGGAGACUCACGCACACGGUGGUUAUUUCAACGAAUCUUGUUUCUUGUCCGGGGUUACUGGACAAUAAAAUUGAGGACUGUUGUAGUCGGUCUACAGCAUCUUGGGAACACACCCUACUGGAAACUGUGAAUCACCUCUCUGUCAGUAGAUACGGCCAACAGGGCCCGUACGGCAACUACUGGAGAGAUACAUGUUUAGUUCUCCAGCCGAACUUUGCGAUAGGAAGGCGAUUAGCUGAUAAGGCUCAGUUCAUUUCUGUCCAAACGGGUGAUAAGGCCUGGCGCUUAUUUACUGAGUCGGACCUGAUUAAGGGACGUAAUUGCACAAUAGGAAUUAUAGGUUUGGAGGGCGUAUUUUGGCGCUUGCCCGUUAUAACCCGAGCAUUUUGCAUUGGAGGCGUGGAUCUGACUUCUAGGAUAGAACAACCAACUGAAAAGGAUAUGGACCCUCGCGAGCCAGAACGUUGGAGGUUAAAAUCCUCAAAACAAGAACGGAGGUUACUAGACUUUAACCUCUGUCGCGGUUCGAGCUAUCACCAUGCGGAGGCUGACGAUCCUGAGCUCUGCGAACGUCAUAGAUACGUGCAACCUCCGCGCGUAGUUACAGCUUGUGGGCUGGAACGCUUACUUUUGAGAGGCAAUUUGCUGGGUCUAAACCACUUGAUCGCGCGCUUGCAAUUGAUCGUUGUCUUACGAAUUUCAUUAGCUUCUUCCGUACAACGGAAGGUAAGUGAAGGAUUGACAAGUAUGAAAUCCAUAGAAGACCGCUACGUGGGGACGGACUCUCUAAGUAAACAUCCGCUGCCGUGGGCCGGGUUUGCUAUAGAACGCCUUGCGAAGGAGAGCCAACAUUCCAAGGACGGGUGCACGCCUCGGCCGCUGACUCUCCUACGGCGAUUAGGAUAUCCUACAGUGCUGCAGCAGUCUGGCCCAUGUGCCUAUCGAUGCAAUUCACGAGCCGCUUGUCGGAGCGGUGCCAGGGUAGCACGACCUAGGUGGCGCCAACACGUUCCCCACCACCUAACAAUUUUGGGUUGGUACCAAGAACUGCGAGAUAGAGUUCCCACGCCUGGAAUCCGUGGUAGGGUCGACCCUCCGACCGAGGAAGUAGUGGGACCGGUUGUCUCCUGCCGUCUUCAAUCUGUCGAGAUCACAGGGAUGGCAAUAGUAUCGACACCUAACACCAACGGGAAAGGCAAGUGGUCACGAUUGGAAUACCAUCUUACUAGGGACUAUACAUUUUGUAGUGUGCUUCCCACACCCCCGCAGGGCCCAAGGAAGCGGCUAAAAGGCUUGGUGGACAGUAAAGCGCAUCGGUGUGAUUUGCGAACGGAGGGGGUUCUUUACGCGGGAUAUAUUGUCACUUAUAGCGCCAUAUCCUUGCUACUUUUCGUAACUUCUAAGCUCCUUGGAUCCGUGAUUCUCGUCCUGCGAGACCAAGGAGUGGUGGUGGGACCUGGACAAGUCACUUCCAGGCGGACUAUGCCCAUCUUCUCGGAGACGCAGGUGGGGUGGUUCCUAGACGGAUACUCGGGCGUGGUACGCGAUUUAAGGCCACAUGCCGGGACAGUUUUAGAAAAUGGACAUCGCCUUAUCACAGGACGACAAAUCCAACGUCCUAGUUUGACGAAUGAACAGGUGGUAUAUCAACCAAUCGCGGCCGACUUACUAAUCUGGGCUAGAAUUGAGUGUACAAUUCGUGACUCCCACGCAUCUAUGGGACUCCACAACGCGUGUAGUAGUACACCGGACGUGUACUCCGGCGAUAUUAACGUCAUCUAUCUCUCCGCGGAUCCCCAUAUCGGCCGAAUACUAAUUCCAGUGCUGCCAGAUAUCGGUCGUAUCUCCAAAGACCACCAGGAUCCCUACACGUGCCUACACUCGAAACCACUCGAUACCAAUCCCGGCCUUCGGCUAGCGACGAGUGGAUUAUUGCCAAGUGAGUUAUCUCUCAACUUCGCAAAGCGCCGAGCCGGGUCUUUGCUGCCGAGGAGACUCUACCUGCGCGCCGCUUGGAGAAAGCCCAGGGGAAGUCUCUGUCGAAAGAACGAAGGCUAUCUCGAUAGCCAUAAAAGGGCCACUGCCUAUACUAGCAGUUUCUCUUUGAUUUUCAGAUCUCUAUUAGCGCCCAUGAUAUGGCCUAACCGCGUAGUACAUAUGCUAUGCCGUGAUCUGUACUCUCCAAAUACGAUUCCCGUCACAUCUCAAUUAACAACGUUCGUUCGUUUGUCACUAACCCGCCGGUGCUGUAUGCACUUAAACGUGAGGUUAGCGGGAGUUAUCUCGGUAGGCCUAUCAACCUGGAGCAUCCGCUGCGGUACCCCUGCAAACACUUCAUUACAAAAUACGCACAUUACCUCCCCGGACCGGGGGAGAAUUGCGGCUUCGAACCCGCUGGCAGUUUCACAGCCGCGGGGGCUUGGGCUUUCGGACUGGGCCACAACUAGGGGUGGGGCUUCAGGGUUUCCCUUGUUCGCAACUCUUCGCAAGGCUCACCCAUGUAGUAUGAAGCCGACGUGUCAGAUGUGUGAAACACAGAGUGUAGUGAGUCUGUCGGAAGUUGGGUCUUCUGAAGUACGACCAUGGGUCAAGGACUAUGCAUAUCGUCGCGUAAGCAGCCUCAGAUAUGGUAAUUUCUUAGUGACACUUACAGAAAUAUCGAAACGACCACGUGCAAAAAGGACGGAGGAUAAUGAACGUGAAACUACGCGGGAUGUAGGAGCUUCGAGCUUUCGUCACAGAACAAGUCGCCGUCGCCUGCGCCGCAAUUGCAGACAUUCGCGCACGUUGAGUGUGCCGUCGCGACCGGGCGCUAGUCAACCUCUGGUAAAGCUAGUACUACCUGAGGUCGACCCCCAUCAUUCAUCCAUAACCUACCCGUGUACUCCUCACGGCUAUGUGUCAAUCCCAAUAUCCACUACAGGCAAGUGGUUUAGUAUUCUGUUAUUGGUGCACAUUGACAGCCAUGCCCUUGCGCGGUUGUUUUUACUGCCAAUAGACCGUUACAAAUGGGUGGGCAGUGCUGUCACCCCAUCGCGGUCCUUCGAGCAGCACGUGGUGACCAAAUUGGUUCUACGGGGGUCCGGACAGCCUAAUCAUCCCAAGGCCUAUGGUGAAAACGCCUCGGUCGAGGUGACAUGCCCCCGCCCCAUCUGGCCAUGGUCCCCAAGGCACGGUGAUCAGCAGCUACGAACUUUAACCAAUGGCGUUAGCGAUUUAGGGUCAAGACGAGGCGAUUGCAUCACCUUUCGUCACAGGCGAGGACUGUACCUUUAUGACAACACGAAACCCCAGGCAUUUAGAAAAAUCGCUAGCUCCUUGAGAACCUGCAAGGUCCGGAGAGUUGUGCCCGCUUCUCCGUCGGCUAGCACAUCGAAGUUACGAAAGACAACGUACAAUAAGACGUCGAUUAGCAACGCAUCGGUCUUAUCGGAAUUACCAGUCAUACGUACCGAGGUAGACAAUGACUCGAACCUGUACGUCGGUUUGCUAAGGGGGAAGACUAAAACCCCCAUAAUCCUGUCUUUAGUUCUGCACAGCGUAGAAUUUGACGCCCGGCGUAGAACGCAUGUCAGAGAAACACUACAAGUAGACAGCUGCCUAGGAGCACGAUUUUAUGAUUGUUCUCCAUUGACUCUGGCACGCUGGACAUCAACCGGGAGGUCUUAUAAAUCAGAAGACUGCUCAGAGGUAUGUCCAUCAAUUUAUCGAAUUGGCCUAUGGCAGUCCAAAUCGCCGUUACGCGUUUGUCGUGCACCUCUUACAUGGAUCCAUCAAAUUAGUGACCUUUGCCCGCCGAGCAAGUACCGACAACCAGGGUCGAUACCAGGGCCCGCGCCCAAACACCUAAACUUGGGUGCUCCAACUGGAUCGAUAUUUGCCAGACGUACGUCGCCCCUUGCCGUGACACAGGAGGAAGUCAAGUGUCUUAUUAGAAUGCGUGAGAUCCAAAAUUACGGACGCGUCGUUGCGCAGCUCUUAUCGUUACUUCGUUGGAUUUUGAUGACCCGGUAUUGGUCGCAAUCUGGGCCGCCUUUACCCCCAGUAAGAUCCGGCUGCGAGCGCGCGGCGUGCAAAGGCGGGCAAAGGUUUAAGCUGGAAGGCGAUGAAGGCAGCCUCCUGAAGCGUCACGCUAGAACCGGAAAUCGCCGUUUCUAUCCGCGCACUCAUAGUGGAGACAACCUUGUAUUCGCAAUGCAGGUGAGUGGGGAAGACCAAAAUUGGAUCUCUGAAGGUGUCCACGUAACAAAGUUGCCUAUAUCUUUGGAUACUUUGUAUCCGACUUCACGUUGUUACCCUAGUGAGUCUCAGUAUUAUUUCACUCGCUCAGGGAGUAUGAAGAAGUCUACCCGCAGAAGAAACAGAUUCUUUGCGAACACACCCCGCGCAUCAACCGGGCCGGUCCUGUGGGAGGAGACUAAACCGGAGUGUGGCAUGAAUAAUCACGCACAGGCCCAGUGGGCGGGCACCAGCGCGGAAAGGCGCACACUAAGACAAAAACGUAGUUCAAGGGGGUCAUCAUUAGGCGUGACACAUGCUGGAAUUCCAUGUUGGCUAUGGUUGCCAUCCACAUUAUUCGCCCCAAGGCCCGUUUUCGCGGGUUAUCAUGACCCAUUACCAAGCUGCACAGGCACCCAAAUCCUAGUGACACCUGAUUCAUGGGGCCGAAUGCCAAAUCCGUUGGUGCGCCCUACAGAGUUUGUCGCACGAGCCGGGAUUCAAGUACCGCGAAAGUUACGCGCCAAAUUUUACCUAAUGACCUUGAGCCCACGGCUGGAGCCCCUUCAGGCCUCGAACGACUGGCAGGCAGAUCAAUGUUUUAUAAGGAGGCGAGAACUCUUACCCAGGGGAGUCUAUCUGUCAGUUAAGUGGGGCUACGGGAUGUGCCGUGGAGGAGGUUUGAGCAUCGAAUCGAGGGUGGGCGACGCUAUCGGGCACUGGACGAGCAUGUUCCCCCUUGGUAACGAACUUCUGAACGUGAUGGGACUAAGGGCUCCACCUUUACUCGCGGUCGGCUACUCUAAGAUGCUAAUAGUGUCUGUAGCGCACAACCAUUAUAUGAGAUUCAUUGGGUUAGCAGGCGUCCAUGUUCUGUCAUAUAGACGGUGCUGCUCGGGAAGUCGUGACGUAUCCAGUACUUUCGGCGAAACAUCAAGUAGGUGGAAGUAUUGGUUCUGCUCUAUAUUGGUCAAGAAUUCCCAUUGGUCUACGAUUCAGGAUAACUCAGGUACAGCUUUGCGCCGCGCCAUGAACCAGGGGCAAGAUCUCUCCACAGUACGAAAUGAGUGGGGAUAUGACGACAUGAACUUCAGCCUCCUCCUCCAUGGAAGUAUCGGGCCAAAUCCAAUGCCUACGGGAUCCAAACUGCGAGUCUGGAAGGGAUAUGGAGUAGACCAGAUUUCUCUCAAAAGAUCUGUCCUGGUACUACCUCUAGUUAAUUGUAUUUUAAAUCUACCGAGGAGUUCCGUGCUGACUGCCACCCAACCAGUUACCGAUCCUGAUAGCUCCACGUGGCGCAAAACGAUAAGAGCAUGGGACCGCGACCGCAAUUGGACAUCAGUGUUACGUCACUUAGCUUCGCCCCAAAAGCGCGAAAGGUCCUAUAAAGUUCAUUAUCGCAGGUGUUCUAAUAUUAGGACAGGCGUGAUAAGCUAUCACUACGGACCGACUAGGUCCAUGGAACGAAUUCCCCAAAGACGGAUGGUGUUUCGACAUCCAAUAGCACAUCCGGUUUGCGCUCCCGCUGUUGGGCGAGAAGAAGCACAACGCGCGGUACUCGAAACUAUCUUACCUAAACACUGUUCGCUUCAAAGGGUAGGACAGUCUGGGAAGUCUUGUGACUAUCUUACAGCAAGUGCGUUAACAGCUAGCAAGAUAUUCGGCGUCGCUUCAAAACUCCCAACCCCACAGUGGGAGAUGUCUACGGCGGUGAACUCGACACGCGCUAGGGGCUAUCUACGUUUGCAGCCCUUCGAAGGAACGCGGUUGAGAUCACAAUUUCGUCCUAAGGAUCGGGCCCAUUCUCGUGUUUAUCUUGCGUUUUUGUUACGCAUUCGUGGUACCGCAAGGGCUCCCCAUGCCCACGAGUGUAAGGUCACACCUUUACACCGAUCCGUCCCUUUAAGGAAUACCUUCCGAAUUCAUAAGAUGCCCGAAAGAAUCUUCAAAGCUCCCGACAAAGCUGACAUCAGUCCUUUAAGGAUACCCAAACGCCCGUAUGCUGAGGUUUUACAGGCGCCUUAUCAAAUCGGGAGGACUAGAUGUCAAUAUUCUUUGGGAACUACGAAGGUGACCAUUUCGUUUCUCAGGAUCGCCGCAUCCGAAAUGUGUAGCGAGAGUUGUUCAAGACUGAGGGUAUUGAGCACGCGGGUGGUAGCGACACGUACGUAUCCGGGCGUCCACACAAUUCUUAUCCGAGUUUGCGCCUCUGGAGUUGCCAUCGGCCCAUCGGCCAAGGAGGCCCUACUGCGAGCCACGGGCAACACAGUCUUCAUGUUCAUGGUCCGACCGACCAAUAUGCCUUGCCUAAUUGGCCCCACCCCCUUCUGUCGAGGAACACGAUCUCGGUUUAACCGAUGCUCAAUGAGCUGUAAGGCUACCAUAAUGUUCGACUUGUUACGAAUAAAGGACACACCGUGCCCGAGGAGAAAUCAAGUAGCUUGCAGCCGAGCGCAGCGGGCAGGAUUUGUGCGUUCCCCACGCAGCAGGCCUGAGAACAUUAAUGAUUGUUAUCCCCCAGAGUGGACGCUCUACUGGAAGACGCCGGAACUUGACCACACUAAGCCAGCUUUAUCUCGAGUCGAAAGGACUGACACAUACGACACGAACAUCUCGGCUCCGCACUUUUUGGCCCAGUGCAGUAUGACAAGACCAUCGACAAACAUAGUUAUGCCCGAUGCAUGCCAGAAUCUAGCUCCGAUGUUCCAGGUCCAUAUGGGCAAGUACAGAACACGCAUGGAACGUAGCAAGCCUAGUGGGGAGCCUGCUUGUACACUGGGGGGGGGUGCGGCGAACACAUCUGAAACAGUAUUGCGCACCGGACCAGAAUCAGGGAGUACUGAUCCCUUCCCUCGGGAUACGGAUUCGACGUUUCUACCCGCAGUCCUCGCAUCAUUACUUCUUCCAAUCGCGUGGUCUAACGAAAGAACCUCUUCAGUAUUGCGCUGUCCGACAACCCGGAUGGAAAUGUUUAAACGGCUGUCUAUCCCACCUUGGAAGAACUCGCGCGUCCGUUCGAUAUUUGAAAAUACGGUAUAG"
seq1 = "GGACACGGGCATTTAGTGGAGACCTAATCATGCTAAGACCAAACTGTCCCTCTGTGCACCCATACCCCAATGTTGCGGCCGGCAGCGACTACTTGAAGATAGCGTTCGTGGGGGCCGACTTATGCGGGAAACAGTACTAACGGCATTGACGCTGCCCTGTAGGATTCATACATTGTCTCCTCTTGGAAACCACGGGGTCCGCGCCTTCGTGAGTCCGTAGAAGTGGTACACATGATGAGAACGCCAGGTCAATACTATTGATCCGCTCCGTACTTCGATCCCCGAGCTAGCAACGATGCAATGAGTGTTAAGTGCCGGCCGTTTAATACGCGTTGAGAATGGTTTTCATAACGGTCAGCAGTGAGCGTGTTGTGGAGTGAACCGTTATGTGCACAACTCCTCTGGTGTCCGATTCGAGCGGTTTAAGGTATGGCTAGTCGAACGGCATGCGAGGGAGTCATATATCGCATGCTCAGCTAAACTGAGGGGGATATGAATTACGGGCTGATTGTAAATGACCGCTGCGGTTGGTCGGGACCGACCGATCAGGCTGCAACAGCGGTGCACTAAGGGAATACTCACAGTTTCAAGACTTGAAGTGCTTGCATGTAAACCTCACCTTAAGGATCCCTTGGACCGTACAAAATTTGTTCTAGTTGAATTGAGTGCCCAGGGTAGGGCGAATGGCTAAGAGGGCCGGCTAAGTCTTCACGTACCGTTTAATTTCCACAGACTGGGTGACGGTGCATTGGTAAAAATGCTGTGTCATTATCCTTATCCTTATTTGGCGCAGTGGATAACTCTTCTGCGTTGCTGCGCTACGCCTTTAGGTACTTGCAAAGGTGTGCCGGGTTTTATATTAGTAGGTCCGGGATTCACGCATTCGTGCCGTCCGATTCTATGCGTCTGACAGCTTTACCCAACTACTGGTGTCTCTCTGTCTGGCGGAATATTTAC"
seq2 = "AGAAACGGGCCTATTGTGAATAGCGGCGCATCTTGACAAAAAACCAACCATAGGTGCTGCGAGACGCCCATGTTGGGGTCGCCCTCTGTTTCTTAGCAATAGCGTTACACTGGGCCAATGCCTCGGCTAAACAATACCAACCGTAATCACGAAGTAGTTGCTCATTCCGGTATTGGCTTCTTGTGACAATGACGTTCTCGTAGACAGGGAGAGGCCGTCTCCGGTATACAACTTATGAGAATGACAGGTCTGTACTTCTTACCATCTGCGTCCTTCGCCACATTTCCTGATGTACGTGGAGTACAGAATAGTCCCCGAAAGTCTTGGGAGGATTCGGAGAGAGATGCTTAACAATAAGGAGAAAGGTTGTCGTAGATTGTATCATTATGTTCACAATTCCACTGTTGATTAAAACATTACGTTACAAGAAGGGCGGGACCTTCGGAAACTGTAACACTTGTGTAGCGTAAGGCCACTTGTACGTCAGTGTTTGTGACCTAACGACTGGTTATATATGTGCGTTCTCGGCGTGGCGGACCCCCCGAGACGGCACCACAGCACCTTAGCGAAGTGGCTGTTTACAGTTTTAAGACCTTATATATTAGCCTATCGAACCCAGATTGATGATGCATTGCGCCATACACAGTCCAATGTAAGCGGATAGCCTGGCCTCAGCAAGCCCGTTCTCGACGAGGAAAGGCGCGACCTTCACGGACCGACTAATTTACAAAGTCTCAAACAGCGTGCGCGGGTAAAGCCGCTTCTGACTTGATGTAAGTTGTTCTTTGAGCTCTCACGATCGTTGATGCGCTAACGCCTCAGTAGTATAGAGAGGTCGAATGGAGTAGCCCTGATTAGATTAACAGAGCAGGGCCTGATGCTTACGGACCCCATGGTTCGACGTGACAAGCAATTTTACCTAAGTTCTATCGGCTTAGTCTCTCACGTCTTTTTTAC"

dna_seq = "TCGGTACACCCGGTACATTTATCGGTACACACGGTACACGGTACACATACGGTACAACTGTGAACAGGCGGTACACAGACGGTACAGCCGTTTATCCTCGGTACAGCATCAACTGGGCCCGGTACACGGCGGTACAACCGGTACAACGGTACACCGGTACAGAGACCGGTACAGTCGGTACACGAGGACCGGTACATACGGTACAACCGGTACATACTTGACGGTACATCGGTACAGGCTCGGTACAGACGGTACAATCGGTACACGGTACAACGGTACAAAACGGTGCTCGGTACACTTCGGTACAGCGGTACAAACGTCCGGTACAGGTGCGGTAAGGCCGGTACACGGTACACGGTACACGTCGGTACATAACGGTACAGCTACGGTACACCGGTACAGCGGTACACAGGTCGGTACAGTGCGGTACACAAGGCGGTACAGGCGGTACATGTTCCGCGGTACATGCGGCGGTACAGGCGCCGGTACAGAGATACGGTACAGAGCCGGTACAGCGGTACAAACGTACGGTACACGGTACAAATGGGGTCGGTACATACTCGGTACACGGTACATCGGTACACGGTACAACCGGTACATCGGTACACGGTACACACGATACACGGTACACGGTACACCGGTACATTCGGTACAACGGTACAGCGGTACAACGGTACAAGGGAGACTCCGGTACACTTTTCAAGGCGGTACATCAATCGGTACAAGGTCGGTACAGTTCGTCGGTACACGGTACAACGGTACACGGTACAGAACCACGGTACACTCGGCGGTACACGGTACATCGGTACAGCTGTGTGCGGTACACCCGGTACAACGGTACACAAGTCGGTACAACCGGTACAGTCGGTACACTGATCGACCCGGTACAT"
substring = "CGGTACACG"

get_consensus_profile_seq("fasta.txt")