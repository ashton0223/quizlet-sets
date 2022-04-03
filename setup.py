import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quizlet-sets",
    version="0.0.1",
    author="Ashton South",
    author_email="aasouth223@gmail.com",
    description="A package to download Quizlet study sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashton0223/quizlet-sets",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "quizlet_sets"},
    packages=setuptools.find_packages(where="quizlet_sets"),
    python_requires=">=3.6",
    install_requires=[
        'xlwt',
        'genanki',
    ]
)