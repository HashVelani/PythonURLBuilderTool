import pytest

from urlBuilder.builders import urlBuilder

def test_url():
    output = urlBuilder()
    assert output == "hello world"