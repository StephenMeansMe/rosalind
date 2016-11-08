#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_hamm.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: COUNTING POINT MUTATIONS
# ----------------------------------------------------------------------
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# 
# Return: The Hamming distance d_H(s,t).
# ======================================================================

from itertools import izip

def hamming_dist(s, t):
    assert len(s) == len(t)
    return sum(c1 != c2 for c1, c2 in izip(s, t))

t_file = "rosalind_hamm_test.txt"
i_file = "rosalind_hamm.txt"
o_file = "rosalind_hamm_ans.txt"

def main():
    with open(i_file, "r") as f:
        S = f.readline()
        T = f.readline()
    # f.close()
    S = S.rstrip()
    T = T.rstrip()
    with open(o_file, "w") as answer:
        hd = str(hamming_dist(S, T))
        print hd
        answer.write(hd)
    return 0

if __name__ == '__main__':
	main()

