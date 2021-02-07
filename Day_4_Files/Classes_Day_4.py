import pandas as pd


class Protein:
    def __init__(self, fasta):
        self.fasta = fasta
        self.fasta_file = None
        self.combined_seq = None
        # method get data (pulls sequence from uniprot given id)
        # method map --> accepts kwarp specify which lookup should be used to map the sequence against and return the value list
        # method plot
        # method sliding window

    # get data
    def get_data(self):
        # use self.fasta to get fasta file from online
        return # fasta_file

    def sequence_from_fasta(self):
        with open(self.fasta_file) as f:
            combined_seq = ""
            for line_dict in f:
                if not line_dict.startswith(">"):
                    combined_seq += line_dict.replace("\n", "")
        self.combined_seq = combined_seq
        return combined_seq

    def mapping_dict(self, csv):
        return


if __name__ == '__main__':
    aa_df = pd.read_csv("../data/amino_acid_properties.csv")
    print(aa_df)
    aa_df1 = aa_df.pivot_table(index = "1-letter code")
    print(aa_df1)
    # aa_df2 = aa_df1.T
    # aa_df3 = aa_df.T
    # print(aa_df3)

    # aa_df2.groupby("1-letter code")[['A','C','D','E', 'F', 'G', 'H', 'I', 'K', 'L','M','N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']].to_dict()
    # print(aa_df2)
    # dict = {k: aa_df1.groupby('1-letter code')['Molecular Weight','Molecular Formula','Residue Formula',
    #                                            'Residue Weight','pka1','pka2','pkaX','pI','hydropathy index (Kyte-Doolittle method)',
    #                                            'Accessible surface'].apply(list).to_dict() for k, f in }
    # d = {k: f.groupby('subgroup')['selectedCol'].apply(list).to_dict()
    #      for k, f in df.groupby('maingroup')}

    # {"hydropathy": {"A" : "...", "B" : "..."},
    #  "pI": {"A": "...", "B": "..."}}