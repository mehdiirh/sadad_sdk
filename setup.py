import ast
import re
from pathlib import Path

import setuptools

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


def get_version() -> str:
    sadad_sdk = CURRENT_DIR / "sadad_sdk/__init__.py"
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(sadad_sdk, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setuptools.setup(
    name="sadad_sdk",
    version=get_version(),
    author="Mehdi Rahimi",
    author_email="contact@mehdirh.dev",
    description="Python SDK for the Sadad API (v1)",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords=["sadad", "shaparak"],
    url="https://github.com/mehdiirh/sadad_sdk",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["requests", "dataclasses-json", "pycrypto", "pycryptodome"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False,
)
