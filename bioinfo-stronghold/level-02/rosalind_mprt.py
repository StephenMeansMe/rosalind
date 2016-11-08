#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rosalind_mprt.py
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
ROSALIND - BIOINFORMATICS STRONGHOLD: FINDING A PROTEIN MOTIF
------------------------------------------------------------------------
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output 
  its given access ID followed by a list of locations in the protein 
  string where the motif can be found.
========================================================================
'''

import requests

def n_glycofinder(substring):
    isGlyco = False
    # N, not-a-P, S-or-T, not-a-P
    if substring[0] == "N":
        if substring[1] != "P":
            if substring[2] in ("S", "T"):
                if substring[3] != "P":
                    isGlyco = True
                # end if
            # end if
        # end if
    # end if
    return isGlyco

t_file = "rosalind_mprt_test.txt"
i_file = "rosalind_mprt.txt"
o_file = "rosalind_mprt_ans.txt"

def main():
    prot_ids = []
    with open(t_file, "r") as f:
        prot_ids = f.readlines()
        # end for
    # f.close()
    prot_ids = [str(x).rstrip() for x in prot_ids]
    print prot_ids, type(prot_ids)
    s = set()
    for i in prot_ids:
        print i, type(i)
        s.add(i)
        print s
    proteins = dict.fromkeys(s, "")
    for x in prot_ids:
        remote = "http://www.uniprot.org/uniprot/" + x + ".fasta"
        u = requests.get(remote)
        for line in u.text.split("\n"):
            if ">" not in line:
                proteins[x] += line
            # end if
        # end for
    # end for
    
    positions = dict.fromkeys(s, [])
    for x in proteins.keys:
        positions[x] = find_pos(proteins[x])
    # end for
    
    with open(o_file, "w") as answer:
        answer.write()
    # answer.close()
    return 0

if __name__ == '__main__':
	main()

