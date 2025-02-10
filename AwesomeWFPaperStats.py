import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('AwesomeWFS.csv', usecols=['Year', 'Journal/Conference', 'Category'], encoding='utf-8')

# Pivot the DataFrame to create a count of each category for each year
pivot_df = df.pivot_table(index='Year', columns='Category', aggfunc='size', fill_value=0)

# Create a mapping for the category labels
category_labels = {
    0: 'WF Attack/Defense Measurement',
    1: 'WF Attacks',
    2: 'WF Defenses'
}

# Update the column names (Category labels)
pivot_df = pivot_df.rename(columns=category_labels)

# Plot a stacked bar chart
pivot_df.plot(kind='bar', stacked=True, figsize=(10, 7))



# Adding titles and labels
plt.title('Distribution of Awesome Publications by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Awesome Publications', fontsize=12)
plt.xticks(rotation=45)
#plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')

# Custom legend with the new category names
plt.legend(title="Category", loc='upper left')

# Show the plot
plt.tight_layout()
#plt.savefig('imgs/AwesomeWFPaperStats.png', dpi=800)
plt.show()
