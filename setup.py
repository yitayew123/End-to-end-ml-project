import setuptools  # Import the setuptools module to facilitate packaging of the Python project

with open("README.md", "r", encoding="utf-8") as f:  # Open the README.md file in read mode with UTF-8 encoding
    long_description = f.read()  # Read the content of the README.md file and store it in the long_description variable

__version__ = "0.0.0"  # Define the version of the package

# Define metadata for the package
REPO_NAME = "End-to-end-ML-Project-Implementation"  # Name of the repository
AUTHOR_USER_NAME = "yitayew123"  # GitHub username of the author
SRC_REPO = "mlproject"  # Name of the source repository
AUTHOR_EMAIL = "yitayewsolomon3@gmail.com"  # Email of the author

# Configure the setup function to provide package details
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's username
    author_email=AUTHOR_EMAIL,  # Author's email
    description="A small python package for ml app",  # Short description of the package
    long_description=long_description,  # Long description of the package from README.md
    long_description_content="text/markdown",  # Format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for reporting issues
    },
    package_dir={"": "src"},  # Directory where packages are located
    packages=setuptools.find_packages(where="src")  # Automatically find all packages under the "src" directory
)