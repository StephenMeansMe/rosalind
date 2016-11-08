#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_prot.py
#  
#  Copyright 2016 Stephen Peterson <stephen@brahmin>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# ======================================================================
# ROSALIND - BIOINFORMATICS STRONGHOLD: TRANSLATING RNA INTO PROTEIN
# ----------------------------------------------------------------------
# Given: An RNA string s corresponding to a strand of mRNA (of length at 
#   most 10 kbp).
#
# Return: The protein string encoded by s.
# ======================================================================

def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

codons_a = dict.fromkeys({"GCU", "GCC", "GCA", "GCG"}, "A")
codons_c = dict.fromkeys({"UGU", "UGC"}, "C")
codons_d = dict.fromkeys({"GAU", "GAC"}, "D")
codons_e = dict.fromkeys({"GAA", "GAG"}, "E")
codons_f = dict.fromkeys({"UUU", "UUC"}, "F")
codons_g = dict.fromkeys({"GGU", "GGC", "GGA", "GGG"}, "G")
codons_h = dict.fromkeys({"CAU", "CAC"}, "H")
codons_i = dict.fromkeys({"AUU", "AUC", "AUA"}, "I")
codons_k = dict.fromkeys({"AAA", "AAG"}, "K")
codons_l = dict.fromkeys({"UUA", "UUG", "CUU", "CUC", "CUA", "CUG"}, "L")
codons_m = dict.fromkeys({"AUG"}, "M")
codons_n = dict.fromkeys({"AAU", "AAC"}, "N")
codons_p = dict.fromkeys({"CCU", "CCC", "CCA", "CCG"}, "P")
codons_q = dict.fromkeys({"CAA", "CAG"}, "Q")
codons_r = dict.fromkeys({"CGU", "CGC", "CGA", "CGG", "AGA", "AGG"}, "R")
codons_s = dict.fromkeys({"UCU", "UCC", "UCA", "UCG", "AGU", "AGC"}, "S")
codons_t = dict.fromkeys({"ACU", "ACC", "ACA", "ACG"}, "T")
codons_v = dict.fromkeys({"GUU", "GUC", "GUA", "GUG"}, "V")
codons_w = dict.fromkeys({"UGG"}, "W")
codons_y = dict.fromkeys({"UAU", "UAC"}, "Y")
#codons_stop = dict.fromkeys({"UAA", "UAG", "UGA"}, "")

codon_table = merge_dicts(codons_a, codons_c, codons_d, codons_e, 
                          codons_f, codons_g, codons_h, codons_i, 
                          codons_k, codons_l, codons_m, codons_n,
                          codons_p, codons_q, codons_r, codons_s,
                          codons_t, codons_v, codons_w, codons_y)

t_file = "rosalind_prot_test.txt"
i_file = "rosalind_prot.txt"
o_file = "rosalind_prot_ans.txt"

def main():
    with open(i_file, "r") as f:
        dna = f.readline()
    # f.close()
    dna = dna.rstrip()
    protein = ""
    for i in range(0, len(dna), 3):
        try:
            protein += codon_table[dna[i:i+3]]
        except:
            # We've hit a Stop codon!
            #print "!" + dna[i:i+3] + "!"
            pass
    # end for
    print protein
    with open(o_file, "w") as answer:
        answer.write(protein)
    # answer.close()
    return 0

if __name__ == '__main__':
	main()

