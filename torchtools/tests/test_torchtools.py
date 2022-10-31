"""
Unit and regression test for the torchtools package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import torchtools


def test_torchtools_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "torchtools" in sys.modules
