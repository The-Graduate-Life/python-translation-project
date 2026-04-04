#!/usr/bin/env python3

"""
translate_orf.py

This script finds the first open reading frame (ORF) in a nucleotide sequence
and translates it into the corresponding amino acid sequence.

Usage:
    python3 translate_orf.py -i <input_file>

Dependencies:
    - find_orf.py: must contain find_first_orf and parse_sequence_from_path functions
    - translate.py: must contain translate_sequence function and genetic code dictionary
"""


