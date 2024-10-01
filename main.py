from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Directory dove salvare i file caricati
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/app/image', methods=['POST'])
def upload_image_and_json():
    print("Request is on!")
    # Verifica che la richiesta contenga multipart/form-data
    if 'image' not in request.files or 'data' not in request.form:
        return jsonify({"error": "Image and data fields are required."}), 400

    file_image = request.files['image']
    json_data = request.form['data']

    # Salva il file sul filesystem locale
    if file_image.filename == '':
        return jsonify({"error": "No file selected."}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file_image.filename)
    file_image.save(file_path)

    # Salva il JSON sul filesystem locale
    try:
        json_object = json.loads(json_data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format."}), 400

    json_path = os.path.join(UPLOAD_FOLDER, 'data.json')
    with open(json_path, 'w') as json_file:
        json.dump(json_object, json_file, indent=4)

    return jsonify({
        "message": "File and JSON saved successfully.",
        "file_path": file_path,
        "json_path": json_path
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
