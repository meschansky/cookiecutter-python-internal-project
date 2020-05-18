"""Root package."""
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

if __name__ == "__main__":
    print(f"installed version of this project: {__version__}")
