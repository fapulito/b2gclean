# MUST add GCP KEY use gitignore. Directory name will depend on your device.

import os
import requests

import google.generativeai as genai



GOOGLE_API_KEY = " ADD API KEY "
genai.configure(api_key=GOOGLE_API_KEY)

# Define the directory and URL
directory = '/home/USER/unihiker/'
# url = 'https://example.com/upload'

# Get the list of files in the directory
files = os.listdir(directory)

# Ensure there are files in the directory
if files:
    # Get the first file
    # first_file = files[0]
    # file_path = os.path.join(directory, first_file)
    file_path = os.listdir(directory)[0]

    # Open the file and upload it
    sample_file = genai.upload_file(path=file_path, display_name="Gemini Sample")
    

    # with open(file_path, 'rb') as f:
    #    response = requests.post(url, files={'file': f})

    # Print the response from the server
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    #print(response.text)
else:
    print("No files found in the directory.")
