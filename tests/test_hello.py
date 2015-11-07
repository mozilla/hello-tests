# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.hello import HelloPage
from pages.issue import IssuePage


@pytest.mark.nondestructive
def test_supported_browser(base_url, selenium):
    page = HelloPage(base_url, selenium).open()
    assert page.is_hello_logo_visible
    assert page.is_mozilla_logo_visible
    assert 'Sorry, you cannot join this conversation. ' \
           'The link may be expired or invalid.' == page.failed_room_message


@pytest.mark.nondestructive
def test_unsupported_browser(base_url, selenium):
    page = IssuePage(base_url, selenium).open()
    assert 'Oops!' == page.heading
    assert 'Firefox Hello only works in browsers that support WebRTC' == page.issue
    assert 'Download Firefox to make free audio and video calls!' == page.download_firefox_prompt
    assert 'https://www.mozilla.org/firefox/' in page.download_firefox_location
