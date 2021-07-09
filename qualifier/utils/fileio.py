# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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

def save_csv(output_path, data):
    """Saves the list of loans to the local machine as a .csv file
    
    Args:
        output_path: The location where the user would like to save the list of accepted loans.
        data: The qualifying loans from the find_qualifying_loans function. Added automatically in the main app.
    
    Return: Saves the info.
    
    """

    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    with open(output_path, "w") as new_csv_file:
        
        csvwriter = csv.writer(new_csv_file, delimiter = ",")
        csvwriter.writerow(header)
        for row in data:
            csvwriter.writerow(row)
    return True
