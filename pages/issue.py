#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait as Wait

from pages.page import Page


class IssuePage(Page):

    _heading_locator = (By.CSS_SELECTOR, '.highlight-issue-box h1')
    _issue_locator = (By.CSS_SELECTOR, '.highlight-issue-box h4')
    _download_firefox_prompt_locator = (By.CSS_SELECTOR, '.promote-firefox h3')
    _download_firefox_link_locator = (By.CSS_SELECTOR, '.promote-firefox a')

    @property
    def _url(self):
        return '{base_url}/{id}'.format(base_url=self.base_url, id=uuid.uuid4())

    def wait_for_page_to_load(self):
        Wait(self.selenium, self.timeout).until(
            expected.visibility_of_element_located(self._heading_locator))
        return self

    @property
    def heading(self):
        return self.selenium.find_element(*self._heading_locator).text

    @property
    def issue(self):
        return self.selenium.find_element(*self._issue_locator).text

    @property
    def download_firefox_prompt(self):
        return self.selenium.find_element(
            *self._download_firefox_prompt_locator).text

    @property
    def download_firefox_location(self):
        return self.selenium.find_element(
            *self._download_firefox_link_locator).get_attribute('href')
