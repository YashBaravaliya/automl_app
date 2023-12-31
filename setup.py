from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A Python package for automated feature engineering and machine learning.'
# LONG_DESCRIPTION = 'A package to perform arithmetic operations'

# Setting up
setup(
    name="automll",
    version=VERSION,
    author="Yash Bravaliya",
    author_email="yashbaravaliya206@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/YashBaravaliya/automll_package",
    # long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    INSTALL_REQUIRES = [
    "streamlit",
    "scikit-learn",
    "streamlit_extras",
    "pandas",
    "numpy",
    "streamlit_option_menu"
    ],
    keywords=['auto ml','no code ml','model'],
    LICENSE = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'automll = automll_package.main:main'
        ]
    },
)