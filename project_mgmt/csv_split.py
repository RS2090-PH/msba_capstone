import pandas as pd
import sys
import os


def split_csv(input_file: str, output_prefix: str = "split"):
    """
    Splits a CSV file into two CSV files of approximately equal size by rows.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_prefix (str): Prefix for the output files (default: 'split').

    Returns:
        None
    """
    try:
        # Load the CSV into a DataFrame
        df = pd.read_csv(input_file)

        # Calculate the midpoint
        midpoint = len(df) // 2

        # Split into two DataFrames
        df1 = df.iloc[:midpoint]
        df2 = df.iloc[midpoint:]

        # Prepare output file names
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        file1 = f"{output_prefix}_0.csv"
        file2 = f"{output_prefix}_1.csv"

        # Save to new CSVs
        df1.to_csv(file1, index=False)
        df2.to_csv(file2, index=False)

        print(f"CSV successfully split into:\n  {file1}\n  {file2}")

    except Exception as e:
        print(f"Error while processing file: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_csv.py <input_file> [output_prefix]")
    else:
        input_file = sys.argv[1]
        output_prefix = sys.argv[2] if len(sys.argv) > 2 else "split"
        split_csv(input_file, output_prefix)
