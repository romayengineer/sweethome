import unittest

import sweethome.sites.remax as remax
from sweethome import browser
from sweethome.logging import Logger
from sweethome.types import expect, get_context

logger = Logger(__name__, is_test=True)


class TestGoto(unittest.TestCase):

    def setUp(self) -> None:
        logger.info("Setting up test TestGoto")
        self.play = get_context().start()
        self.browser = browser.new(self.play, headless=True)
        self.context = browser.context(self.browser)

    def tearDown(self) -> None:
        logger.info("Tearing down test TestGoto")
        self.browser.close()
        self.play.stop()

    def test_home(self) -> None:
        logger.info("Testing home")
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
        logger.info("Testing next_page")
        for page_index in range(0, 5):
            page_url = remax.urls.get_department_page(page_index=page_index)
            next_page_url = remax.urls.get_department_page(page_index=page_index + 1)
            output_next_page_url = remax.urls.next_page_url(page_url)
            self.assertEqual(output_next_page_url, next_page_url)
