#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.hello import HelloPage


class TestHelloPage:

    @pytest.mark.nondestructive
    def test_supported_browser(self, mozwebqa):
        hello_page = HelloPage(mozwebqa)
        hello_page.go_to_page()
        assert hello_page.is_header_title_visible
        assert hello_page.is_start_call_button_visible
        assert hello_page.is_footer_logo_visible
        assert 'Firefox Hello' == hello_page.header_title_text
        assert 'Start' == hello_page.start_call_button_text
        assert hello_page.current_url_text == hello_page.actual_page_url

    @pytest.mark.nondestructive
    def test_unsupported_browser(self, mozwebqa):
        hello_page = HelloPage(mozwebqa)
        hello_page.go_to_page()
        assert 'Oops!\nFirefox Hello only works in browsers that support WebRTC\n' \
               'Download Firefox to make free audio and video calls!\nGet Firefox' == \
               hello_page.unsupported_browser_message_text
        assert 'https://www.mozilla.org/firefox/' in hello_page.unsupported_browser_firefox_link_href
