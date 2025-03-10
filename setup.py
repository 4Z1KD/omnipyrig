from setuptools import setup, find_packages
major = 1
minor = 0
build = 0
VERSION = f'{major}.{minor}.{build}'
DESCRIPTION = 'A python wrapper for Omni-Rig'

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="omnipyrig",
    version=VERSION,
    author="4Z1KD (Gil)",
    author_email="<4z1kd@iarc.org>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    project_urls= {"github":"https://github.com/4Z1KD/omnipyrig"},
    packages=find_packages(),
    install_requires=['pywin32'],
    keywords=['python', 'amateur radio', 'ham', 'omni-rig', 'omnirig', 'radio'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)