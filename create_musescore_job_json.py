"""
Script to generate a JSON file for a MuseScore job with the 
MSCZ files in the repository to be converted to PDF files
"""

import os
import json

def create_musescore_job_json():
    """
    Scans the 'scores' directory for MSCZ files and creates a JSON
    mapping each MSCZ file to its corresponding PDF output path.
    """
    data = []
    for root, _, files in os.walk('./scores'):
        for file in files:
            if file.endswith('.mscz'):
                file_path = os.path.join(root, file)
                out_path = file_path.replace('.mscz', '.pdf')
                data.append({"in": file_path, "out": out_path})

    with open('job.json', 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    create_musescore_job_json()