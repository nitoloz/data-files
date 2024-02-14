import csv

def export_to_csv(data, file_name):
    field_names = data[0].keys()
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
