import csv
from collections import Counter

data = "../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))
print(counted_seq)

aminoacid_key_list = list(counted_seq.keys())
count_list = list(counted_seq.values())

print(aminoacid_key_list)
print(count_list)

with open("../human.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for pos, element in enumerate(aminoacid_key_list):
        aap_writer.writerow({"aa": aminoacid_key_list[pos], " count": count_list[pos]})


