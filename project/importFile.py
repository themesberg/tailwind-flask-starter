# importFile.py
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.identity import DefaultAzureCredential
from .models import Files
from . import db

importFile = Blueprint('importFile', __name__)

# Remplacez ces valeurs par les vôtres
ACCOUNT_NAME = "geduser"
CONTAINER_NAME = "ged-immeuble"

@importFile.route("/upload/<profile>", methods=["POST"])
def upload_file(profile):
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Utilisez DefaultAzureCredential pour l'authentification
    blob_service_client = BlobServiceClient(
        account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net",
        credential=DefaultAzureCredential(),
    )
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    # Créer un "dossier" virtuel pour chaque profil
    blob_prefix = f"{profile}/"

    # Remplacez 'your_blob_name' par le nom que vous souhaitez donner au blob
    blob_client = container_client.get_blob_client(blob_prefix + "your_blob_name")

    # Téléchargez le fichier vers le blob
    blob_client.upload_blob(file)

    return jsonify({"message": "File uploaded successfully"}), 200
