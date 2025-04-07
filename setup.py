import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "jugesdebnath7"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "jugesdebnath7@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization project using NLP techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "src"},
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/tree/main/docs",
        "Funding": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/funding",
        "Say Thanks!": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/say-thanks",
        "Code of Conduct": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/blob/main/CODE_OF_CONDUCT.md",
        "License": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/blob/main/LICENSE",
    }
)