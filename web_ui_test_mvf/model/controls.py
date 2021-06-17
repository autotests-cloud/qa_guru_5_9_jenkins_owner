from selene import have
from selene.support.shared.jquery_style import s

# public class DropDown {
#
#     public DropDown(/*this, */String selector) {
#         this.selector = selector
#     }
#
#     public void select(/*this, */String optionText) {
#         $(this.selector).click()
#         $(this.selector).$$("option").findBy(exactText(optionText)).click()
#     }
# }

# new DropDown("#country").select("Brazil")


class DropDown:

    def __init__(self, selector: str):
        self.selector = selector

    def select(self, option_text: str):
        s(self.selector).click()
        s(self.selector).all("option").element_by(have.exact_text(option_text)).click()



