import csv
def load_data(file_path):

    with open(file_path, "r", encoding="utf-8-sig", newline="") as csv_file:
        return list(csv.DictReader(csv_file))