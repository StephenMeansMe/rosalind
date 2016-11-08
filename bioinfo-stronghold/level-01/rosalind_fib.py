#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_fib.py
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
# ROSALIND - BIOINFORMATICS STRONGHOLD: RABBITS AND RECURRENCE RELATIONS
# ----------------------------------------------------------------------
# Given a number of generations N and a breeding coefficient K, 
#   return the number of rabbits after that many generations
# ======================================================================
t_file = "rosalind_fib_test.txt"
i_file = "rosalind_fib.txt"
o_file = "rosalind_fib_ans.txt"

def rabbits(N, K):
    if N in (1, 2):
        # F_1 = F_2 = 1
        return 1
    else:
        # F_n = F_{n-1} + k * F_{n-2}
        return rabbits(N - 1, K) + K * rabbits(N - 2, K)

def main():
    with open(i_file, "r") as f:
        params = f.readline()
    # f.close()
    params = params.rstrip().split(" ")
    n = int(params[0])
    k = int(params[1])
    rabbitpop = rabbits(n, k)
    with open(o_file, "w") as answer:
        print str(rabbitpop) + " rabbits!"
        answer.write(str(rabbitpop))
    # answer.close()
	
    return 0

if __name__ == '__main__':
	main()
