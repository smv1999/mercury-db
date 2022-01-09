from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mercury_db',
    version='0.0.1',
    description='The mercury-db package is a simple key-value datastore',
    packages=['mercury_db'],
    py_modules=['mercury_db.datastore'],
    package_dir={'': 'src'},
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vaidhyanathan S M",
    author_email="vaidhyanathan.sm@gmail.com",
    url="https://github.com/smv1999/mercury-db"
)
