import os


def credential():
    pk_path = os.getcwd()+"\\utils\credential.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = pk_path
