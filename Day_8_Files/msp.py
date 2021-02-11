import numpy as np
import pandas as pd
import timeit


def msp_to_df(
    input_file,
    max_seq_len=30,
    min_ce=36,
    max_ce=40,
    mz_min=135,
    mz_max=1400,
):
    """
    Function to read spectrum data from .msp file and convert to dataframe.
    Args:
        input_file (str): path to .msp file
        max_seq_len (int): maximum acceptable sequence length
        min_ce (int): minimum collision energy of spectra to be included in df
        max_ce (int): maximum collision energy of spectra to be included in df
        mz_min (int): lower boundary for m/z to be included in df
        mz_max (int): upper boundary for m/z to be included in df

    Returns:
        df (pd.DataFrame or np.array): spectrum information within defined parameters [n_spectra, n_features]
        seqs (pd.DataFrame or np.array): sequences
    """

    with open(input_file) as file:

        file = file.read()
        list_spectra = file.split("\n\n")
        list_spectra = list_spectra[:-1]
        seq_list = []

        for idx, value in enumerate(list_spectra):
            seq = value[value.find(" ")+1:value.find("/")]
            ce_split = value.split("\n")[0]
            ce_ev = ce_split.split("_")[-1]
            ce = float(ce_ev[:ce_ev.find("eV")])
            if len(seq) > max_seq_len or ce > max_ce or min_ce > ce:
                list_spectra.pop(idx)
            else:
                seq_list.append(seq)

        seqs = pd.DataFrame()
        seqs["seq"] = seq_list

        dict = {}   # empty dict
        prefixes = ("M", "N", "C")
        for idx_sequence, value in enumerate(list_spectra):
            row_spectra = value.split("\n")
            row_spectra = [x for x in row_spectra if not x.startswith(prefixes)]    # list with mz and ints [mzintblah, mzintblah, mzintblah, ...]
            dict[idx_sequence] = {}
            for idx, value in enumerate(row_spectra):
                mz_split = row_spectra[idx].split("\t")     # list [mz , int , blah]
                mz_val = round(float(mz_split[0]))      # rounded mz
                int_val = float(mz_split[1])     # unrounded intensity
                if mz_val > mz_max or mz_val < mz_min:
                    continue
                elif mz_val in dict[idx_sequence].keys():
                    if int_val > dict[idx_sequence][mz_val]:
                        dict[idx_sequence][mz_val] = int_val
                else:
                    dict[idx_sequence][mz_val] = int_val

    df = pd.DataFrame(dict).T
    return df, seqs


if __name__ == '__main__':
    msp_file = "./cptac2_mouse_hcd_selected.msp"
    df, seq = msp_to_df(msp_file)
    # print(df, seq)
    print(timeit.timeit("msp_to_df()", setup="from __main__ import msp_to_df"))

