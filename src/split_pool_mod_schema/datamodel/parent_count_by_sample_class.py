import pandas as pd

# Read the TSV file into a DataFrame
df = pd.read_csv('parent_count_by_sample_class.tsv', sep='\t')

print(df)

# Create a pivot table with sampleClass for rows, parent_count as columns, and the count of rows as cell contents
# pivot_table = pd.pivot_table(
#     df,
#     values='parent_count',
#     index=['sampleClass'],
#     columns=['parent_count'],
#     aggfunc='count', fill_value=0
# )

pivot_table = pd.pivot_table(
    df,
    values='parent_count',
    index=['sampleClass'],
    columns=['parent_count'],
    aggfunc='count'
)

# # Print the pivot table
# print(pivot_table)
