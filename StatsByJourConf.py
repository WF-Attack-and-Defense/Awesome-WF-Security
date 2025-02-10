import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame from the given data
df = pd.read_csv('AwesomeWFS.csv', usecols=['Year', 'Journal/Conference', 'Category'], encoding='utf-8')

# Create a mapping for the category labels
category_labels = {
    0: 'WF Attack/Defense Measurement',
    1: 'WF Attacks',
    2: 'WF Defenses'
}

# Pivot the DataFrame to create a count of each category for each Journal/Conference and Year
pivot_df = df.pivot_table(index=['Journal/Conference', 'Year'], columns='Category', aggfunc='size', fill_value=0)

# Rename the columns with the descriptive labels
pivot_df = pivot_df.rename(columns=category_labels)

# Plot the stacked bar chart for each Journal/Conference
pivot_df.unstack(level=0).plot(kind='bar', stacked=True, figsize=(12, 7))

# Adding titles and labels
plt.title('Distribution of Categories by Journal/Conference and Year', fontsize=16)
plt.xlabel('Journal/Conference and Year', fontsize=12)
plt.ylabel('Count of Awesome Publications', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Custom legend with the new category names
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
