import csv
import os


# Variables
ALLOWED_EXTENSIONS = set(['csv'])
UPLOAD_FOLDER = 'uploads'


# Check that uploaded file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# Make string from csv header
def create_query_by_header(file):
    query_start = 'CREATE TABLE RawData_' + file.rsplit('.', 1)[0] + ' ("RawData_Key" INTEGER PRIMARY KEY'
    with open(os.path.join(UPLOAD_FOLDER, file), 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        field_names = reader.fieldnames
        for field in field_names:
            query_start = query_start + ', ' + '"{}"'.format(field) + ' TEXT'
        csv_file.close()
    query_end = ');'
    query = query_start + query_end
    return query


# Save uploaded file to the upload folder
def path_to_upload_folder(file):
    upload_path = os.path.join(UPLOAD_FOLDER, file)
    return upload_path


# Delete uploaded file from the upload folder
def delete_from_upload_folder(file_name):
    os.remove(os.path.join(UPLOAD_FOLDER, file_name))


# Count how many rows csv file has except header
def count_rows(file):
    count = -1
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            count += 1
    return count
