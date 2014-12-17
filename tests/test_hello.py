#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.hello import HelloPage


class TestHelloPage:

    @pytest.mark.nondestructive
    def test_supported_browser(self, mozwebqa):
        hello_page = HelloPage(mozwebqa)
        hello_page.go_to_page()
        Assert.true(hello_page.is_header_title_visible)
        Assert.true(hello_page.is_start_call_button_visible)
        Assert.true(hello_page.is_footer_logo_visible)
        Assert.equal('Firefox Hello', hello_page.header_title_text)
        Assert.equal('Start', hello_page.start_call_button_text)
        Assert.equal(hello_page.actual_page_url, hello_page.current_url_text)

    @pytest.mark.nondestructive
    def test_unsupported_browser(self, mozwebqa):
        hello_page = HelloPage(mozwebqa)
        hello_page.go_to_page()
        Assert.equal('Oops!\nFirefox Hello only works in browsers that support WebRTC\nDownload Firefox to make free audio and video calls!\nGet Firefox',
                     hello_page.unsupported_browser_message_text)
        Assert.equal('https://www.mozilla.org/firefox/', hello_page.unsupported_browser_firefox_link_href)
