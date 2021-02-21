import Classes_Day_4.protein as p
import pandas as pd
import plotly.graph_objects as go
import pytest
import sys, os


title1 = "Hydropathy Along G Protein Sequence"
xaxis1 = "G Protein Sequence"
yaxis1 = "Hydropathy"
window_size = 10
window_or_reg = "reg"


def test_get_data():
    fasta = "../Day_3_Files/P32249.fasta"
    aa_csv = "../data/amino_acid_properties.csv"
    lookup = "hydropathy"
    testprotein = p.Protein(fasta, aa_csv, lookup)
    sequence = testprotein.get_data()
    assert sequence == "MDIQMANNFTPPSATPQGNDCDLYAHHSTARIVMPLHYSLVFIIGLVGNLLALVVIVQNRKKINSTTLYSTNLVISDILFTTALPTRIAYYAMGF" \
                       "DWRIGDALCRITALVFYINTYAGVNFMTCLSIDRFIAVVHPLRYNKIKRIEHAKGVCIFVWILVFAQTLPLLINPMSKQEAERITCMEYPNFEET" \
                       "KSLPWILLGACFIGYVLPLIIILICYSQICCKLFRTAKQNPLTEKSGVNKKALNTIILIIVVFVLCFTPYHVAIIQHMIKKLRFSNFLECSQRHS" \
                       "FQISLHFTVCLMNFNCCMDPFIYFFACKGYKRKVMRMLKRQVSVSISSAVKSAPEENSREMTETQMMIHSKSSNGK"

def test_create_mapping_dict():
    assert

def test_hydropathy_sequence_list():
    assert

def test_sliding_window():
    assert

def test_create_plot_bar():
    assert fig == go.Figure(data=data, layout=layout)

# !pytest --cov-report html --cov=Classes_Day_4 Day_5_Files/
