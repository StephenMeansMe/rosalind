#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  python03.py
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
# ROSALIND - PYTHON VILLAGE: PROBLEM NO. 3
# ----------------------------------------------------------------------
# String slicing
# ======================================================================

t_file = "rosalind_ini3_test.txt"   # sample dataset
i_file = "rosalind_ini3.txt"        # the real dataset
o_file = "rosalind_ini3_ans.txt"    # where to print the answers

def main():
    
	with open(i_file, "r") as f:
        	the_string = f.readline()
        	indices = f.readline()
    # f.close()
	indices = indices.split(' ')
	a = int(indices[0])   # first slice STARTING index
	b = int(indices[1])+1 # first slice ENDING index
	c = int(indices[2])   # second slice STARTING index
	d = int(indices[3])+1 # second slice ENDING index?
	sliced_string = " ".join([the_string[a:b], the_string[c:d]])
	print sliced_string
	with open(o_file, "wr") as answer:
		answer.write(str(sliced_string))
    # answer.close()
	return 0

if __name__ == '__main__':
	main()

