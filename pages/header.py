from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Header(Page):
    cases_protection_link = (By.CSS_SELECTOR, '#menu-item-485 a[href="/cases"]')
    accessories = (By.ID, 'menu-item-472')
    cases_protection_404 = (By.CSS_SELECTOR, 'h1.page-title')

    def hover_over_accessories(self):
        accessories = self.find_element(*self.accessories)
        actions = ActionChains(self.driver)
        actions.move_to_element(accessories)
        actions.perform()

    def cases_protection_click(self):
        self.click(*self.cases_protection_link)

    def cases_protection_404_verify(self):
        self.verify_partial_text("Oops! That page can’t be found.", *self.cases_protection_404)

