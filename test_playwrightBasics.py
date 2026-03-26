import time


#from playwright.sync_api import Page, expect


def test_playwrightBasics(page):
    browser = page.chromium.launch(headless=True, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://vitaminworld.com", wait_until="domcontentloaded")


#def test_playwrightShortcut(page: Page):
    #page.goto("https://vitaminworld.com")

    omega_tablet = page.locator("ai-product-slider-container").filter(
        has_text="Omega 3,6,9 Fish, Flax & Borage Oils, 120 Softgels")

    page.locator("button[data-product-id='8355062055104']").click()

    page.wait_for_timeout(2000)

    hair_tablet = page.locator("ai-product-slider-container").filter(
        has_text="Codeage Hair Vitamins 10000 mcg Biotin, Keratin, Collagen, 120 Caps")
    page.locator("button[data-product-id='8355056812224']").click()

    page.wait_for_timeout(2000)

    page.evaluate("window.scrollTo(0, 0)")

    page.get_by_role("link", name="Cart").click()

    cart = page.locator("#cart-drawer")



    assert cart.get_by_text("Codeage Hair Vitamins 10000 mcg Biotin, Keratin, Collagen, 120 Caps")
    assert cart.get_by_text("Omega 3,6,9 Fish, Flax & Borage Oils, 120 Softgels").is_visible()

    cart_count = page.locator("cart-count.count-bubble--md")
    assert cart_count.inner_text().strip() == "2"

    page.get_by_role("button", name= "checkout").click()

    assert page.get_by_text("Codeage Hair Vitamins 10000 mcg Biotin, Keratin, Collagen, 120 Caps")
    assert page.get_by_text("Omega 3,6,9 Fish, Flax & Borage Oils, 120 Softgels")

    time.sleep(10)
