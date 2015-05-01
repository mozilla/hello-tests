#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page


class HelloPage(Page):

    _current_url_locator = (By.CSS_SELECTOR, '.call-url')
    _start_call_button_locator = (By.CSS_SELECTOR, 'button.btn-accept')
    _footer_logo_locator = (By.CSS_SELECTOR, '.footer-logo')
    _header_title_locator = (By.CSS_SELECTOR, '.standalone-header-title')
    _page_content_locator = (By.ID, 'main')
    _unsupported_browser_message_locator = (By.ID, 'main')
    _unsupported_browser_firefox_link_locator = (By.CSS_SELECTOR, '#main a')

    def go_to_page(self):
        self.url = '%s/c/%s' % (self.base_url, hash(datetime.datetime.now()))
        self.selenium.get(self.url)
        WebDriverWait(self.selenium, self.timeout).until(EC.visibility_of_element_located(self._page_content_locator))

    @property
    def actual_page_url(self):
        return self.url

    @property
    def current_url_text(self):
        return self.selenium.find_element(*self._current_url_locator).text

    @property
    def is_start_call_button_visible(self):
        return self.is_element_visible(*self._start_call_button_locator)

    @property
    def start_call_button_text(self):
        return self.selenium.find_element(*self._start_call_button_locator).text

    @property
    def is_header_title_visible(self):
        return self.is_element_visible(*self._header_title_locator)

    @property
    def header_title_text(self):
        return self.selenium.find_element(*self._header_title_locator).text

    @property
    def unsupported_browser_message_text(self):
        return self.selenium.find_element(*self._unsupported_browser_message_locator).text

    @property
    def unsupported_browser_firefox_link_href(self):
        return self.selenium.find_element(
            *self._unsupported_browser_firefox_link_locator).get_attribute('href')

    @property
    def is_footer_logo_visible(self):
        return self.is_element_visible(*self._footer_logo_locator)
