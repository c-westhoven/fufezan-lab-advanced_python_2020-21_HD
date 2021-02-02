import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd

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

plt.bar(list(counted_seq.keys()), list(counted_seq.values()))
plt.show()
plt.savefig("human.pdf")