#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_mrna.py
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

'''
========================================================================
ROSALIND - BIOINFORMATICS STRONGHOLD: INFERRING mRNA FROM PROTEIN
------------------------------------------------------------------------
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein 
   could have been translated, modulo 1,000,000. (Don't neglect the 
   importance of the stop codon in protein translation.)
========================================================================
'''

modulus = 10**6   # 1,000,000
codons_per_protein = {"A": 4,
                      "C": 2,
                      "D": 2,
                      "E": 2,
                      "F": 2,
                      "G": 4,
                      "H": 2,
                      "I": 3,
                      "K": 2,
                      "L": 6,
                      "M": 1,
                      "N": 2,
                      "P": 4,
                      "Q": 2,
                      "R": 6,
                      "S": 6,
                      "T": 4,
                      "V": 4,
                      "W": 1,
                      "Y": 2,
                      "Stop": 3}

t_file = "rosalind_mrna_test.txt"
i_file = "rosalind_mrna.txt"
o_file = "rosalind_mrna_ans.txt"

def main():
    with open(i_file, "r") as f:
        protein = f.readline().rstrip()
    # f.close()
    possible_codings = 1
    for p in protein:
        possible_codings = (possible_codings * codons_per_protein[p]) % modulus
    # end for
    possible_codings = (possible_codings * codons_per_protein["Stop"]) % modulus
    with open(o_file, "w") as answer:
        print possible_codings
        answer.write(str(possible_codings))
    # answer.close()
    
	return 0

if __name__ == '__main__':
	main()

