import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github-actions-jashburn8020",
    version="0.0.1",
    author="Jeffri Abu Bakar",
    description="Sample Python scripts to run GitHub Actions examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License v2",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)