import csv
import os
import urllib.request, json
from src.components.update_packages import update_packages
from src.components.view_builder import view_builder

# Function to help verify if the dependency is up to date or not
def verify(file_location, dependency, version, update):

    # Converting CSV file to JSON Data for easier access.
    json_data = {}
    with open(file_location, "r") as file:
        csvreader = csv.reader(file)
        next(file)
        i = 1
        for rows in csvreader:
            json_data[f"obj_{i}"] = [rows[0], rows[1]]
            i += 1

    # Obtain the version of the dependency from the Package.json file and adding it to JSON data.
    for obj in json_data:
        repo_url = json_data[obj][1].replace("https://github.com/", "")
        pkj_url = f"https://raw.githubusercontent.com/{repo_url}/master/package.json"
        with urllib.request.urlopen(pkj_url) as url:
            data = json.loads(url.read().decode())
            try:  # To handle the different formats.
                all_dependencies = data["packages"]["dependencies"]
            except:
                all_dependencies = data["dependencies"]

        # Check if dependency version is greater than or equal to the provided version.
        if dependency in all_dependencies:
            json_data[obj].append(all_dependencies[dependency].replace("^", ""))
            if json_data[obj][2] >= version:
                json_data[obj].append("true")
            else:
                json_data[obj].append("false")
        else:
            json_data[obj].append("NULL", "false")

    # Check if update is needed, if yes, update, else build the view for front-end.
    if update == True:
        json_data = update_packages(json_data, dependency, version)
    os.remove(file_location)
    try:
        return view_builder(json_data, update)  # Build the view for front-end.
    except:
        return json_data
