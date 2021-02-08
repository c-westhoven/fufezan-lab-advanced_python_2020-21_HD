import csv
from collections import Counter, OrderedDict


# make it into functions
def csv_from_fasta(fastafile, name_of_org):
    with open(fastafile) as aap:
        combined_seq = ""
        for line_dict in aap:
            if not line_dict.startswith(">"):
                combined_seq += line_dict.replace("\n", "")
    counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

    aminoacid_key_list = list(counted_seq.keys())
    count_list = list(counted_seq.values())

    with open("../Results_Ex_2/" + str(name_of_org) + ".csv", "w") as output:
        aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
        aap_writer.writeheader()
        for pos, element in enumerate(aminoacid_key_list):
            aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})
    return


if __name__ == '__main__':
    lion = csv_from_fasta("../uniprot_Panthera_leo_Lion.fasta", "lion")
    eggplant = csv_from_fasta("../uniprot_Solanum_melongena_Eggplant.fasta", "eggplant")
    human = csv_from_fasta("../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta", "human")
    bacillus = csv_from_fasta("../uniprot_bacillus_subtilis.fasta", "bacillus")
    archaea = csv_from_fasta("../uniprot_Haloquadratum_walsbyi.fasta", "archaea")
