#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_ini6.py
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
# ROSALIND - PYTHON VILLAGE: PROBLEM NO. 6
# ----------------------------------------------------------------------
# Fun with dictionaries
# ======================================================================

t_file = "rosalind_ini6_test.txt"
i_file = "rosalind_ini6.txt"
o_file = "rosalind_ini6_ans.txt"

def main():
    
    with open(i_file, "r") as f:
        the_string = f.readline()
    # f.close()
    the_string = the_string.rstrip()
    the_string = the_string.split(" ")
    string_dict = dict.fromkeys(set(the_string), 0)
    for word in the_string:
        string_dict[word] += 1
    # end for
    with open(o_file, "w") as answer:
        for x in string_dict.keys():
            print x, str(string_dict[x])
            answer.write(" ".join([x, str(string_dict[x]), "\n"]))
        # end for
    # answer.close()
	return 0

if __name__ == '__main__':
	main()
