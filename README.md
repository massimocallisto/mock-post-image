# Flask File and JSON Upload API

This project is a simple Flask REST API that allows clients to upload both a file and JSON data via a `multipart/form-data` POST request. The uploaded file and JSON data are saved to the local filesystem.

## Project Description

- **Endpoint**: `/app/image`
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Data**: 
  - A file under the `image` key
  - A JSON string under the `data` key
- **Response**: A JSON response with the status of the upload and the paths where the file and JSON were saved.

## Requirements

To run this project, you need the following:

- Docker
- Python 3.x (for local execution)
- Flask (if running locally outside of Docker)

## How to Build the Image Locally

First, clone this repository and navigate to the project directory.

To build the Docker image locally, run the following command:

```bash
docker build -t massimocallisto/flask-upload-api:1.0.0 .
```

## How to Run
You can run the API either using a Python virtual environment or using Docker.

Running Locally (Without Docker)
* Install Python 3.x and Flask.
* Install the dependencies 

 ```bash
pip install -r requirements.txt
python app.py
```

By default, Flask will run on port 5000. You can access the API at http://127.0.0.1:3000/app/image.

## Running with Docker
Once the image is built, you can run it with Docker using the following command:

```bash
docker run -p 3000:3000 massimocallisto/flask-upload-api:1.0.0
```

If you want to mount an existing directory, create first in your file systems. E.g..: 

 ```bash
mkdir data-uploads
```

Then use:
```bash
docker run -p 3000:3000  -v "./data-uploads:/app/uploads" massimocallisto/flask-upload-api:1.0.0
```


This will map the container's port 3000 to your local machine's port 3000. You can access the API at http://127.0.0.1:3000/app/image.

## Sample POST Request
To test the API, you can use curl to send a POST request with both a file and JSON data.

```
curl -X POST http://127.0.0.1:3000/app/image \
  -F "file=@path_to_your_image/image.jpg" \
  -F 'json_data={"name": "Sample", "type": "Test"}'
```

## Notes
This API saves the uploaded file and the JSON data to the uploads directory in the container.
Ensure that the file and JSON data are correctly passed as multipart/form-data in your POST requests.
