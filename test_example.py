import pytest

@pytest.mark.smoke
def test_example(page):
    page.goto("https://example.com")
    page.wait_for_timeout(1000)
    assert False