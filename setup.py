from setuptools import find_packages, setup

setup(
    name="mypypackage",
    version="1.0.0",
    description="Example project using  my cookiecutter template.",
    author="Justin Lam",
    author_email="contact@justinmklam.com",
    url="https://github.com/justinmklam/example-python-package",
    packages=find_packages(),
    scripts=[],
    install_requires=[
        "pytest",
    ],
    zip_safe=False,
)
