# conftest.py
# Configuration file for pytest

def pytest_addoption(parser):
    parser.addoption("--mock", action="store_true", dest="mock")
