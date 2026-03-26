#import time

#from playwright.sync_api import Page


def test_playwrightBasics(page):
    page.goto("https://vitaminworld.com")
    assert page.title() != ""

    omega = page.get_by_role("link", name='Omega 3,6,9 Fish, Flax & Borage Oils, 120 Softgels')


    omegaParent = omega.locator("..").locator("..")

    omegaParent.get_by_role("button", name="Add to Cart").click()

    page.wait_for_timeout(2000)

    hair = page.get_by_role("link", name="Codeage Hair Vitamins 10000 mcg Biotin, Keratin, Collagen, 120 Caps")
    hair_parent = hair.locator("..").locator("..")
    hair_parent.get_by_role("button", name="Add to Cart").click()

    page.wait_for_timeout(2000)

    # Scroll (your working fix 👍)
    page.evaluate("window.scrollTo(0, 0)")

    page.get_by_role("link", name="Cart").click()
