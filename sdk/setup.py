from setuptools import setup, find_packages

setup(
    name="truvem",
    version="0.1.1",
    description="Universal persistent memory for AI agents",
    author="Truvem",
    author_email="gettruvem@gmail.com",
    url="https://github.com/truvem/truvem",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)
