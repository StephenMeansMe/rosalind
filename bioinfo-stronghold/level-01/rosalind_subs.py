#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_subs.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: FINDING A MOTIF IN DNA
# ----------------------------------------------------------------------
# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
#  Return: All locations of t as a substring of s.
# ======================================================================

t_file = "rosalind_subs_test.txt"
i_file = "rosalind_subs.txt"
o_file = "rosalind_subs_ans.txt"

def main():
    with open(i_file, "r") as f:
        main_string = f.readline()
        substring = f.readline()
    # f.close()
    main_string = main_string.rstrip()
    substring = substring.rstrip()
    positions = []
    w = len(substring)
    
    for i in range(0, len(main_string) - w):
        if substring == main_string[i:i+w]:
            positions.append(str(i+1))
        # end if
    # end for
    
    with open(o_file, "w") as answer:
        positions = " ".join(positions)
        print positions
        answer.write(positions)
    # answer.close()
    return 0

if __name__ == '__main__':
	main()

