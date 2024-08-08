import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description= f.read()

__version__ = "0.0.0"
REPO_NAME = "TestProject"
AUTHER_USER_NAME = "MohammedSameeruddin"
SRC_REPO ="TESTPROJECT"
AUTHER_EMAIL = "mohdsameeruddinsam@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHER_USER_NAME,
    description="Test Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    author_email=AUTHER_EMAIL,
    project_url={
        "Bug Tracker":f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")
)