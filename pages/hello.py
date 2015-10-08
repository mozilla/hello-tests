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

    _failed_room_text_locator = (By.CSS_SELECTOR, '.failed-room-message')
    _mozilla_logo_locator = (By.CSS_SELECTOR, '.standalone-moz-logo')
    _header_title_locator = (By.CSS_SELECTOR, '.room-conversation-wrapper header h1')
    _page_content_locator = (By.ID, 'main')
    _unsupported_browser_message_locator = (By.ID, 'main')
    _unsupported_browser_firefox_link_locator = (By.CSS_SELECTOR, '#main a')

    def go_to_page(self):
        self.url = '%s/%s' % (self.base_url, hash(datetime.datetime.now()))
        self.selenium.get(self.url)
        WebDriverWait(self.selenium, self.timeout).until(EC.visibility_of_element_located(self._page_content_locator))

    @property
    def actual_page_url(self):
        return self.url

    @property
    def is_invalid_conversation_visible(self):
        return self.is_element_visible(*self._failed_room_text_locator)

    @property
    def invalid_conversation_text(self):
        return self.selenium.find_element(*self._failed_room_text_locator).text

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
    def is_mozilla_logo_visible(self):
        return self.is_element_visible(*self._mozilla_logo_locator)
