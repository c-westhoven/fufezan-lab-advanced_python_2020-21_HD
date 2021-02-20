import pandas as pd
from collections import deque
import plotly.graph_objects as go


class Protein:
    def __init__(self, fasta, aa_csv, length, window_or_reg):
        self.fasta = fasta
        self.aa_csv = aa_csv
        self.length = length
        self.window_or_reg = window_or_reg
        self.combined_seq = None
        self.mapping_dict = None
        self.averaged_hydropathy_list = None
        self.hydropathy_list = None
        self.combined_seq = None


        # method get data (pulls sequence from uniprot given id)
        # method map --> accepts kwarp specify which lookup should be used to map the sequence against and return the value list
        # method plot
        # method sliding window

    # # get data
    # def get_data(self):
    #     # use self.fasta to get fasta file from online
    #     return  # fasta_file

    def sequence_from_fasta(self):
        with open(self.fasta) as f:
            combined_seq = ""
            for line_dict in f:
                if not line_dict.startswith(">"):
                    combined_seq += line_dict.replace("\n", "")
        self.combined_seq = combined_seq
        return combined_seq

    def create_mapping_dict(self):
        aa_df = pd.read_csv(self.aa_csv)
        hydropathy_df = pd.DataFrame.drop(aa_df, columns=["Name", "3-letter code", "Molecular Weight",
                                                          "Molecular Formula", "Residue Formula", "Residue Weight",
                                                          "pka1",
                                                          "pka2", "pkaX", "pI", "Accessible surface"], axis=1)
        hydropathy_df = hydropathy_df.rename(
            columns={"1-letter code": "aa", "hydropathy index (Kyte-Doolittle method)": "hydropathy"})
        mapping_dict = dict(zip(hydropathy_df.aa, hydropathy_df.hydropathy))
        self.mapping_dict = mapping_dict
        return mapping_dict

    def hydropathy_sequence_list(self, combined_seq, mapping_dict):
        """
        creates a list with hydropathy values corresponding to the sequence
        :param sequence: single sequence, str
        :param mapping_dict: mapping_dict with aminoacid: hydropathy
        :return:
        """
        hydropathy_list = []
        for pos, aminoacid in enumerate(combined_seq):
            hydropathy_list.append(mapping_dict.get(combined_seq[pos]))
        self.hydropathy_list = hydropathy_list
        return hydropathy_list

    def sliding_window_hydropathy(self, combined_seq, mapping_dict):
        """
        creates a sliding window along sequence, and calculates the average at each position
        :param sequence: aminoacid sequence, str
        :param mapping_dict: mapping dict
        :param length: length of window
        :return: list where each element represents the average of the window at a position
        """
        sequence_as_hydropathy_window = deque([], maxlen=self.length)
        averaged_hydropathy_list = []
        for pos, aa in enumerate(combined_seq):
            sequence_as_hydropathy_window.append(mapping_dict.get(combined_seq[pos]))
            if pos > len(combined_seq) + self.length:
                break
            average = sum(sequence_as_hydropathy_window) / len(sequence_as_hydropathy_window)
            averaged_hydropathy_list.append(average)
        self.averaged_hydropathy_list = averaged_hydropathy_list
        return averaged_hydropathy_list

    def create_plot_bar(self, title="", xaxis="", yaxis=""):
        """
        plots the sequence (x) against the corresponding values (ex. hydropathy) (y)
        :param seq_hydropathy: list with hydropathy values corresponding to amino acid sequence
        :param seq_aa: generally a string
        :param title: title of plot
        :param xaxis: xaxis label
        :param yaxis: yaxis label
        :return:
        """
        if self.window_or_reg == "window":
            sequence_aa_list = []
            for x in range(len(self.averaged_hydropathy_list)):
                sequence_aa_list.append(x)
            seq_hydropathy = self.averaged_hydropathy_list

        elif self.window_or_reg == "reg":
            if isinstance(self.hydropathy_list, str) == True:
                sequence_aa_list = []
                seq_hydropathy = self.hydropathy_list
                for pos, aminoacid in enumerate(self.combined_seq):
                    sequence_aa_list.append(aminoacid + str(pos))

            else:
                sequence_aa_list = self.combined_seq
                seq_hydropathy = self.hydropathy_list

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
    aa_df = pd.read_csv("../data/amino_acid_properties.csv")
    fasta = "../Day_3_Files/P32249.fasta"
    aa_csv = "../data/amino_acid_properties.csv"
    title1 = "Hydropathy Along G Protein Sequence",
    xaxis1 = "G Protein Sequence"
    yaxis1 = "Hydropathy"

    protein = Protein(fasta, aa_csv, 10, "window")
    seq = protein.sequence_from_fasta()
    mapping_dict = protein.create_mapping_dict()
    hydropathy_list = protein.hydropathy_sequence_list(seq, mapping_dict)
    window_list = protein.sliding_window_hydropathy(seq, mapping_dict)

    barplot = protein.create_plot_bar()