import plotly
import plotly.graph_objects as go
import pandas as pd
from collections import deque


def sequence_from_fasta(fastafile):
    with open(fastafile) as fasta:
        combined_seq = ""
        for line_dict in fasta:
            if not line_dict.startswith(">"):
                combined_seq += line_dict.replace("\n", "")
    return combined_seq


def mapping_dict(amino_acid_properties_csv):
    aa_df = pd.read_csv(amino_acid_properties_csv)
    hydropathy_df = pd.DataFrame.drop(aa_df, columns=["Name", "3-letter code", "Molecular Weight",
                                                      "Molecular Formula", "Residue Formula", "Residue Weight", "pka1",
                                                      "pka2", "pkaX", "pI", "Accessible surface"], axis=1)
    hydropathy_df = hydropathy_df.rename(columns={"1-letter code": "aa", "hydropathy index (Kyte-Doolittle method)": "hydropathy"})
    mapping_dict = dict(zip(hydropathy_df.aa, hydropathy_df.hydropathy))
    return mapping_dict


def hydropathy_sequence_list(sequence, mapping_dict):
    """

    :param sequence:
    :param mapping_dict:
    :return:
    """
    sequence_as_hydropathy = []
    for pos, aminoacid in enumerate(sequence):
        sequence_as_hydropathy.append(mapping_dict.get(sequence[pos]))
    return sequence_as_hydropathy


def plot_sequence_bar(sequence_aa, sequence_hydropathy, title="", xaxis="", yaxis=""):

    sequence_aa_list=[]
    for pos, aminoacid in enumerate(sequence_aa):
        sequence_aa_list.append(aminoacid + str(pos))
    data = [
        go.Bar(
            x=sequence_aa_list,
            y=sequence_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text= title,
                      xaxis=dict(
                          title= xaxis
                      ),
                      yaxis=dict(
                          title= yaxis
                      ))
    fig.show()
    return


def plot_sequence_bubble(sequence_aa, sequence_hydropathy, title="", xaxis="", yaxis=""):
    sequence_aa_list=[]
    for pos, aminoacid in enumerate(sequence_aa):
        sequence_aa_list.append(aminoacid + str(pos))

    pos_hydropathy = []
    for element in sequence_hydropathy:
        pos_hydropathy.append(10 * abs(element))
    data = [
        go.Scatter(
            x=sequence_aa_list,
            y=sequence_hydropathy,
            mode='markers',
            marker_size=pos_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text= title,
                      xaxis=dict(
                          title= xaxis
                      ),
                      yaxis=dict(
                          title= yaxis
                      ))
    fig.show()
    return


def sliding_window_hydropathy(sequence, mapping_dict, length):
    sequence_as_hydropathy_window = deque([], maxlen=length)
    averaged_hydropathy_list = []
    for pos, aa in enumerate(sequence):
        sequence_as_hydropathy_window.append(mapping_dict.get(sequence[pos]))
        if pos > len(sequence) + length:
            break
        average = sum(sequence_as_hydropathy_window)/len(sequence_as_hydropathy_window)
        averaged_hydropathy_list.append(average)
    return averaged_hydropathy_list


def plot_sequence_bar_window(len_window_list, sequence_hydropathy):
    sequence_aa_list=[]
    for x in range(len_window_list):
        sequence_aa_list.append(x)
    data = [
        go.Bar(
            x=sequence_aa_list,
            y=sequence_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title_text='Hydropathy Along G Protein Sequence',
                      xaxis=dict(
                          title='G Protein Sequence'
                      ),
                      yaxis=dict(
                          title='Hydropathy'
                      ))
    fig.show()
    return


def plot_bar(seq_aa=None, seq_hydropathy=list, title="", xaxis="", yaxis=""):
    if isinstance(seq_aa, str) == True:
        sequence_aa_list=[]
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
    fig.update_layout(title_text= title,
                      xaxis=dict(
                          title= xaxis
                      ),
                      yaxis=dict(
                          title= yaxis
                      ))
    fig.show()
    return


if __name__ == '__main__':
    seq = sequence_from_fasta("./P32249.fasta")
    mapping_dict = mapping_dict("../data/amino_acid_properties.csv")
    sequence_hydropathy = hydropathy_sequence_list(seq, mapping_dict)
    plot_bar(seq, seq_hydropathy=sequence_hydropathy, title="Hydropathy Along G Protein Sequence", xaxis="G Protein Sequence", yaxis="Hydropathy")
    window = sliding_window_hydropathy(seq, mapping_dict, 10)
    plot_bar(seq_hydropathy=window)
