import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd

# human
data = "../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))

# df = pd.DataFrame({k: [v] for k, v in counted_seq.items()}).sort_values(by=0, axis=1)
# ax = sns.barplot(x="aa", y="count", data=df)
# plt.show()
plt.xlabel("aa")
plt.ylabel("counts")
plt. title("human")
plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("Human_Westhoven.pdf")

# bacteria (B. subtilis)
data = "../uniprot_bacillus_subtilis.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))

plt.xlabel("aa")
plt.ylabel("counts")
plt. title("B. subtilis")
plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("B_Subtilis_Westhoven.pdf")

# archea
data = "../uniprot_Haloquadratum_walsbyi.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))

plt.xlabel("aa")
plt.ylabel("counts")
plt. title("Archaea")
plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("Archaea_Westhoven.pdf")

# plantae (eggplant)
data = "../uniprot_Solanum_melongena_Eggplant.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))

plt.xlabel("aa")
plt.ylabel("counts")
plt. title("Eggplant")
plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("Eggplant_Westhoven.pdf")

# animalia (lion)
data = "../uniprot_Panthera_leo_Lion.fasta"
with open(data) as aap:
    combined_seq = ""
    for line_dict in aap:
        if not line_dict.startswith(">"):
            combined_seq += line_dict.replace("\n", "")
counted_seq = dict(Counter(combined_seq))

plt.xlabel("aa")
plt.ylabel("counts")
plt. title("Lion")
plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("Lion_Westhoven.pdf")
