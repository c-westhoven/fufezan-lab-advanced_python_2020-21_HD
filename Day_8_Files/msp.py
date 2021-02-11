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

    with open(msp_file) as file:

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
        mz_int = []
        prefixes = ("M", "N", "C")
        for idx, value in enumerate(list_spectra):
            row_spectra = value.split("\n")
            row_spectra = [x for x in row_spectra if not x.startswith(prefixes)]    # list with mz and ints [mzint, mzint, mzint, ...]
            for idx, value in enumerate(row_spectra):
                mz_split = row_spectra[idx].split("\t")     # list [mz , int , blah]
                mz_val = round(float(mz_split[0]))
                int_val = round(float(mz_split[1]))
                if mz_val > mz_max or mz_val < mz_min:
                    continue
                else:
                    mz_int.append([mz_val, int_val])


    df = None
    return df, seqs


if __name__ == '__main__':
    msp_file = "./cptac2_mouse_hcd_selected.msp"
    df, seq = msp_to_df(msp_file)
    print(df, seq)

    # with open(msp_file) as file:
    #
    #     file = file.read()
    #     list_spectra = file.split("\n\n")
    #     list_spectra = list_spectra[:-1]
    #
    #     prefixes = ("M", "N", "C")
    #     for idx, value in enumerate(list_spectra):
    #         row_spectra = value.split("\n")
    #         row_spectra = [x for x in row_spectra if not x.startswith(prefixes)]
        #     for idx, value in enumerate(row_spectra):
        #         if not value[0] == "N":
        #             continue
        #         elif not value[0] == "M":
        #             continue
        #         elif not value[0] == "C":
        #             continue
        #         else:
        #             row_spectra.pop(idx)
        # print(row_spectra)

    # with open(msp_file) as file:
    #     file = file.read()
    #     list_spectra = file.split("\n\n")
    #     list_spectra = list_spectra[:-1]
    #     df_list = []
    #     max_seq_len = 30
    #     min_seq_len = 1
    #     min_ce = 36
    #     max_ce = 40
    #     for idx, value in enumerate(list_spectra):
    #         # value = list_spectra[idx]
    #         seq = value[value.find(" ")+1:value.find("/")]
    #         ce_split = value.split("\n")[0]
    #         ce_ev = ce_split.split("_")[-1]
    #         ce = float(ce_ev[:ce_ev.find("eV")])
    #         print(ce)
    #         if len(seq) > max_seq_len or ce > max_ce or min_ce > ce:
    #             list_spectra.pop(idx)
    #         else:
    #             df_list.append(seq)
    #             df_list.append(ce)
    #
    #
    # print(df_list, len(df_list))
