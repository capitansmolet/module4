from selenium.webdriver import Remote

from .base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser: Remote, url: str) -> None:
        super().__init__(browser, url)
