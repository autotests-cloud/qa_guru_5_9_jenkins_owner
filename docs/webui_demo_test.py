from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = True

browser.open("https://google.com/ncr")
s("[name=q]").type('qa guru').press_enter()
