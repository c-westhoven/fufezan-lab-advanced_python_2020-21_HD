from Classes_Day_4.protein import Protein
import plotly.graph_objects as go


def test_get_data():
    fasta = "/Users/Charlotte/Fufezan_Python_Lab/Day_3_Files/P32249.fasta"
    aa_csv = "../data/amino_acid_properties.csv"
    lookup = "hydropathy"
    testprotein = Protein(fasta, aa_csv, lookup)

    sequence = testprotein.get_data()
    assert sequence == "MDIQMANNFTPPSATPQGNDCDLYAHHSTARIVMPLHYSLVFIIGLVGNLLALVVIVQNRKKINSTTLYSTNLVISDILFTTALPTRIAYYAMGF" \
                       "DWRIGDALCRITALVFYINTYAGVNFMTCLSIDRFIAVVHPLRYNKIKRIEHAKGVCIFVWILVFAQTLPLLINPMSKQEAERITCMEYPNFEET" \
                       "KSLPWILLGACFIGYVLPLIIILICYSQICCKLFRTAKQNPLTEKSGVNKKALNTIILIIVVFVLCFTPYHVAIIQHMIKKLRFSNFLECSQRHS" \
                       "FQISLHFTVCLMNFNCCMDPFIYFFACKGYKRKVMRMLKRQVSVSISSAVKSAPEENSREMTETQMMIHSKSSNGK"


def test_create_mapping_dict():
    fasta = "/Users/Charlotte/Fufezan_Python_Lab/Day_3_Files/P32249.fasta"
    aa_csv = "/Users/Charlotte/Fufezan_Python_Lab/data/amino_acid_properties.csv"
    lookup = "hydropathy"
    testprotein = Protein(fasta, aa_csv, lookup)

    mapping_dict = testprotein.create_mapping_dict()
    mapping_dict_solution = {'Name': {'A': 'Alanine', 'R': 'Arginine', 'N': 'Asparagine', 'D': 'Aspartic acid', 'C': 'Cysteine', 'E': 'Glutamic acid', 'Q': 'Glutamine', 'G': 'Glycine', 'H': 'Histidine', 'I': 'Isoleucine', 'L': 'Leucine', 'K': 'Lysine', 'M': 'Methionine', 'F': 'Phenylalanine', 'P': 'Proline', 'S': 'Serine', 'T': 'Threonine', 'W': 'Tryptophan', 'Y': 'Tyrosine', 'V': 'Valine'}, '3-letter code': {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}, 'aa': {'A': 'A', 'R': 'R', 'N': 'N', 'D': 'D', 'C': 'C', 'E': 'E', 'Q': 'Q', 'G': 'G', 'H': 'H', 'I': 'I', 'L': 'L', 'K': 'K', 'M': 'M', 'F': 'F', 'P': 'P', 'S': 'S', 'T': 'T', 'W': 'W', 'Y': 'Y', 'V': 'V'}, 'Molecular Weight': {'A': 89.1, 'R': 174.2, 'N': 132.12, 'D': 133.11, 'C': 121.16, 'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.18, 'L': 131.18, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13, 'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15}, 'Molecular Formula': {'A': 'C3H7NO2', 'R': 'C6H14N4O2', 'N': 'C4H8N2O3', 'D': 'C4H7NO4', 'C': 'C3H7NO2S', 'E': 'C5H9NO4', 'Q': 'C5H10N2O3', 'G': 'C2H5NO2', 'H': 'C6H9N3O2', 'I': 'C6H13NO2', 'L': 'C6H13NO2', 'K': 'C6H14N2O2', 'M': 'C5H11NO2S', 'F': 'C9H11NO2', 'P': 'C5H9NO2', 'S': 'C3H7NO3', 'T': 'C4H9NO3', 'W': 'C11H12N2O2', 'Y': 'C9H11NO3', 'V': 'C5H11NO2'}, 'Residue Formula': {'A': 'C3H5NO', 'R': 'C6H12N4O', 'N': 'C4H6N2O2', 'D': 'C4H5NO3', 'C': 'C3H5NOS', 'E': 'C5H7NO3', 'Q': 'C5H8N2O2', 'G': 'C2H3NO', 'H': 'C6H7N3O', 'I': 'C6H11NO', 'L': 'C6H11NO', 'K': 'C6H12N2O', 'M': 'C5H9NOS', 'F': 'C9H9NO', 'P': 'C5H7NO', 'S': 'C3H5NO2', 'T': 'C4H7NO2', 'W': 'C11H10N2O', 'Y': 'C9H9NO2', 'V': 'C5H9NO'}, 'Residue Weight': {'A': 71.08, 'R': 156.19, 'N': 114.11, 'D': 115.09, 'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05, 'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.18, 'M': 131.2, 'F': 147.18, 'P': 97.12, 'S': 87.08, 'T': 101.11, 'W': 186.22, 'Y': 163.18, 'V': 99.13}, 'pka1': {'A': 2.34, 'R': 2.17, 'N': 2.02, 'D': 1.88, 'C': 1.96, 'E': 2.19, 'Q': 2.17, 'G': 2.34, 'H': 1.82, 'I': 2.36, 'L': 2.36, 'K': 2.18, 'M': 2.28, 'F': 1.83, 'P': 1.99, 'S': 2.21, 'T': 2.09, 'W': 2.83, 'Y': 2.2, 'V': 2.32}, 'pka2': {'A': 9.69, 'R': 9.04, 'N': 8.8, 'D': 9.6, 'C': 10.28, 'E': 9.67, 'Q': 9.13, 'G': 9.6, 'H': 9.17, 'I': 9.6, 'L': 9.6, 'K': 8.95, 'M': 9.21, 'F': 9.13, 'P': 10.6, 'S': 9.15, 'T': 9.1, 'W': 9.39, 'Y': 9.11, 'V': 9.62}, 'pI': {'A': 6.0, 'R': 10.76, 'N': 5.41, 'D': 2.77, 'C': 5.07, 'E': 3.22, 'Q': 5.65, 'G': 5.97, 'H': 7.59, 'I': 6.02, 'L': 5.98, 'K': 9.74, 'M': 5.74, 'F': 5.48, 'P': 6.3, 'S': 5.68, 'T': 5.6, 'W': 5.89, 'Y': 5.66, 'V': 5.96}, 'hydropathy': {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'E': -3.5, 'Q': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2}, 'Accessible surface': {'A': 44.1, 'R': 159.2, 'N': 80.8, 'D': 76.3, 'C': 56.4, 'E': 99.2, 'Q': 100.6, 'G': 0.0, 'H': 98.2, 'I': 90.9, 'L': 92.8, 'K': 139.1, 'M': 95.3, 'F': 107.4, 'P': 79.5, 'S': 57.5, 'T': 73.4, 'W': 143.4, 'Y': 119.1, 'V': 73.0}}
    assert mapping_dict == mapping_dict_solution


def test_hydropathy_sequence_list():
    fasta = "/Users/Charlotte/Fufezan_Python_Lab/Day_3_Files/P32249.fasta"
    aa_csv = "/Users/Charlotte/Fufezan_Python_Lab/data/amino_acid_properties.csv"
    lookup = "hydropathy"
    testprotein = Protein(fasta, aa_csv, lookup)
    mapping_dict = {'hydropathy': {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'E': -3.5, 'Q': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2}}

    combined_seq = "AAAAA"
    hydropathy_seq_list = testprotein.hydropathy_sequence_list(combined_seq, mapping_dict)
    hydropathy_seq_list_sol = [1.8, 1.8, 1.8, 1.8, 1.8]
    assert hydropathy_seq_list == hydropathy_seq_list_sol


def test_sliding_window():
    fasta = "/Users/Charlotte/Fufezan_Python_Lab/Day_3_Files/P32249.fasta"
    aa_csv = "/Users/Charlotte/Fufezan_Python_Lab/data/amino_acid_properties.csv"
    lookup = "hydropathy"
    testprotein = Protein(fasta, aa_csv, lookup)
    mapping_dict = {
        'hydropathy': {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'E': -3.5, 'Q': -3.5, 'G': -0.4, 'H': -3.2,
                       'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9,
                       'Y': -1.3, 'V': 4.2}}

    combined_seq = "AAAAA"
    sliding_window_list = testprotein.sliding_window(combined_seq, mapping_dict=mapping_dict, length=1)
    sliding_window_list_sol = [1.8, 1.8, 1.8, 1.8, 1.8]
    assert sliding_window_list == sliding_window_list_sol


def test_create_plot_bar():
    fasta = "/Users/Charlotte/Fufezan_Python_Lab/Day_3_Files/P32249.fasta"
    aa_csv = "/Users/Charlotte/Fufezan_Python_Lab/data/amino_acid_properties.csv"
    lookup = "hydropathy"
    window_or_reg = "reg"
    title1 = "Hydropathy Along G Protein Sequence"
    xaxis1 = "G Protein Sequence"
    yaxis1 = "Hydropathy"

    testprotein = Protein(fasta, aa_csv, lookup)
    mapping_dict = testprotein.create_mapping_dict()

    combined_seq = testprotein.get_data()
    if isinstance(combined_seq, str) == True:
        sequence_aa_list = []
        sequence_aa_list = sequence_aa_list
        for pos, aminoacid in enumerate(combined_seq):
            sequence_aa_list.append(aminoacid + str(pos))

    seq_hydropathy = testprotein.hydropathy_sequence_list(combined_seq, mapping_dict)

    data_sol = [
        go.Bar(
            x=sequence_aa_list,
            y=seq_hydropathy
        )
    ]
    fig_sol = go.Figure(data=data_sol)
    fig_sol.update_layout(title_text=title1,
                      xaxis=dict(
                          title=xaxis1
                      ),
                      yaxis=dict(
                          title=yaxis1
                      ))

    fig_test = testprotein.create_plot_bar(title1, xaxis1, yaxis1, window_or_reg=window_or_reg)
    assert fig_test == fig_sol

# !pytest --cov-report html --cov=Classes_Day_4 Day_5_Files/