import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup
    name="DataGlacier-bmusham", #Replace with your own username
    version="0.0.1",
    author="Bindu Musham",
    author_email="bindu.musham@gmail.com",
    description="It is a simple package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmusham/DataGlacier",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires='>=3.6',
