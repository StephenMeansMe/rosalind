#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_revc.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: COMPLEMENTING A STRAND OF DNA
# ----------------------------------------------------------------------
# Given a DNA string, return the reverse complement
# ======================================================================

t_file = "rosalind_revc_test.txt"
i_file = "rosalind_revc.txt"
o_file = "rosalind_revc_ans.txt"

comps = {"A": "T",
         "C": "G",
         "G": "C",
         "T": "A"}

def main():
    with open(i_file, "r") as f:
        dna_seq = f.readline()
    # f.close()
    dna_seq = dna_seq.rstrip()
    revc_seq = ""
    for x in dna_seq[::-1]:
        revc_seq += comps[x]
    # end for
    with open(o_file, "w") as answer:
        print dna_seq[0:10] + "..."
        print revc_seq[0:10] + "..."
        answer.write(revc_seq)
    # answer.close()
	return 0

if __name__ == '__main__':
	main()
