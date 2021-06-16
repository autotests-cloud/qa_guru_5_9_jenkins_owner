from selene.support.shared.jquery_style import s
from selene import have


# // Kind of Java version, with additional comments about `this` ;)
#
# /**
#  * usage: new Dropdown("#country").select("Brazil")
#  */
# public class Dropdown {
#     public Dropdown(/*this, */String selector) {
#         this.selector = selector;
#     }
#
#     def select(/*this, */optionText) {
#         $(this.selector).click();
#         $(this.selector).$$("option").find_by(exactText(optionText)).click();
#     }
#
# }


class Dropdown:
    def __init__(self, selector: str):
        """
        this kind of a python docstring ;)

        usage:
            Dropdown("#country").select("Brazil")

        and here is what happens under the hood,
        for you to understand all this "self" magic:
            new_object = Dropdown.__new__()
            Dropdown.__init__(new_object, "#country")
            Dropdown.select(new_object, "Brazil")

        in fact, Java does pretty similar thing,
        it just hides all this "self" (called as "this" in java) under the hood;)
        while python follows the Tao :D telling "Explicit is better than implicit" :D
        """
        self.selector = selector

    def select(self, option_text):
        s(self.selector).click()
        s(self.selector).all("option").element_by(have.exact_text(option_text)).click()
