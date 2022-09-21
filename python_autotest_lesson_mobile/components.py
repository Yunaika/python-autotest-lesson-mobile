from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from helpers.allure.report import step


@step
def search_in_wikipedia(text):
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

@step
def verify_content_found():
    browser.all(
        (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
    ).should(have.size_greater_than(0))