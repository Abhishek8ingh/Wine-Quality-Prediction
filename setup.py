import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Wine-Qaulity-Prediction"
AUTHOR_USER_NAME = "ahbhi"
SRC_REPO = "WineQaulityPediction"
AUTHOR_EMAIL = "xyz@gamil.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Abhishek8ingh/Wine-Quality-Prediction",
    project_urls={
        "Bug Tracker": f"https://github.com/Abhishek8ingh/Wine-Quality-Prediction/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)