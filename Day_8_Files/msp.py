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

        df_list = []
        for line in file:
            if line.startswith("Name: "):
                line = line.replace(str(line[line.index("/"):]), "")
                df_list.append(line.replace("Name: ", ""))
            for line in file:
                if line.endswith("eV"):
                    line = line.replace(str(line[:line.index("_", -1)]), "")
                    df_list.append(line.replace("eV", ""))
    print(df_list)


    df = pd.DataFrame(df_list, columns=["sequence", "ce", "mz", "intensity"])

    df = None
    seqs = None

    return df, seqs


if __name__ == '__main__':
    msp_file = "./cptac2_mouse_hcd_selected.msp"

    # with open(msp_file) as file:
    #     df_list = []
    #     for nameline in file:
    #         if nameline.startswith("Name: "):
    #             nameline = nameline.replace(str(nameline[nameline.index("/"):]), "")
    #             df_list.append(nameline.replace("Name: ", ""))
    #     for celine in file:
    #         if celine.endswith("eV\n"):
    #             celine = celine.replace(str(celine[:celine.rfind("_")+1]), "")
    #             df_list.append(celine.replace("eV\n", ""))
    # print(df_list)

    with open(msp_file) as file:
        file = file.read()
        list_spectra = file.split("\n\n")
        list_spectra = list_spectra[:-1]
        df_list = []
        max_seq_len = 30
        min_seq_len = 1
        min_ce = 36
        max_ce = 40
        for idx, value in enumerate(list_spectra):
            # value = list_spectra[idx]
            seq = value[value.find(" ")+1:value.find("/")]
            if len(seq) > max_seq_len or len(seq) < min_seq_len:
                list_spectra.pop(idx)
            else:
                df_list.append(seq)

            ce_split = value.split("\n")[0]
            ce_ev = ce_split.split("_")[-1]
            ce = float(ce_ev[:ce_ev.find("eV")])
            print(ce)
            if not max_ce > ce > min_ce:
                list_spectra.pop(idx)
            else:
                df_list.append(ce)

    print(df_list, len(df_list))
