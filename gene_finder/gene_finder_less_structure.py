# -*- coding: utf-8 -*-
"""
Created on Jan 28 2015

@author: Nora Mohamed

"""
from amino_acids_less_structure import aa, codons
import random
from load import load_seq

def find_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> find_ORF("ATGAGATAGGATGAAAAAATAA")
    ['ATGAGA', 'ATGAAAAAA']
    """
    start = "ATG"
    r_ORF = []
    while True: #looping to find every ORF
        #Finds start codon
        if start in dna: #checks to make sure start codon can be found
            start_index = dna.index(start) #find index of ATG
            new_ORF = dna[start_index:len(dna)] #new ORF, placeholder type
            #check every three indices after for TAG TGA TAA
            for x in range(3, len(new_ORF), 3): 
                if new_ORF[x:x+3] == "TAG" or new_ORF[x:x+3] == "TGA" or new_ORF[x:x+3] == "TAA":
                    r_ORF.append(new_ORF[0:x]) #add to array new ORF
                    dna = new_ORF[x+3:len(new_ORF)] #replace dna with 
                    break
        else: #if start can't be found, finish
            return r_ORF
    #note: could change new_ORF to dna? look it over again

def find_reverse_complement(dna):
    """ Finds complementary strand to input (doesn't reverse it)

        dna: a DNA sequence
        returns: the complementary strand of dna
    >>> find_complement("ATCG")
    'CGAT'
    """
    dna = dna[::-1] #reverse string
    new = ""
    for x in range(0, len(dna)): #check for compliment
        print dna[x]
        if dna[x] == 'A':
            new = new + 'T'
        elif dna[x] == 'T':
            new = new + 'A'
        elif dna[x] == 'C':
            new = new + 'G'
        elif dna[x] == 'G':
            new = new + 'C'
        else: #change this so better error is returned, or make way to check 
              #that string is viable
            return 'String is not possible DNA strand'
    return new


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    #find ORF for first strand
    first_strand = find_ORF(dna)
    #find ORF for second strand (find reverse complement of dna)
    second_strand = find_ORF(find_reverse_complement(dna))
    return first_strand.append(second_strand)

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
pass
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
    # TODO: implement this
pass
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
    larger than the specified threshold.
    dna: a DNA sequence
    threshold: the minimum length of the ORF for it to be considered a valid
    gene.
    returns: a list of all amino acid sequences whose ORFs meet the minimum
    length specified.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()