from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A python wrapper for Omni-Rig'
LONG_DESCRIPTION = 'A package that allows the deveplopment of amateur radio applications using the amazing Omni-Rig library'

# Setting up
setup(
    name="omnipyrig",
    version=VERSION,
    author="4Z1KD (Gil)",
    author_email="<4z1kd@iarc.org>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pywin32'],
    keywords=['python', 'amateur radio', 'ham', 'omni-rig', 'omnirig', 'radio'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)