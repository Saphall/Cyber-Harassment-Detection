from setuptools import setup, find_packages

setup(
    name="Cyber Harassment Detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nltk==3.9.2",
        "flask==3.1.3",
        "emoji==2.15.0",
        "scipy==1.11.4",
        "numpy==1.26.4",
        "scikit-learn==1.6.1",
    ],
    extras_require={"dev": ["black"]},
)
