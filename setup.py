from setuptools import setup, find_packages

setup(
    name="m3_project",
    version="1.0",
    packages=find_packages(include=("app", "m3_project")),
    install_requires=(
        "django>=2.2.28",
        "m3-django-compat==1.9.2",
        "m3-objectpack==2.2.47"
    )
)
