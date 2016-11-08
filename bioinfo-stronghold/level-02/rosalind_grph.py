#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_grph.py
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
ROSALIND - BIOINFORMATICS STRONGHOLD: OVERLAP GRAPHS
------------------------------------------------------------------------
Given: A collection of DNA strings in FASTA format having total length 
   at most 10 kbp.

Return: The adjacency list corresponding to O_3. You may return edges in 
   any order.
========================================================================
'''

overlaps = set()
proteins = dict()

def overlap_finder(id1, id2):
    # no duplicates!
    if proteins[id1[-3:]] == proteins[id2[:3]]:
        # id1's suffix overlaps id2's prefix
        overlaps.add((id1, id2))
    # end if
    if proteins[id1[:3]] == proteins[id2[-3:]]:
        # id1's prefix overlaps id2's suffix
        overlaps.add((id2, id1))
    # end if

def main():
    str_buff = "" # buffer for DNA strings
    ids_strings = []
    just_ids = []
    just_str = []
    gc_content = []
    with open(i_file, "r") as f:
        ids_strings = f.readlines()
    # f.close()
    for x in ids_strings:
        if ">" in x:
            just_ids.append(x.rstrip()[1:])
            if str_buff != "":
                just_str.append(str_buff)
                str_buff = ""
            # end if
        else:
            # else we have a (piece of a) DNA string; add it to buffer
            str_buff += x.rstrip()
        # end if
    # end for
	return 0

if __name__ == '__main__':
	main()

