from setuptools import setup, find_packages

setup(
    name="wong-kar-wai-lens",
    version="0.1.0",
    description="Transform everyday photos into 1990s Hong Kong cinematic art & candid film snapshots.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pillow>=10.0.0",
        "numpy>=1.24.0",
    ],
    entry_points={
        "console_scripts": [
            "wkw-lens=src.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.9",
)
