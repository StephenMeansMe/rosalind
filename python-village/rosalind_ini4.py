#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_ini4.py
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

t_file = "rosalind_ini4_test.txt"
i_file = "rosalind_ini4.txt"
o_file = "rosalind_ini4_ans.txt"

def main():
	
    with open(i_file, "r") as f:
        numbers = f.readline()
    # f.close()
    numbers = numbers.split(" ")
    a = int(numbers[0])
    print a
    b = int(numbers[1])
    print b
    if a % 2 == 0:
        a += 1
    # end if
    sum_of_odds = sum(range(a, b, 2))
    # end for
    if b % 2 == 1:
         # b is odd
         sum_of_odds += b
    # end if
    print sum_of_odds
    with open(o_file, "w") as answer:
        answer.write(str(sum_of_odds))
    # answer.close()
    
	return 0

if __name__ == '__main__':
	main()
