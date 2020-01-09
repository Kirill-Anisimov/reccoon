from flask import Flask, render_template, request, redirect, url_for
import model
import service
from werkzeug.utils import secure_filename


app = Flask(__name__)


# Create database and mandatory tables
model.create_db()
model.create_table_file_names()


@app.route('/')
def index():
    file_names = model.list_uploaded_file_names()
    return render_template('index.html', file_names=file_names)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and service.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(service.path_to_upload_folder(filename))

        model.save_file_name(filename)
        model.create_random_table(service.create_query_by_header(filename))
        # Insert file content into relevant table

        service.delete_from_upload_folder(filename)
    return redirect(url_for('index'))


@app.route('/raw-data/<filename>')
def display_raw_data(filename):
    result = model.select_my_filename(filename)
    return render_template('raw-data.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
