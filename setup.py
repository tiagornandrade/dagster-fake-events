import setuptools

setuptools.setup(
    name="dagster_fake_events",
    packages=setuptools.find_packages(exclude=["dagster_fake_events_tests"]),
    install_requires=[
        "dagster==0.14.12",
        "dagit==0.14.12",
        "pytest",
    ],
)
