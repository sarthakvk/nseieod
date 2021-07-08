from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nseieod",
    version="1.0",
    author="Sarthak Vineet Kumar",
    author_email="kumar.v.sarthak@gmail.com",
    description="A python package for learning algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarthakvk/nseieod",
    packages=find_packages(),
    licence="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["nsetools", "sqlalchemy"],
    # entry point for the application
    entry_points={
        "console_scripts": [
            "nseieod=nseieod:run",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/sarthakvk/nseieod/issues",
        "Say Thanks!": "http://sarthakvkumar.tech",
        "Source": "https://github.com/sarthakvk/nseieod/",
    },
)
