# Introduction to Programming – Python Solutions

This repository includes Python implementations of exercises adapted from the course **"Introduction to Programming"**. The tasks cover a wide range of beginner programming topics: from working with numbers and strings to simulating random movement and analyzing DNA sequences.

## Exercise List

### Exercise 1 – Weekday Calculator
Function: `weekday(day, month, year)`  
Determines the day of the week (Sunday = 0, ..., Saturday = 6) for a given date using a variation of Zeller’s Congruence formula.

---

### Exercise 2 – Segment Intersection
Function: `segment_length(Ap, Ak, Bp, Bk)`  
Calculates the overlapping segment (if any) between two 1D line segments.

---

### Exercise 3 – 2D Random Walk
Function: `random_walk(n)`  
Simulates a 2D random walk from the origin until the walker is more than `n` units away. The trajectory is visualized using `matplotlib`.

---

### Exercise 4 – Decimal to Binary Converter
Function: `dec2bin(x)`  
Converts a non-negative integer to its binary representation using division and remainder tracking.

---

### Exercise 5 – DNA Complement
Function: `dna_complement(orig_strand)`  
Returns the complementary DNA strand based on Watson-Crick base-pairing rules (A-T, C-G).

---

### Exercise 6 – Gene Finder
Script: `find_genes.py`  
Identifies all valid genes within a DNA sequence and its complementary strand. A gene starts with `ATG`, ends with `TAG`, `TAA`, or `TGA`, is a multiple of 3 bases long, and does not contain internal stop codons.

## Requirements

- Python 3.7+
- `matplotlib` (for Exercise 3)

Install dependencies using:
```bash
pip install matplotlib
