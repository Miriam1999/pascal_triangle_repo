from setuptools import setup

with open("requirements.txt", "r") as file:
    requirements = file.read()

setup(
    name="pascal_triangle",
    version="0.1.0",
    description="Simple pascal triangle implementation",
    install_requires=requirements.splitlines(),
    scripts=[
        "bin/pascal_triangle"
    ],
    package_dir={
        "": "src"
    })
