from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import yaml
import json


class DriveRepository:
    def __init__(self):
        self.folder_id = "drive.google.com/drive/u/3/folders/1veMpzxUr9MIWrbdDPpNaUTfYiOlr9TcZ"
        self.resource_path = "../../../resource"
        settings_file = f"{self.resource_path}/settings.yaml"
        settings = open(settings_file, "r")
        client_secret = open(f"{self.resource_path}/client_secret.json", "r")
        client_secret_json = json.load(client_secret)

        settings_yaml = yaml.load(settings, Loader=yaml.FullLoader)

        settings_yaml["client_config"]["client_id"] = client_secret_json["installed"]["client_id"]
        settings_yaml["client_config"]["client_secret"] = client_secret_json["installed"]["client_secret"]
        settings_yaml["save_credentials_file"] = f"{self.resource_path}/credentials.json"

        with open(settings_file, "w") as yaml_file:
            yaml_file.write(yaml.dump(settings_yaml, default_flow_style=False))

        g_auth = GoogleAuth(settings_file=f"{self.resource_path}/settings.yaml")
        g_auth.LocalWebserverAuth()
        self.drive = GoogleDrive(g_auth)

    def create_folder(self, folder_name: str):
        file_metadata = {
            'title': folder_name,
            'parents': [{'id': self.folder_id}],
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = self.drive.CreateFile(file_metadata)
        folder.Upload()

    def upload_file(self, file_name: str):
        file_metadata = {
            'title': folder_name,
            'parents': [{'id': self.folder_id}],
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = self.drive.CreateFile(file_metadata)
        folder.Upload()