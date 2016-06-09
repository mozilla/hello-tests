# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import uuid

from pypom import Page


class Base(Page):

    URL_TEMPLATE = '{room}'

    def __init__(self, selenium, base_url, room=None, **url_kwargs):
        room = room or uuid.uuid4()
        super(Base, self).__init__(selenium, base_url, room=room, **url_kwargs)
