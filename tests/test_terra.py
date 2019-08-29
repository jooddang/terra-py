import toml

from terra import __version__


def test_version():
    # tests are started from root folder so path is relative to there
    with open("pyproject.toml") as f:
        assert __version__ == toml.load(f)["tool"]["poetry"]["version"]
