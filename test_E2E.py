import json
import os
import time

#from playwright.sync_api import Page, expect

from pageObject.cart import Cart
from pageObject.dashboard import Dashboard
from pageObject.overviewpage import OverviewPage
#from pageObject import dashboard

from pageObject.login import LoginPage


#Launch URL
def test_E2E(page):
    page.goto("https://vitaminworld.com")

    #Import testData

    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_dir, "data", "product.json")

    with open(file_path) as f:
        testdata = json.load(f)
        print(testdata)
        products = testdata['product']

    home = Dashboard(page)
    cart = Cart(page)
    overview = OverviewPage(page)

    #Login to vitamin page
    login = LoginPage(page)
    login.navigate()

    #Select the product
    for product in products:
        home.visibleProduct(product["name"])

        #addtoCart
        home.addCart(product["id"])

    #GotoCart
    home.go_to_cart()

    #Cartvisible
    for product in products:
        cart.cart_visible(product["name"])

    assert cart.cart_count() == len(products)

    #clickCheckout
    cart.click_checkout()

    #OverviewPage
    for product in products:
        overview.summary_visible(product["name"])

    time.sleep(10)
