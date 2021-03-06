# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans, save_path):
    """Qualifying loans from find_qualifying_loans function.

    Args:
        save_path: The csv destination file path.
        If running from the main function, the arguments will be return values from save_qualifiying_loans(). 

    Returns:
        A CSV file of qualifying loans."""

    save_path = Path(save_path)
    
    header = "Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"

    with open(save_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        #write header row to CSV file
        csvwriter.writerow(header)
    
        #add each loan in qualifying loans list to CSV
        for loan in qualifying_loans:
            csvwriter.writerow(loan)