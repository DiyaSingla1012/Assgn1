from setuptools import setup, find_packages

setup(
    name="Topsis-Diya-102303694",
    version="1.0.0",
    author="Diya Singla",
    author_email="diya@example.com",
    description="A Python package for TOPSIS decision making",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_diya_102303694.topsis:run"
        ]
    },
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
