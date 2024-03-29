import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="liblistloader",
    version="1.0.1.post2",
    author="BBaoVanC",
    author_email="pypi@bbaovanc.com",
    description="Library for loading of word lists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.bbaovanc.com/bbaovanc/liblistloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
