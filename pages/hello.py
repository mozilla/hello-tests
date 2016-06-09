# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Hello(Base):

    _hello_logo_locator = (By.CSS_SELECTOR, '.hello-logo')
    _failed_room_message_locator = (By.CSS_SELECTOR, '.failed-room-message')

    def wait_for_page_to_load(self):
        body = self.find_element(By.TAG_NAME, 'body')
        self.wait.until(lambda s: 'is-standalone-room' in body.get_attribute('class'))
        return self

    @property
    def failed_room_message(self):
        return self.find_element(*self._failed_room_message_locator).text

    @property
    def is_hello_logo_visible(self):
        return self.is_element_displayed(*self._hello_logo_locator)
