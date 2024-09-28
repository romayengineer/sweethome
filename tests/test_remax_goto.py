import unittest
from sweethome import browser
from playwright.sync_api import expect, sync_playwright
import sweethome.sites.remax as remax

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
        expect(page).to_have_url(remax.urls.home)
        page.close()
