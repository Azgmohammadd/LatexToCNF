import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="LatexToCNF",
    version="0.1.3",
    description="python cli program to convert latex input to CNF (conjuctive normal form).",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Azgmohammadd/LatexToCNF",
    author="azgmohammadd",
    author_email="azgmohammadd@gmail.com",
    license="MIT",
    entry_points={
        'console_scripts': [
            'LatexToCNF = LatexToCNF.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["LatexToCNF"],
    include_package_data=True,
    install_requires=requirements,
)