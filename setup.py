import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devai",
    version="0.1.0",
    author="588seco",
    author_email="",
    description="Testing the first machine learning project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Seco588/devai",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "pandas", "tensorflow", "matplotlib","openai","gpt-3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
