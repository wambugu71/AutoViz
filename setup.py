import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoviz",
    version="0.1.803",
    author="Ram Seshadri",
    # author_email="author@example.com",
    description="Automatically Visualize any dataset, any size with a single line of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url="https://github.com/AutoViML/AutoViz.git",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=[
        "xlrd",
        "wordcloud",
        "emoji",
        "numpy",
        "pandas",
        "pyamg",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "statsmodels",
        "nltk",
        "textblob",
        "holoviews",
        "bokeh",
        "hvplot",
        "panel",
        "xgboost",
        "fsspec",
        "typing-extensions",
        "pandas-dq"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
