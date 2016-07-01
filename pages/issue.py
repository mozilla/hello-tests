# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Issue(Base):

    _heading_locator = (By.CSS_SELECTOR, '.info-panel h1')
    _download_firefox_prompt_locator = (By.CSS_SELECTOR, '.promote-firefox > p')
    _download_firefox_link_locator = (By.CSS_SELECTOR, '.get-firefox a')

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.is_element_displayed(*self._heading_locator))
        return self

    @property
    def heading(self):
        return self.find_element(*self._heading_locator).text

    @property
    def download_firefox_prompt(self):
        return self.find_element(*self._download_firefox_prompt_locator).text

    @property
    def download_firefox_location(self):
        return self.find_element(*self._download_firefox_link_locator).get_attribute('href')
