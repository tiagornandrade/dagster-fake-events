from dagster import job

from dagster_fake_events.ops.etl_ops import (
    extract_events_fake,
    transform_to_pandas,
    load_events_fake,
    load_gcs_to_bigquery,
)


@job
def etl_events_fake():
    extract = extract_events_fake()
    transform = transform_to_pandas(extract)
    load = load_events_fake(transform)
    load_gcs_to_bigquery(load)
