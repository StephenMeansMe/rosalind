#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_gc.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: MENDEL'S FIRST LAW
# ----------------------------------------------------------------------
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp
#   each).
#
# Return: The ID of the string having the highest GC-content, followed 
#   by the GC-content of that string.
# ======================================================================

import itertools

t_file = "rosalind_gc_test.txt"
i_file = "rosalind_gc.txt"
o_file = "rosalind_gc_ans.txt"
error_tol = 0.001

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
    
    just_gcs = []
    for x in just_str:
        x = x.rstrip()
        gc = 100 * (float(x.count("C")) + float(x.count("G"))) / float(len(x))
        just_gcs.append(gc)
    # end for    
    sort_gcs = sorted(zip(just_ids, just_gcs), 
                      key=lambda tup: tup[1], reverse = True)
    with open(o_file, "w") as answer:
        print sort_gcs[0]
        answer.write(sort_gcs[0][0] + '\n')
        answer.write(str(sort_gcs[0][1]))
    # answer.close()

    return 0

if __name__ == '__main__':
	main()

