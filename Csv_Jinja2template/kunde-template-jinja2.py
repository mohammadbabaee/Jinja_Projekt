import csv
from jinja2 import Template
source_file = "csv_example_jinja2.csv"
template_file = "kunde-template.j2"
kunde_infos = ""

with open(template_file) as f:
    temp_template = Template(f.read())

with open(source_file) as f:
    reader = csv.DictReader(f, delimiter = ";")
    for row in reader:
        kunde_info = temp_template.render(
        Kundename = row["Kundename"],
        location = row["Standort"],
        ipAdresse = row ["IP"],
        status = row ["Status"]
        )
        kunde_infos += kunde_info

#print(kunde_infos)

with open("kunde_infos.txt", "w") as f:
    f.write(kunde_infos)
