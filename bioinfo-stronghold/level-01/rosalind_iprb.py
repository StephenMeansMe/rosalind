#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_iprb.py
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
# Given: Three positive integers k, m, and n, representing a population 
#   containing k+m+n organisms: k individuals are homozygous dominant 
#   for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms 
#   will produce an individual possessing a dominant allele (and thus 
#   displaying the dominant phenotype). Assume that any two organisms 
#   can mate.
# ======================================================================

def P_2d(k, p):
    # If we're randomly selecting individuals, we have k * (k-1) ways to
    # pick two homozygous dominant individuals.
    # DD + DD -> DD or DD or DD or DD (dominant allele with Pr(D) = 1.0)
    return k * (k - 1) / p

def P_1d1r(k, n, p):
    # If we're randomly selecting individuals, we have k * n ways to 
    # pick a homozygous dominant and a homozygous recessive.
    # DD + rr -> Dr or Dr or Dr or Dr (dominant allele with Pr(D) = 1.0)
    return 2 * k * n / p

def P_1d1h(k, m, p):
    # We have k ways of choosing a homozygous dominant, and m ways of
    # choosing a heterozygous
    # DD + Dr -> DD or DD or Dr or Dr (dominant allele with Pr(D) = 1.0)
    return 2 * k * m / p

def P_1r1h(m, n, p):
    # We have m ways of choosing a heterozygous, and n ways of choosing
    # a homozygous recessive
    # Dr + rr -> Dr or Dr or rr or rr (dominant allele with Pr(D) = 0.5)
    return (m * n / p)
    
def P_2h(m, p):
    # We have m * (m-1) ways of choosing two heterozygous
    # Dr + Dr = DD or Dr or rD or rr (dominant allele with Pr(D) = 0.75)
    return 0.75 * (m * (m - 1) / p) 

t_file = "rosalind_iprb_test.txt"
i_file = "rosalind_iprb.txt"
o_file = "rosalind_iprb_ans.txt"

def main():
    with open(i_file, "r") as f:
        pops = f.readline()
    # f.close()
    pops = pops.rstrip().split(" ")
    K = float(pops[0])
    M = float(pops[1])
    N = float(pops[2])
    P = (K + M + N)*(K + M + N - 1) # All possible pairs
    total_prob = P_2d(K, P) + P_1d1r(K, N, P) + P_1d1h(K, M, P) + P_1r1h(M, N, P) + P_2h(M, P)
    
    with open(o_file, "w") as answer:
        print "Chance of dominant allele: " + str(total_prob)
        answer.write(str(total_prob)) 
    # answer.close()
    return 0

if __name__ == '__main__':
	main()

