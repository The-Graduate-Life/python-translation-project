#!/usr/bin/env python3

"""
translate_orf.py

This script finds the first open reading frame (ORF) in a nucleotide sequence
and translates it into the corresponding amino acid sequence.

Usage:
    python3 translate_orf.py -i <input_file>

Dependencies:
    - find_orf.py: must contain find_first_orf and parse_sequence_from_path functions
"""

import argparse
from find_orf import find_first_orf, parse_sequence_from_path


def translate_first_orf(sequence,
        start_codons=['AUG'],
        stop_codons=['UAA', 'UAG', 'UGA'],
        genetic_code={
            'GUC': 'Valine', 'ACC': 'Threonine', 'GUA': 'Valine', 'GUG': 'Valine', 'ACU': 'Threonine',
            'AAC': 'Asparagine', 'CCU': 'Proline', 'UGG': 'Tryptophan', 'AGC': 'Serine', 'AUC': 'Isoleucine',
            'CAU': 'Histidine', 'AAU': 'Asparagine', 'AGU': 'Serine', 'GUU': 'Valine', 'CAC': 'Histidine',
            'ACG': 'Threonine', 'CCG': 'Proline', 'CCA': 'Proline', 'ACA': 'Threonine', 'CCC': 'Proline',
            'UGU': 'Cysteine', 'GGU': 'Glycine', 'UCU': 'Serine', 'GCG': 'Alanine', 'UGC': 'Cysteine',
            'CAG': 'Glutamine', 'GAU': 'Aspartic acid', 'UAU': 'Tyrosine', 'CGG': 'Arginine', 'UCG': 'Serine',
            'AGG': 'Arginine', 'GGG': 'Glycine', 'UCC': 'Serine', 'UCA': 'Serine', 'UAA': 'Stop',
            'GGA': 'Glycine', 'UAC': 'Tyrosine', 'GAC': 'Aspartic acid', 'UAG': 'Stop', 'AUA': 'Isoleucine',
            'GCA': 'Alanine', 'CUU': 'Leucine', 'GGC': 'Glycine', 'AUG': 'Methionine', 'CUG': 'Leucine',
            'GAG': 'Glutamic acid', 'CUC': 'Leucine', 'AGA': 'Arginine', 'CUA': 'Leucine', 'GCC': 'Alanine',
            'AAA': 'Lysine', 'AAG': 'Lysine', 'CAA': 'Glutamine', 'UUU': 'Phenylalanine', 'CGU': 'Arginine',
            'CGC': 'Arginine', 'CGA': 'Arginine', 'GCU': 'Alanine', 'GAA': 'Glutamic acid', 'AUU': 'Isoleucine',
            'UUG': 'Leucine', 'UUA': 'Leucine', 'UGA': 'Stop', 'UUC': 'Phenylalanine'
        },
        ):

"""
    Find the first ORF and translate it into an amino acid sequence.
"""

    orf = find_first_orf(sequence, start_codons, stop_codons)

    if not orf:
        return None

    amino_acids = []

    for i in range(0, len(orf), 3):
        codon = orf[i:i+3]

        if len(codon) < 3:
            break

        aa = genetic_code.get(codon, "Unknown")

        if aa == "Stop":
            break

        amino_acids.append(aa)

    return amino_acids

def main():
    """ Handle command line arguments and run translation."""

    parser = argparse.ArgumentParser(
        description="Translate the first ORF in a nucleotide sequence."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to the input nucleotide sequence file"
    )

    args = parser.parse_args()

    sequence = parse_sequence_from_path(args.input)

    protein = translate_first_orf(sequence)

    if protein is None:
        print("No ORF found in the sequence.")
        return

    print("Amino acid sequence:")
    print(" - ".join(protein))


if __name__ == "__main__":
    main()
