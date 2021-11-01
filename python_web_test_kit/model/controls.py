from selene import have
from selene.support.shared.jquery_style import s


class DropDown:
    def __init__(self, selector: str):
        self.selector = selector

    def select(self, text):
        s(self.selector).click()
        s(self.selector).all('option').element_by(have.text(text)).click()
