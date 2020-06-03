"""Test cases for the hypermodern_projectstructure __init__."""
import hypermodern_projectstructure


def test_version_exists() -> None:
    """It tries to get the __version__ of hypermodern_projectstructure."""
    assert hasattr(hypermodern_projectstructure, "__version__")
