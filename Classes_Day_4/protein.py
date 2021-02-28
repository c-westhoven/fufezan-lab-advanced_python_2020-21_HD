import pandas as pd
from collections import deque
import plotly.graph_objects as go


class Protein:
    def __init__(self, fasta, aa_csv, lookup):
        """

        :param fasta: fasta file in directory
        :param aa_csv: amino acid property file in directory
        :param lookup: hydropathy, or another amino acid property
        :param length: length of sliding window
        :param window_or_reg: sliding window "window" or now sliding window "reg"
        """
        self.fasta = fasta
        self.aa_csv = aa_csv
        self.lookup = lookup
        self.length = None

        self.combined_seq = None
        self.mapping_dict = None
        self.averaged_hydropathy_list = None
        self.lookup_list = None
        self.combined_seq = None
        self.sequence_aa_list = None

    def get_data(self):
        """
        gets data from fasta file and puts sequence together
        :return: combined_seq, str of the sequence from file
        """
        with open(self.fasta) as f:
            combined_seq = ""
            for line_dict in f:
                if not line_dict.startswith(">"):
                    combined_seq += line_dict.replace("\n", "")
        self.combined_seq = combined_seq
        return combined_seq

    def create_mapping_dict(self):
        """
        creates a mapping dict for lookup/property of choice when initializing class
        :return:
        """
        # lookup = {
        # "hydropathy": {"A" : "..."},
        # "pI": {"A": "..."},

        aa_df = pd.read_csv(self.aa_csv)
        aa_df = aa_df.rename(
            columns={"1-letter code": "aa", "hydropathy index (Kyte-Doolittle method)": "hydropathy"})
        aa_df = aa_df.drop(["pkaX"], axis=1)

        mapping_dict = {}
        # add to dict with aa_dict["key"] = "value
        for aa_property in list(aa_df.columns):
            mapping_dict[aa_property] = {}
            for idx, lettercode in enumerate(list(aa_df.aa.values)):
                if aa_df.loc[idx, aa_property] == None:
                    pass
                else:
                    mapping_dict[aa_property][lettercode] = aa_df.loc[idx, aa_property]

        self.mapping_dict = mapping_dict
        return mapping_dict

    def hydropathy_sequence_list(self, combined_seq, mapping_dict):
        """
        creates a list with property values corresponding to the sequence
        :param combined_seq: single sequence, str
        :param mapping_dict: mapping_dict with aminoacid: hydropathy
        :return: lookup list of property values to sequence
        """
        lookup_list = []
        for pos, aminoacid in enumerate(combined_seq):
            lookup_list.append(mapping_dict[self.lookup].get(combined_seq[pos]))
        self.lookup_list = lookup_list
        return lookup_list

    def sliding_window(self, combined_seq, mapping_dict, length):
        """
        creates a sliding window along sequence, and calculates the average at each position
        :param combined_seq: aminoacid sequence, str
        :param mapping_dict: mapping dict
        :return: list where each element represents the average of the window at a position
        """

        sequence_as_hydropathy_window = deque([], maxlen=length)
        self.length = length
        averaged_hydropathy_list = []
        for pos, aa in enumerate(combined_seq):
            sequence_as_hydropathy_window.append(mapping_dict[self.lookup].get(combined_seq[pos]))
            if pos > len(combined_seq) + self.length:
                break
            average = sum(sequence_as_hydropathy_window) / len(sequence_as_hydropathy_window)
            averaged_hydropathy_list.append(average)
        self.averaged_hydropathy_list = averaged_hydropathy_list

        return averaged_hydropathy_list

    def create_plot_bar(self, title="", xaxis="", yaxis="", window_or_reg=""):
        """
        plots the sequence (x) against the corresponding values (ex. hydropathy) (y)
        :param title: title of plot
        :param xaxis: xaxis label
        :param yaxis: yaxis label
        :return:
        """
        if window_or_reg == "window":
            sequence_aa_list = []
            self.sequence_aa_list = sequence_aa_list
            for x in range(len(self.averaged_hydropathy_list)):
                sequence_aa_list.append(x)
            seq_hydropathy = self.averaged_hydropathy_list

        elif window_or_reg == "reg":
            if isinstance(self.combined_seq, str) == True:
                sequence_aa_list = []
                self.sequence_aa_list = sequence_aa_list
                seq_hydropathy = self.lookup_list
                for pos, aminoacid in enumerate(self.combined_seq):
                    sequence_aa_list.append(aminoacid + str(pos))

            else:
                sequence_aa_list = self.combined_seq
                seq_hydropathy = self.lookup_list
        else:
            print("Something went wrong here")

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
        # fig.show()
        return fig


if __name__ == '__main__':
    aa_df = pd.read_csv("../data/amino_acid_properties.csv")
    fasta = "../Day_3_Files/P32249.fasta"
    aa_csv = "../data/amino_acid_properties.csv"
    lookup = "hydropathy"
    title1 = "Hydropathy Along G Protein Sequence"
    xaxis1 = "G Protein Sequence"
    yaxis1 = "Hydropathy"
    window_size = 10
    window_or_reg = "reg"

    protein = Protein(fasta, aa_csv, lookup)
    seq = protein.get_data()
    mapping_dict = protein.create_mapping_dict()
    hydropathy_list = protein.hydropathy_sequence_list(seq, mapping_dict)
    window_list = protein.sliding_window(seq, mapping_dict, window_size)

    barplot = protein.create_plot_bar(title1, xaxis1, yaxis1, window_or_reg)
