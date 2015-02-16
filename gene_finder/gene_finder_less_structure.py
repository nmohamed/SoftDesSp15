# -*- coding: utf-8 -*-
"""
Created on Jan 28 2015

@author: Nora Mohamed

"""
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

#TO DO: Add function that checks to make sure DNA string is actually DNA?

def find_ORF(dna):
    """ Takes a DNA sequence and returns every ORF, not including stop codons.
        If there is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: all open reading frames represented as a string in array
    >>> find_ORF("CATGAGATAGGATGAAA")
    ['ATGAGA', 'ATGAAA']
    """
    start = "ATG"
    r_ORF = []
    while True: 
        if start in dna: 
            start_index = dna.index(start) 
            new_ORF = dna[start_index:len(dna)] 

            if new_ORF == "ATG":
                r_ORF.append(new_ORF)
                return r_ORF

            for x in range(3, len(new_ORF), 3): 
                if new_ORF[x:x+3] == "TAG" or new_ORF[x:x+3] == "TGA" or new_ORF[x:x+3] == "TAA":
                    r_ORF.append(new_ORF[0:x])
                    dna = new_ORF[x+3:len(new_ORF)]
                    break
                elif x + 3 >= len(new_ORF):
                    r_ORF.append(new_ORF)
                    return r_ORF
        else: 
            return r_ORF

def find_reverse_complement(dna):
    """ Reverses strand and finds complementary strand

        dna: a DNA sequence
        returns: the reverse complementary strand of dna
    >>> find_reverse_complement("ATCG")
    'CGAT'
    """
    dna = dna[::-1] 
    new = ""
    for x in range(0, len(dna)):
        if dna[x] == 'A':
            new = new + 'T'
        elif dna[x] == 'T':
            new = new + 'A'
        elif dna[x] == 'C':
            new = new + 'G'
        elif dna[x] == 'G':
            new = new + 'C'
        else: 
            raise ValueError
    return new

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    first_strand = find_ORF(dna)
    second_strand = find_ORF(find_reverse_complement(dna))
    return first_strand + second_strand

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGAATTAA")
    'ATGAAT'
    """
    ORFs = find_all_ORFs_both_strands(dna)
    if len(ORFs) > 1:
        longest = max(ORFs, key=len)
        return longest
    elif len(ORFs) == 0: 
        return "x"
    elif len(ORFs) == 1: 
        return ORFs[0]

    #what should this do if they're the same length? and will there only be
    #one ORF on each strand?

def shuffle_string(s):
    """ Shuffles the characters in the input string"""
    return ''.join(random.sample(s,len(s)))

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    shuffled = []
    for trial in range(0, num_trials):
        dna = shuffle_string(dna)
        shuffled.append(longest_ORF(dna))
    longest = max(shuffled, key=len)
    print "longest = " + longest
    return longest

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA. This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
        the input DNA fragment
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    polymer = ""
    for x in range(0, len(dna), 3):
        if x + 3 > len(dna):
            return polymer
        else:
            amino_acid = aa_table[dna[x:x+3]]
            polymer = polymer + amino_acid
    return polymer


def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
    larger than the specified threshold.
    dna: a DNA sequence
    threshold: the minimum length of the ORF for it to be considered a valid
    gene.
    returns: a list of all amino acid sequences whose ORFs meet the minimum
    length specified.
    """
    threshold = len(longest_ORF_noncoding(dna, 1500))  
    all_ORFs = find_all_ORFs_both_strands(dna)

    aas = []
    pass_ORFs = []
    for x in range(0, len(all_ORFs)): 
        if len(all_ORFs[x]) >= threshold:
            pass_ORFs.append(all_ORFs[x])

    for x in range(0, len(pass_ORFs)):
        aas.append(coding_strand_to_AA(pass_ORFs[x]))

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    for x in range(0, len(aas)):
        if len(aas[x]) >= threshold:
            pass_aas.append(aas[x])
    return aas



from load import load_seq
dna = load_seq("./data/X73525.fa")

genes = gene_finder(dna)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
MGIFASAGCGKTMLMHMLIEQTEADVFVIGLIGERGREVTEFVDMLRASHKKEKCVLVFATSDFPSVDRCNAAQLATTVAEYFRDQGKRVVLFIDSMTRYARALRDVALASGERPARRGYPASVFDNLPRLLERPGATSEGSITAFYTVLLESEEEADPMADEIRSILDGHLYLSRKLAGQGHYPAIDVLKSVSRVFGQVTTPTHAEQASAVRKLMTRLEELQLFIDLGEYRPGENIDNDRAMQMRDSLKAWLCQPVAQYSSFDDTLSGMNAFADQN
MFYALYFEIHHLVASAALGFARVAPIFFFLPFLNSGVLSGAPRNAIIILVALGVWPHALNEAPPFLSVAMIPLVLQEAAVGVMLGCLLSWPFWVMHALGCIIDNQRGATLSSSIDPANGIDTSEMANFLNMFAAVVYLQNGGLVTMVDVLNKSYQLCDPMNECTPSLPPLLTFINQVAQNALVLASPVVLVLLLSEVFLGLLSRFAPQMNAFAISLTVKSGIAVLIMLLYFSPVLPDNVLRLSFQATGLSSWFYERGATHVLE

MGDVSAVSSSGNILLPQQDEVGGLSEALKKAVEKHKTEYSGDKKDRDYGDAFVMHKETALPLLLAAWRHGAPAKSEHHNGNVSGLHHNGKSELRIAEKLLKVTAEKSVGLISAEAKVDKSAALLSSKNRPLESVSGKKLSADLKAVESVSEVTDNATGISDDNIKALPGDNKAIAGEGVRKEGAPLARDVAPARMAAANTGKPEDKDHKKVKDVSQLPLQPTTIADLSQLTGGDEKMPLAAQSKPMMTIFPTADGVKGEDSSLTYRFQRWGNDYSVNIQARQAGEFSLIPSNTQVEHRLHDQWQNGNPQRWHLTRDDQQNPQQQQHRQQSGEEDDA
MADYSLAVFGIGLKYLIPFMLLCLVCSALPALLQAGFVLATEALKPNLSALNPVEGAKKLFSMRTVKDTVKTLLYLSSFVVAAIICWKKYKVEIFSQLNGNIVGIAVIWRELLLALVLTCLACALIVLLLDAIAEYFLTMKDMKMDKEEVKREMKEQEGNPEVKSKRREVHMEILSEQVKSDIENSRLIVANPTHITIGIYFKPELMPIPMISVYETNQRALAVRAYAEKVGVPVIVDIKLARSLFKTHRRYDLVSLEEIDEVLRLLVWLEEVENAGKDVIQPQENEVRH
"""
