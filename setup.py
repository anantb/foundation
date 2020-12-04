import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instabase-foundation",
    version="0.0.1",
    author="Instabase",
    author_email="support@instabase.com",
    description="A library defining types and interfaces to be used across Instabase.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/instabase/foundation",
    packages=['foundation'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'': 'py'},
    install_requires=[
        'mypy==0.701',
        'mypy-extensions==0.4.3',
        'mypy-protobuf==1.9',
        'protobuf==3.6.1',
        'six==1.15.0',
        'typed-ast==1.3.5',
        'typing-extensions==3.7.4.3',
    ]
)
