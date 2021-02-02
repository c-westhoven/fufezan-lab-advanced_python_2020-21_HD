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
print(counted_seq)

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

print("human", aminoacid_key_list)
print("human", count_list)

with open("../human.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"])
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
print(counted_seq)

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

print("bacillus", aminoacid_key_list)
print("bacillus", count_list)

with open("../bacillus.csv", "w") as output:
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

print("archaea", aminoacid_key_list)
print("archaea", count_list)

with open("../archaea.csv", "w") as output:
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

print("eggplant", aminoacid_key_list)
print("eggplant", count_list)

with open("../eggplant.csv", "w") as output:
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

print("lion", aminoacid_key_list)
print("lion", count_list)

with open("../lion.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], "count": count_list[pos]})