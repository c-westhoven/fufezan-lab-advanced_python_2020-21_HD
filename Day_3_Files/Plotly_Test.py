import plotly.graph_objects as go
import pandas as pd
from collections import deque
import argparse

def sequence_from_fasta(fastafile):
    """
    gathering sequences from fasta file
    :param fastafile: fasta file "./name.fasta"
    :return:
    """
    with open(fastafile) as fasta:
        combined_seq = ""
        for line_dict in fasta:
            if not line_dict.startswith(">"):
                combined_seq += line_dict.replace("\n", "")
    return combined_seq


def mapping_dict(amino_acid_properties_csv):
    """
    create a mapping dictionary from csv
    :param amino_acid_properties_csv: "../folder/name.csv"
    :return: mapping_dict
    """
    aa_df = pd.read_csv(amino_acid_properties_csv)
    hydropathy_df = pd.DataFrame.drop(aa_df, columns=["Name", "3-letter code", "Molecular Weight",
                                                      "Molecular Formula", "Residue Formula", "Residue Weight", "pka1",
                                                      "pka2", "pkaX", "pI", "Accessible surface"], axis=1)
    hydropathy_df = hydropathy_df.rename(
        columns={"1-letter code": "aa", "hydropathy index (Kyte-Doolittle method)": "hydropathy"})
    mapping_dict = dict(zip(hydropathy_df.aa, hydropathy_df.hydropathy))
    return mapping_dict


def hydropathy_sequence_list(sequence, mapping_dict):
    """
    creates a list with hydropathy values corresponding to the sequence
    :param sequence: single sequence, str
    :param mapping_dict: mapping_dict with aminoacid: hydropathy
    :return:
    """
    sequence_as_hydropathy = []
    for pos, aminoacid in enumerate(sequence):
        sequence_as_hydropathy.append(mapping_dict.get(sequence[pos]))
    return sequence_as_hydropathy


def plot_bubble(seq_hydropathy, seq_aa=None, title="", xaxis="", yaxis=""):
    """
    plots the sequence (x) against the corresponding values (ex. hydropathy) (y)
    :param seq_hydropathy: list with hydropathy values corresponding to amino acid sequence
    :param seq_aa: generally a string
    :param title: title of plot
    :param xaxis: xaxis label
    :param yaxis: yaxis label
    :return:
    """
    if isinstance(seq_aa, str) == True:
        sequence_aa_list = []
        for pos, aminoacid in enumerate(seq_aa):
            sequence_aa_list.append(aminoacid + str(pos))
    elif seq_aa is None:
        sequence_aa_list = []
        for x in range(len(seq_hydropathy)):
            sequence_aa_list.append(x)
    else:
        sequence_aa_list = seq_aa

    pos_hydropathy = []
    for element in seq_hydropathy:
        pos_hydropathy.append(10 * abs(element))

    data = [
        go.Scatter(
            x=sequence_aa_list,
            y=seq_hydropathy,
            mode='markers',
            marker_size=pos_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text=title,
                      xaxis=dict(
                          title=xaxis
                      ),
                      yaxis=dict(
                          title=yaxis
                      ))
    fig.show()
    return


def sliding_window_hydropathy(sequence, mapping_dict, length):
    """
    creates a sliding window along sequence, and calculates the average at each position
    :param sequence: aminoacid sequence, str
    :param mapping_dict: mapping dict
    :param length: length of window
    :return: list where each element represents the average of the window at a position
    """
    sequence_as_hydropathy_window = deque([], maxlen=length)
    averaged_hydropathy_list = []
    for pos, aa in enumerate(sequence):
        sequence_as_hydropathy_window.append(mapping_dict.get(sequence[pos]))
        if pos > len(sequence) + length:
            break
        average = sum(sequence_as_hydropathy_window) / len(sequence_as_hydropathy_window)
        averaged_hydropathy_list.append(average)
    return averaged_hydropathy_list


def plot_bar(seq_hydropathy, seq_aa=None, title="", xaxis="", yaxis=""):
    """
    plots the sequence (x) against the corresponding values (ex. hydropathy) (y)
    :param seq_hydropathy: list with hydropathy values corresponding to amino acid sequence
    :param seq_aa: generally a string
    :param title: title of plot
    :param xaxis: xaxis label
    :param yaxis: yaxis label
    :return:
    """
    if isinstance(seq_aa, str) == True:
        sequence_aa_list = []
        for pos, aminoacid in enumerate(seq_aa):
            sequence_aa_list.append(aminoacid + str(pos))
    elif seq_aa is None:
        sequence_aa_list = []
        for x in range(len(seq_hydropathy)):
            sequence_aa_list.append(x)
    else:
        sequence_aa_list = seq_aa
    data = [
        go.Bar(
            x=sequence_aa_list,
            y=seq_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text=title,
                      xaxis=dict(
                          title=xaxis
                      ),
                      yaxis=dict(
                          title=yaxis
                      ))
    fig.show()
    return


if __name__ == '__main__':
    # seq = sequence_from_fasta("./P32249.fasta")
    # mapping_dict = mapping_dict("../data/amino_acid_properties.csv")
    # sequence_hydropathy = hydropathy_sequence_list(seq, mapping_dict)
    # plot_bar(seq_hydropathy=sequence_hydropathy, seq_aa=seq, title="Hydropathy Along G Protein Sequence",
    #          xaxis="G Protein Sequence", yaxis="Hydropathy")
    # window = sliding_window_hydropathy(seq, mapping_dict, 15)
    # plot_bar(seq_hydropathy=window)
    # plot_bubble(seq_hydropathy=sequence_hydropathy, seq_aa=seq, title="Hydropathy")

    parser =argparse.ArgumentParser()
    parser.add_argument("--fasta_file", help="FASTA file with the sequence to be analyzed. ", type=str)
    parser.add_argument("--properties", help="csv file with amino acid properties. ", type=str)
    args = parser.parse_args()
    fasta_file_string = args.fasta_file
    aap = args.properties

    seq = sequence_from_fasta(fasta_file_string)
    mapping_dict = mapping_dict(aap)

    sequence_hydropathy = hydropathy_sequence_list(seq, mapping_dict)
    plot_bar(seq_hydropathy=sequence_hydropathy, seq_aa=seq, title="Hydropathy Along G Protein Sequence",
             xaxis="G Protein Sequence", yaxis="Hydropathy")
    window = sliding_window_hydropathy(seq, mapping_dict, 15)
    plot_bar(seq_hydropathy=window)
    plot_bubble(seq_hydropathy=sequence_hydropathy, seq_aa=seq, title="Hydropathy")

    seq.close()         # look up why
    aap.close()

# possible command line input
# python Day_3_Files/Plotly_Test.py --fasta_file "./Day_3_Files./P32249.fasta" --properties "../data/amino_acid_properties.csv"


