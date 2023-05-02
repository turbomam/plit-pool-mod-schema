# import os
#
# rootdir = "/Users/MAM/Downloads/NEON_seq-metagenomic-microbe-soil"
#
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         filepath = os.path.join(subdir, file)
#         print(filepath)

import os
import pandas as pd

rootdir = "/Users/MAM/Downloads/NEON_seq-metagenomic-microbe-soil"
file_substrings = ["mms_metagenomeDnaExtraction", "mms_metagenomeSequencing", "mms_rawDataFiles"]

for substr in file_substrings:
    print("Processing files containing the substring: " + substr)
    # Find all filenames containing the substring
    filepaths = []
    for subdir, dirs, files in os.walk(rootdir):
        print(subdir)
        for file in files:
            print(file)
            if substr in file:
                print(f"{file} contains {substr}")
                filepath = os.path.join(subdir, file)
                filepaths.append(filepath)

    # Combine all CSV files into a single DataFrame
    df_list = []
    for filepath in filepaths:
        print(filepath)
        df = pd.read_csv(filepath)
        df_list.append(df)

    combined_df = pd.concat(df_list, axis=0, ignore_index=True)

    # Determine the output filename based on the substring
    output_file = substr + ".csv"
    print("Writing combined DataFrame to: " + output_file)
    output_path = os.path.join(rootdir, output_file)

    # Write the combined DataFrame to a CSV file
    combined_df.to_csv(output_path, index=False)
