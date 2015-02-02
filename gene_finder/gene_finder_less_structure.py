# -*- coding: utf-8 -*-
"""
Created on Jan 28 2015

@author: Nora Mohamed

"""
from amino_acids_less_structure import aa, codons
import random
from load import load_seq

#TO DO: Add function that checks to make sure DNA string is actually DNA

def find_ORF(dna):
    """ Takes a DNA sequence and returns every ORF, not including stop codons.
        If there is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: all open reading frames represented as a string in array
    >>> find_ORF("CATGAGATAGGATGAAAAAATAA")
    ['ATGAGA', 'ATGAAAAAA']
    """
    start = "ATG"
    r_ORF = []
    while True: #looping to find every ORF
        #Finds start codon
        if start in dna: #checks to make sure start codon can be found
            start_index = dna.index(start) #find index of ATG
            new_ORF = dna[start_index:len(dna)] #new ORF

            if new_ORF == "ATG":
                r_ORF.append(new_ORF[0:x]) #if whats left is just "ATG"
                return r_ORF

            #check every three indices after for TAG TGA TAA
            for x in range(3, len(new_ORF), 3): 
                if new_ORF[x:x+3] == "TAG" or new_ORF[x:x+3] == "TGA" or new_ORF[x:x+3] == "TAA":
                    r_ORF.append(new_ORF[0:x]) #add to array new ORF
                    dna = new_ORF[x+3:len(new_ORF)] #replace dna with
                    break
                elif x + 3 >= len(new_ORF):
                    #if theres no end codon and you reach the end of the sequence
                    #add the sequence without the end codon 
                    r_ORF.append(new_ORF)
                    return r_ORF
        else: #if start can't be found, finish
            return r_ORF

def find_reverse_complement(dna):
    """ Finds complementary strand to input and reverses

        dna: a DNA sequence
        returns: the reverse complementary strand of dna
    >>> find_reverse_complement("ATCG")
    'CGAT'
    """
    dna = dna[::-1] #reverse string
    new = ""
    for x in range(0, len(dna)): #check for compliment
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
    #find ORF for first strand
    first_strand = find_ORF(dna)
    #find ORF for second strand (find reverse complement of dna)
    second_strand = find_ORF(find_reverse_complement(dna))
    return first_strand + second_strand

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