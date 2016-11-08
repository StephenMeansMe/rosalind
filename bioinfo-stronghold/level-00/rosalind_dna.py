#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_dna.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: COUNTING DNA NUCLEOTIDES
# ----------------------------------------------------------------------
# Given a DNA string, return the number of bases A, C, G, and T.
# ======================================================================

t_file = "rosalind_dna_test.txt"
i_file = "rosalind_dna.txt"
o_file = "rosalind_dna_ans.txt"

nt = dict.fromkeys({"A", "C", "T", "G"}, 0)

def main():
    with open(i_file, "r") as f:
        sequence = f.readline()
    # f.close()
    sequence = sequence.rstrip()
    for b in sequence:
        nt[b] += 1
    # end for
    with open(o_file, "w") as answer:
        answer.write(" ".join([str(nt["A"]), str(nt["C"]), 
                               str(nt["G"]), str(nt["T"])]))
    # answer.close()
	return 0

if __name__ == '__main__':
	main()

