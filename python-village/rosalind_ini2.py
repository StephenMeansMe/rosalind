# ======================================================================
# ROSALIND - PYTHON VILLAGE: PROBLEM NO. 2
# ----------------------------------------------------------------------
# Pythagorean stuff
# ======================================================================

import math

t_file = "rosalind_ini2_test.txt"
i_file = "rosalind_ini2.txt"
o_file = "rosalind_ini2_ans.txt"

def main():
    
    with open(i_file, "r") as f:
        numbers = f.readline()
    # f.close()
    numbers = numbers.split(" ")
    a = int(numbers[0])
    b = int(numbers[1])
    result = a*a + b*b
    with open(o_file, "w") as answer:
        answer.write(str(result))
    # answer.close()
    return 0

if __name__ == "__main__":
    main()
# That's it.
