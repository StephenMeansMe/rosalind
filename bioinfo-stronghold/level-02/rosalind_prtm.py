#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_prtm.py
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
ROSALIND - BIOINFORMATICS STRONGHOLD: CALCULATING PROTEIN MASS
------------------------------------------------------------------------
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
========================================================================
'''

monoIsoMass = {}
with open("monoisotopic_mass_table.txt", "r") as d:
    for line in d:
        splitLine = line.split()
        monoIsoMass[splitLine[0]] = float(splitLine[1])
    # end for
# d.close()

t_file = "rosalind_prtm_test.txt"
i_file = "rosalind_prtm.txt"
o_file = "rosalind_prtm_ans.txt"

def main():
    with open(i_file, "r") as f:
        protein = f.readline().rstrip()
    # f.close()
    
    weight = 0
    for aa in protein:
        weight += monoIsoMass[aa]
    # end for
    
    with open(o_file, "w") as answer:
        print weight
        answer.write(str(weight))
    # answer.close()
	return 0

if __name__ == '__main__':
	main()

