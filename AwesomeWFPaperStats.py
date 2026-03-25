import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame from the given data
df = pd.read_csv('AwesomeWFS.csv', usecols=['Year', 'Journal/Conference', 'Category'], encoding='utf-8')

# Normalize Category so isin([0,1,2]) matches CSV ints, floats, or strings (avoids empty df → plot crash)
df['Category'] = pd.to_numeric(df['Category'], errors='coerce')
df = df.dropna(subset=['Category'])
df['Category'] = df['Category'].astype(int)
# Only categories 0, 1, 2 — three colors in the figure
df = df[df['Category'].isin([0, 1, 2])]

category_labels = {
    0: 'WF Attack/Defense Measurement',
    1: 'WF Attacks',
    2: 'WF Defenses'
}

# Count each category per year (one bar per year, stacked)
counts = df.groupby(['Year', 'Category']).size().unstack(fill_value=0)
for c in (0, 1, 2):
    if c not in counts.columns:
        counts[c] = 0
counts = counts[[0, 1, 2]]
counts.columns = [category_labels[c] for c in (0, 1, 2)]

# Three distinct colors for the three series
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
ax = counts.plot(kind='bar', stacked=True, figsize=(12, 7), color=colors, width=0.8)

plt.title('Distribution of Categories by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Count of Awesome Publications', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
# plt.savefig('imgs/AwesomeWFS.png', dpi=800)
plt.show()

