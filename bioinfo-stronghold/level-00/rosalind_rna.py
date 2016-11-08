#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_rna.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: TRANSCRIBING DNA TO RNA
# ----------------------------------------------------------------------
# Given a DNA string, return the RNA string (swapping U <- T)
# ======================================================================

t_file = "rosalind_rna_test.txt"
i_file = "rosalind_rna.txt"
o_file = "rosalind_rna_ans.txt"

def main():
    with open(i_file, "r") as f:
        dna_seq = f.readline() 
    # f.close()
    rna_seq = str.replace(dna_seq, "T", "U")
    with open(o_file, "w") as answer:
        answer.write(rna_seq)
    # answer.close()
	return 0

if __name__ == '__main__':
	main()
