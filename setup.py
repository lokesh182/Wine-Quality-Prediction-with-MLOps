import setuptools

with open("README.md","r",encoding="utf-8") as f:# Readme file
    long_description = f.read()# Read the content of the file

__version__ ="0.0.0"

REPO_NAME="Wine-Quality-Prediction-with-MLOps"
AUTHOR_USER_NAME = "lokesh182"
SRC_REPO = "Wine-Quality-Prediction-with-MLOps"
AUTHOR_EMAIL = "lokeshbapte.18@gmail.com"

# Setup function
setuptools.setup(
    name=f"{REPO_NAME}-{AUTHOR_USER_NAME}",# Name of the project
    version=__version__,# Version of the project
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is a project for wine quality prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",# URL of the project
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    }
)
