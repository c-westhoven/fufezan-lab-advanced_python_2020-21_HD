import csv
from collections import Counter

data = "../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = Counter(combined_seq)
print(counted_seq)
print(type(counted_seq))
aminoacid_key_list = counted_seq.keys()
count_list = counted_seq.values()
print(aminoacid_key_list)
print(count_list)
with open("../test.csv", "w") as output:
    aap_writer = csv.DictWriter(output, fieldnames=["aa", "count"], extrasaction='ignore')
    aap_writer.writeheader()
    for element in count_list:
        aap_writer.writerow({"aa": aminoacid_key_list[element], " count": count_list[element]})

