from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    author="RafaelTorices",
    packages=find_packages(),
    install_requires=[
        # Lista de tus dependencias si las tienes
    ],
    entry_points={
        "console_scripts": [
            "calculator=src.calculator:calculator",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
