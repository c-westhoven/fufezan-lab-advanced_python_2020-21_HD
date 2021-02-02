import csv
from collections import Counter, OrderedDict

#human
data = "../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
# counted_seq = dict(Counter(combined_seq))
counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

with open("../Results_Ex_2/human.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], delimiter=",", quotechar=" ", quoting=csv.QUOTE_ALL)
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})

# bacillus subtilis
data = "../uniprot_bacillus_subtilis.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())


with open("../Results_Ex_2/bacillus.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})

# archea
data = "../uniprot_Haloquadratum_walsbyi.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

with open("../Results_Ex_2/archaea.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})

# plantae (eggplant)
data = "../uniprot_Solanum_melongena_Eggplant.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

with open("../Results_Ex_2/eggplant.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})


# animalia (lion)
data = "../uniprot_Panthera_leo_Lion.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = OrderedDict(sorted(dict.items(Counter(combined_seq))))

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

with open("../Results_Ex_2/lion.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})