#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_ini5.py
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
# ROSALIND - PYTHON VILLAGE: PROBLEM NO. 5
# ----------------------------------------------------------------------
# Reading and returning even-numbered lines of a file
# ======================================================================

import itertools

t_file = "rosalind_ini5_test.txt"
i_file = "rosalind_ini5.txt"
o_file = "rosalind_ini5_ans.txt"

def main():
    
    numlines = sum(1 for line in open(i_file))
    with open(o_file, "w") as answer:
        with open(i_file, "r") as f:
            for line in itertools.islice(f, 1, None, 2):
                answer.write(line)
            # end for
        # f.close
        print " ".join(["File", i_file, "opened:", str(numlines), "lines read."])
    # answer.close()
	return 0

if __name__ == '__main__':
	main()

