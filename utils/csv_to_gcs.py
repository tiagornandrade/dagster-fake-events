import os
import glob
from datetime import datetime
from google.cloud import storage
from utils.secret import credential


class csvToGcs:
    def __init__(self) -> None:
        pass

    def load_gcs(self):

        credential()

        date = datetime.now().strftime("%Y%m%d")

        source_dir = "C:\Temp\stage"
        sources = glob.glob(os.path.join(source_dir, "*.csv"))

        bucket_name = "dl-inbound-fake_events"
        source_file_name = sources[0]
        destination_blob_name = f"fake-event_{date}.csv"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        for f in sources:
            os.remove(f)
