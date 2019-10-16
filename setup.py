import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alembic-multischema",
    version="0.0.2",
    author="Mathew Moon",
    author_email="mmoon@quinovas.com",
    description="Provides a decorator to operate on multiple schemas at once using alembic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QuiNovas/alembic-multischema",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
