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
        mz = []
        for idx, value in enumerate(list_spectra):
            row_spectra = value.split("\n")
            for idx, value in row_spectra:
                if value.startswith("N") or value.startswith("M") or value.startswith("C"):
                    row_spectra.pop(idx)
            # if value.startswith("N") or value.startswith("M") or value.startswith("C"):
            #     row_spectra.pop(idx)
                    mz_split = row_spectra.split("\t")
                    for idx, value in enumerate(mz_split):
                        mz_int = mz_split[idx]
                        mz_val = mz_int[mz_int.rfind("\n")+1:]
                        print("val", mz_val)
                        mz.append(mz_val)
        print("list", mz)

    df = None
    return df, seqs



if __name__ == '__main__':
    msp_file = "./cptac2_mouse_hcd_selected.msp"
    df, seq = msp_to_df(msp_file)
    print(df, seq)

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
