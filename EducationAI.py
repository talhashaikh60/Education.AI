import csv
import requests 
import json

def send_json_to_couchdb(json_file_path):
    # Open the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    username = "talhashaikh60"
    password = "Tasuhu60"
    database = "students"
    couchdb_url = "localhost:5984"
    full_url = f"http://{username}:{password}@{couchdb_url}/{database}" 
    hs={"Content-Type": "multipart/form-data",
        "Accept": "application/json",
        "referer": "http://localhost:5984/ui/"
        }
    for key in data:
        # Add the document ID to the data
        print(data[key])
        # Send the data to CouchDB
        response = requests.put(f"{full_url}/{key}", data=json.dumps(data[key]), headers=hs)
        print(response.text)


def csv_to_json(csv_file_path, json_file_path):
    # Create a dictionary
    data = {}

    # Open the CSV
    with open(csv_file_path, mode='r') as infile:
        # Read the CSV data
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            # Assuming the column to be named 'First name'
            key = row['ID']
            data[key] = row

    # Open the JSON writer, and use the json.dumps() 
    # function to dump data
    with open(json_file_path, mode='w') as json_file:
        json_file.write(json.dumps(data, indent=4))

# Call the csv_to_json function
#csv_to_json("Students.csv", "output.json")
send_json_to_couchdb("output.json")
