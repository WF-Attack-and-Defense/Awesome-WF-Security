import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "AwesomeWFS.csv",
    usecols=["Year", "Journal/Conference"],
    encoding="utf-8",
)

df = df.dropna(subset=["Year", "Journal/Conference"])
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df = df.dropna(subset=["Year"])

# Counts per Journal/Conference × Year (columns = years for legend)
ct = pd.crosstab(df["Journal/Conference"], df["Year"])
ct = ct.reindex(sorted(ct.columns), axis=1)
ct = ct.loc[ct.sum(axis=1).sort_values(ascending=True).index]

n_years = len(ct.columns)
if n_years <= 20:
    colors = plt.cm.tab20(np.linspace(0, 1, n_years))
else:
    colors = plt.cm.viridis(np.linspace(0, 1, n_years))

fig, ax = plt.subplots(figsize=(12, max(6, 0.35 * len(ct))))
ct.plot(
    kind="barh",
    stacked=True,
    ax=ax,
    color=colors,
    edgecolor="black",
    linewidth=0.2,
)

ax.set_title("Published Papers by Journal / Conference (stacked by year)", fontsize=16)
ax.set_xlabel("Number of papers", fontsize=12)
ax.set_ylabel("Journal / Conference", fontsize=12)
ax.grid(axis="x", linestyle="--", alpha=0.4)
ax.legend(title="Year", bbox_to_anchor=(1.02, 1), loc="upper left")

plt.tight_layout()
# plt.savefig("imgs/AwesomeWFS_by_venue.png", dpi=300, bbox_inches="tight")
plt.show()
