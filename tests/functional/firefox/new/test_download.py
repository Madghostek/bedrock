# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.new.download import DownloadPage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_download_button_displayed(base_url, selenium):
    page = DownloadPage(selenium, base_url).open()
    assert page.is_download_button_displayed


# Firefox and Internet Explorer don't cope well with file prompts whilst using Selenium.
@pytest.mark.skip_if_firefox(reason="http://saucelabs.com/jobs/5a8a62a7620f489d92d6193fa67cf66b")
@pytest.mark.skip_if_internet_explorer(reason="https://github.com/SeleniumHQ/selenium/issues/448")
@pytest.mark.nondestructive
def test_click_download_button(base_url, selenium):
    page = DownloadPage(selenium, base_url).open()
    thank_you_page = page.download_firefox()
    assert thank_you_page.seed_url in selenium.current_url
