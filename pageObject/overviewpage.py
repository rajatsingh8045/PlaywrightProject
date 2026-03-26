from playwright.sync_api import expect


class OverviewPage:
    def __init__(self, page):
        self.page = page

    def summary_visible(self, product):
        expect(self.page.get_by_text(product)).to_be_visible()
