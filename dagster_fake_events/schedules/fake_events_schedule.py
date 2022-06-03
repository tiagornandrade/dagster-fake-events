from dagster import schedule

from dagster_fake_events.jobs.etl_jobs import etl_events_fake


@schedule(
    cron_schedule="* * * * *", job=etl_events_fake, execution_timezone="US/Central"
)
def etl_events_schedule(_context):
    return {}
