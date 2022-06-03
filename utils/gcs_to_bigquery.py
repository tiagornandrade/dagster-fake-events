from utils.secret import credential
from google.cloud import bigquery


class gcsToBq:
    def __init__(self) -> None:
        pass

    def load_bq(self):
        id_project = "invertible-pad-249722"
        id_dataset = "fake_events"
        id_table = "tb_fake_events"

        credential()

        # Caso exista a tabela no bigquery, será deletada
        client = bigquery.Client()

        table_id = f"{id_project}.{id_dataset}.{id_table}"

        table = bigquery.Table(table_id)
        table_delete = client.delete_table(
            table_id, not_found_ok=True
        )  # Make an API request.  # executa uma requisição na API.

        # -------------------------------------------------------------------------------------

        # Cria uma nova tabela no bigquery
        client = bigquery.Client()

        table_id = f"{id_project}.{id_dataset}.{id_table}"

        table = bigquery.Table(table_id)
        table = client.create_table(table)  # executa uma requisição na API.

        # -------------------------------------------------------------------------------------

        path_datalake = f"gs://dl-inbound-fake_events"
        file_csv = f"fake-event_*.csv"

        # Cria o job para a carga no bigquery
        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
        )
        uri = f"{path_datalake}/{file_csv}"

        load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config
        )  # executa uma requisição na API.
        load_job.result()  # Espera a conclusão do job.

        destination_table = client.get_table(table_id)
