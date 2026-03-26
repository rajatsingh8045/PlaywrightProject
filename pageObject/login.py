


class LoginPage:

    def __init__(self,page):
        self.page = page



    def navigate(self):
        self.page.goto("https://vitaminworld.com", wait_until="domcontentloaded")

    def get_title(self):
        return self.page.title()