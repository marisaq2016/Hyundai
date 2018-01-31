class BasePage:

    def __init__(self, browser, wait, hover):
        self.browser = browser
        self.wait = wait
        self.hover = hover
