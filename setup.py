import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geonode-api",
    version="0.0.1",
    author="Kartoza",
    author_email="info@kartoza.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kartoza/qgis_geonode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)