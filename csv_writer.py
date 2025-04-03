import csv
import os

def get_unique_filename(base_filename='output.csv'):
    """
    Generates a unique filename by appending a number if the file already exists.

    Parameters:
    - base_filename (str): The desired filename.

    Returns:
    - str: A unique filename.
    """
    if not os.path.exists(base_filename):
        return base_filename

    filename, extension = os.path.splitext(base_filename)
    counter = 1
    new_filename = f"{filename}_{counter}{extension}"

    while os.path.exists(new_filename):
        counter += 1
        new_filename = f"{filename}_{counter}{extension}"

    return new_filename

def write_to_csv(data, filename='output.csv'):
    """
    Writes a list of dictionaries to a CSV file, ensuring no overwrite of existing files.

    Parameters:
    - data (list of dict): The data to write to the CSV file.
    - filename (str): The base name of the CSV file. Default is 'output.csv'.
    """
    if not data:
        print("No data to write.")
        return

    unique_filename = get_unique_filename(filename)
    headers = data[0].keys()

    try:
        with open(unique_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully written to {unique_filename}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
