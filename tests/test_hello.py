# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.hello import Hello
from pages.issue import Issue


@pytest.mark.nondestructive
def test_supported_browser(base_url, selenium):
    page = Hello(selenium, base_url).open()
    assert page.is_hello_logo_visible
    assert 'Sorry, you cannot join this conversation. ' \
           'The link may be expired or invalid.' == page.failed_room_message


@pytest.mark.nondestructive
def test_unsupported_browser(base_url, selenium):
    page = Issue(selenium, base_url).open()
    assert 'Hello is not supported by this browser.' == page.heading
    assert 'Get Firefox and start sharing the Web! Learn more.' == page.download_firefox_prompt
    assert 'https://www.mozilla.org/firefox/' in page.download_firefox_location
