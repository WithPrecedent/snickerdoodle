import pytest


@pytest.fixture()
def context():
    """Creates default prompt values."""
    return {
        'project_name': 'test-project'
    }
    