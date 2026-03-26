from playwright.sync_api import expect


class Cart:

    def __init__(self, page):
        self.page = page
        self.cart = page.locator("#cart-drawer")

    def cart_visible(self, product):
        expect(self.cart.get_by_text(product)).to_be_visible()

    def cart_count(self):
        return int(self.page.locator("cart-count.count-bubble--md").inner_text().strip())


    def click_checkout(self):
        self.page.get_by_role("button", name="checkout").click()


