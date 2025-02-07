import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description= f.read()

__version__= "0.0.0"
Repo_Name = "TextSummarizer"
AUTHOR_USER_NAME = "aswin19031997"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "aswin19031997@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small package for Text Summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{Repo_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{Repo_Name}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)