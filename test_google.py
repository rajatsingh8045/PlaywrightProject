import pytest


@pytest.mark.smoke
def test_google(page):
    page.goto("https://google.com")
