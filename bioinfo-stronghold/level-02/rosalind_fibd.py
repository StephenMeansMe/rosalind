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

'''
========================================================================
ROSALIND - BIOINFORMATICS STRONGHOLD: RABBITS AND RECURRENCE RELATIONS
------------------------------------------------------------------------
Given a number of generations N and a breeding coefficient K, 
   return the number of rabbits after that many generations
========================================================================
'''

t_file = "rosalind_fibd_test.txt"
i_file = "rosalind_fibd.txt"
o_file = "rosalind_fibd_ans.txt"

def first_m_values(M):
    num_rabbits = [0] * (M+1)
    for i in range(1, M+1):
        if i in (1, 2):
            num_rabbits[i] = 1
        else:
            num_rabbits[i] = num_rabbits[i-1] + num_rabbits[i-2]
        # end if
    # end for
    return num_rabbits

def rabbits(N, M, init_vals):
    if N <= M:
        return init_vals[N]
    else:
        return rabbits(N-1, M, init_vals) + rabbits(N-2, M, init_vals) - rabbits(N-M, M, init_vals) 

def main():
    with open(t_file, "r") as f:
        n, m = [int(x) for x in f.readline().rstrip().split(" ")]
    # f.close()
    print "Population after " + str(n) + " months with a " + str(m) + " month lifespan:"
    init_vals = first_m_values(m)
    print init_vals
    poplist = [rabbits(x, m, init_vals) for x in range(1,n+1)]
    print poplist
    rabbitpop = rabbits(n, m, init_vals)
    with open(o_file, "w") as answer:
        print str(rabbitpop) + " rabbits!"
        answer.write(str(rabbitpop))
    # answer.close()
	
    return 0

if __name__ == '__main__':
	main()
