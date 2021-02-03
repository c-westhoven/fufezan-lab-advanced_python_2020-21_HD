import plotly
import plotly.graph_objects as go
import pandas as pd

# aa_df = pd.read_csv("../data/amino_acid_properties.csv")
# print(type(aa_df))
#



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
    for pos, aminoacid in enumerate(sequence):         #check
        sequence_as_hydropathy.append(mapping_dict.get(sequence[pos]))
    return sequence_as_hydropathy


def plot_sequence(sequence_aa, sequence_hydropathy):
    sequence_aa_list=[]
    for pos, aminoacid in enumerate(sequence_aa):
        sequence_aa_list.append(aminoacid)
    data = [
        go.Bar(
            x=sequence_aa_list,
            y=sequence_hydropathy
        )
    ]
    fig = go.Figure(data=data)
    fig.show()
    return


if __name__ == '__main__':
    sequence = sequence_from_fasta("./P32249.fasta")
    mapping_dict = mapping_dict("../data/amino_acid_properties.csv")
    sequence_hydropathy = hydropathy_sequence_list(sequence, mapping_dict)
    plot_sequence(sequence, sequence_hydropathy)


