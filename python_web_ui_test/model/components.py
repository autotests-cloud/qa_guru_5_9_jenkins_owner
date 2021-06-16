import os

from selene.support.shared.jquery_style import s
from selene import have


class Dropdown:
    def __init__(self, selector: str):
        self.selector = selector

    def select(self, option_text):
        s(self.selector).click()
        s(self.selector).all("option").element_by(have.exact_text(option_text)).click()


class Upload:
    def __init__(self, selector: str):
        self.selector = selector

    def from_relative(self, path):
        s(self.selector).type(os.path.abspath(path))
