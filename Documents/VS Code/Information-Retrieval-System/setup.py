from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    version="0.0.1",
    author="DRKing",
    author_email="rmtariq@gmail.com",
    description="A project for generative AI experiments",
    packages=find_packages(),
    install_requires=[
        # Add required packages here, for example:
        "python-dotenv",
        "google-generativeai",
        "langchain",
        "PyPDF2",
        "faiss-cpu",
        "streamlit",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
