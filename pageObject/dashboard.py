


from playwright.sync_api import expect


class Dashboard:

    def __init__(self, page):
        self.page = page


    def visibleProduct(self,product):

      expect(self.page.get_by_text(product)).to_be_visible()

      self.page.wait_for_timeout(1000)




    def addCart(self,product_id):

       self.page.locator(f"button[data-product-id='{product_id}']").click()

    def go_to_cart(self):
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.get_by_role("link", name="Cart").click()



