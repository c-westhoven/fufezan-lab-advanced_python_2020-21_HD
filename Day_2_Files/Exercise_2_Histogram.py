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
plt.savefig("../Results_Ex_2/Human_Westhoven.pdf")

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
plt.savefig("../Results_Ex_2/B_Subtilis_Westhoven.pdf")

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
plt.savefig("../Results_Ex_2/Archaea_Westhoven.pdf")

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
plt.savefig("../Results_Ex_2/Eggplant_Westhoven.pdf")

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
plt.savefig("../Results_Ex_2/Lion_Westhoven.pdf")

# as a function
def make_histogram_from_fasta(fasta_file, name_of_organism):
    with open(fasta_file) as aap:
        combined_seq = ""
        for line_dict in aap:
            if not line_dict.startswith(">"):
                combined_seq += line_dict.replace("\n", "")
    counted_seq = dict(Counter(combined_seq))

    plt.xlabel("aa")
    plt.ylabel("counts")
    plt. title(str(name_of_organism))
    plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
    plt.savefig("../Results_Ex_2/" + str(name_of_organism)+ ".pdf")

if __name__ == '__main__':
    lion = make_histogram_from_fasta("../uniprot_Panthera_leo_Lion.fasta", "lion")
    eggplant = make_histogram_from_fasta("../uniprot_Solanum_melongena_Eggplant.fasta", "eggplant")
    human = make_histogram_from_fasta("../uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta", "human")
    bacillus = make_histogram_from_fasta("../uniprot_bacillus_subtilis.fasta", "bacillus")
    archaea = make_histogram_from_fasta("../uniprot_Haloquadratum_walsbyi.fasta", "archaea")