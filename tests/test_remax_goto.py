import unittest

from playwright.sync_api import expect, sync_playwright

import sweethome.sites.remax as remax
from sweethome import browser


class TestGoto(unittest.TestCase):

    def setUp(self) -> None:
        self.play = sync_playwright().start()
        self.browser = browser.new(self.play, headless=True)
        self.context = browser.context(self.browser)

    def tearDown(self) -> None:
        self.browser.close()
        self.play.stop()

    def test_home(self) -> None:
        page = remax.goto.home(self.context)
        expect(page).to_have_url(remax.urls.home + "/")
        page.close()

    def test_next_page(self) -> None:
        """
        Tests the next_page_url function in remax.urls by comparing its output
        with the expected next page URL.

        The test iterates over the first 5 department pages, calculates the
        expected next page URL, and checks if the output of next_page_url
        matches the expected URL.

        Args:
            None

        Returns:
            None
        """
        for page_index in range(0, 5):
            page_url = remax.urls.get_department_page(page_index=page_index)
            next_page_url = remax.urls.get_department_page(page_index=page_index + 1)
            output_next_page_url = remax.urls.next_page_url(page_url)
            self.assertEqual(output_next_page_url, next_page_url)
