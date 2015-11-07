# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

from pages.page import Page


class HelloPage(Page):

    _hello_logo_locator = (By.CSS_SELECTOR, '.hello-logo')
    _failed_room_message_locator = (By.CSS_SELECTOR, '.failed-room-message')
    _mozilla_logo_locator = (By.CSS_SELECTOR, '.standalone-moz-logo')

    @property
    def _url(self):
        return '{base_url}/{id}'.format(base_url=self.base_url, id=uuid.uuid4())

    def wait_for_page_to_load(self):
        body = self.selenium.find_element(By.TAG_NAME, 'body')
        Wait(self.selenium, self.timeout).until(
            lambda s: 'is-standalone-room' in body.get_attribute('class'))
        return self

    @property
    def failed_room_message(self):
        return self.selenium.find_element(
            *self._failed_room_message_locator).text

    @property
    def is_hello_logo_visible(self):
        return self.is_element_visible(self._hello_logo_locator)

    @property
    def is_mozilla_logo_visible(self):
        return self.is_element_visible(self._mozilla_logo_locator)
