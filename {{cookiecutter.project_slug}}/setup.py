"""https://packaging.python.org/"""
from pathlib import Path

from setuptools import setup, find_packages

import versioneer

HERE = Path(__file__).parent.resolve()  # resolve necessary in pip build context


kwargs = dict(
    name="{{ cookiecutter.project_slug }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(exclude=["docs", "tests"]),
    # TODO adjust for your organisation
    author="{{ cookiecutter.full_name }}",
    # TODO adjust for your organisation
    author_email="{{ cookiecutter.email }}",
    install_requires=(HERE / "requirements.txt").read_text(),
    extras_require={"test": (HERE / "requirements-test.txt").read_text()},
    # If you need command line executables ...
    # entry_points={"console_scripts": ["executable-name = path.to.module:function"]},
    url="{{ cookiecutter.project_url }}",
)


if __name__ == "__main__":
    setup(**kwargs)
