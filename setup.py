from setuptools import setup, find_packages

setup(
    name="Cyber Harassment Detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "flask",
        "emoji",
        "scipy",
        "numpy",
        "scikit-learn",
    ],
    extras_require={"dev": ["black"]},
)
