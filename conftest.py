
#import pytest
#from playwright.sync_api import sync_playwright


#def test_playwrightBasics(page):
#set_viewport_size({"width": 1920, "height": 1080})

import datetime
import os

def pytest_configure(config):
    if config.option.htmlpath:
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)
        config.option.htmlpath = f"{report_dir}/report_{now}.html"


import pytest

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": None
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "args": ["--start-maximized"]
    }

#@pytest.fixture(scope="function")
#def page():
        #with sync_playwright() as p:

         # browser = p.chromium.launch(headless=False, args=["--start-maximized"])
         # context = browser.new_context(no_viewport=True)
         # page = context.new_page()

         # yield page

         # context.close()
         # browser.close()
