from dagster import repository

from dagster_fake_events.jobs.etl_jobs import etl_events_fake
from dagster_fake_events.schedules.fake_events_schedule import etl_events_schedule
from dagster_fake_events.sensors.my_sensor import my_sensor


@repository
def dagster_fake_events():
    job_etl = [etl_events_fake]
    schedule_etl = [etl_events_schedule]

    return job_etl + schedule_etl
