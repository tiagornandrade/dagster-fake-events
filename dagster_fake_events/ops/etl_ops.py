import pandas as pd
from dagster import op
from datetime import datetime
from utils.get_fake_event import create_data
from utils.csv_to_gcs import csvToGcs
from utils.gcs_to_bigquery import gcsToBq


# Variáveis de data e hora
ref_data = datetime.now()
ref_year = datetime.now().year
ref_time = datetime.now().strftime("%H%M%S")


@op
def extract_events_fake():
    # Gera a lista dos dados
    get_events_fake = create_data(1000)
    return get_events_fake


@op
def transform_to_pandas(context, get_events_fake):
    # Converte em DataFrame
    df = pd.DataFrame.from_dict(get_events_fake).transpose()

    date = datetime.now().strftime("%Y%m%d")
    time = str(ref_time)

    filename = f"C:/Temp/stage/fake_events_{date}_{time}"
    df_events_fake = df.to_csv(filename + ".csv", index=False)
    return df_events_fake


@op
def load_events_fake(context, df_events_fake):
    fake_event = csvToGcs().load_gcs()
    return fake_event


@op
def load_gcs_to_bigquery(context, fake_event):
    gcsToBq().load_bq()
