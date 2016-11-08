#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind-iev.py
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
ROSALIND - BIOINFORMATICS STRONGHOLD: FINDING A MOTIF IN DNA
------------------------------------------------------------------------
Given: Six positive integers, each of which does not exceed 20,000. 
   The integers correspond to the number of couples in a population 
   possessing each genotype pairing for a given factor. In order, the 
   six given integers represent the number of couples having the 
   following genotypes:

   AA-AA
   AA-Aa
   AA-aa
   Aa-Aa
   Aa-aa
   aa-aa

Return: The expected number of offspring displaying the dominant 
   phenotype in the next generation, under the assumption that every 
   couple has exactly two offspring.
========================================================================
'''

t_file = "rosalind_iev_test.txt"
i_file = "rosalind_iev.txt"
o_file = "rosalind_iev_ans.txt"

import numpy as np

probabilities = np.array([1.0, 1.0, 1.0, 0.75, 0.5, 0.0])
children_per_couple = 2

def main():
    with open(i_file, "r") as f:
        couples = np.array([int(x) for x in f.readline().split(' ')])
    # f.close
    ev = children_per_couple * np.dot(probabilities, couples)
    with open (o_file, "w") as answer:
        print ev
        answer.write(str(ev))
    # answer.close()    
    return 0
    
    
if __name__ == '__main__':
	main()

