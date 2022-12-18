from helper import display_task_name, display_example

'''
Exercise: RNA Transcription
URL: https://exercism.org/tracks/python/exercises/rna-transcription
Instructions

Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

    G -> C
    C -> G
    T -> A
    A -> U
'''


def to_rna(dna_strand: str) -> str:
    nucleotide_complement = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    new_rna_strand = ""
    for nucleotide in dna_strand:
        new_rna_strand += nucleotide_complement[nucleotide]
    
    return new_rna_strand



# Test 1
display_task_name("I", "RnaTranscription > empty rna sequence")
display_example(
    'to_rna("")',
    ""
)
print(to_rna(""), "\n")



# Test 2
display_task_name("II", "RnaTranscription > rna complement of cytosine is guanine")
display_example(
    'to_rna("C")',
    "G"
)
print(to_rna("C"), "\n")




# Test 3
display_task_name("III", "RnaTranscription > rna complement of guanine is cytosine")
display_example(
    'to_rna("G")',
    "C"
)
print(to_rna("G"), "\n")



# Test 4
display_task_name("IV", "RnaTranscription > rna complement of thymine is adenine")
display_example(
    'to_rna("T")',
    'A'
)
print(to_rna("T"), "\n")



# Test 5
display_task_name("V", "RnaTranscription > rna complement of adenine is uracil")
display_example(
    'to_rna("A")',
    'U'
)
print(to_rna("A"), "\n")



# Test 6
display_task_name("VI", "RnaTranscription > rna complement")
display_example(
    'to_rna("ACGTGGTCTTAA")',
    'UGCACCAGAAUU'
)
print(to_rna("ACGTGGTCTTAA"), "\n")