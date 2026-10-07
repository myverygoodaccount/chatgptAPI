import requests
from playwright.sync_api import sync_playwright


class Chrome:
    CDP_URL = "http://127.0.0.1:9222"

    def __init__(self, chrome_path):
        self.chrome_path = chrome_path
        self.playwright = None
        self.browser = None

    def _is_running(self):
        try:
            return requests.get(
                f"{self.CDP_URL}/json/version",
                timeout=0.5
            ).ok
        except requests.RequestException:
            return False

    def start(self):
        self.playwright = sync_playwright().start()

        if self._is_running():
            # Attach to the existing Chrome
            self.browser = self.playwright.chromium.connect_over_cdp(
                self.CDP_URL
            )
        else:
            # Start a new Chrome
            self.browser = self.playwright.chromium.launch(
                executable_path=self.chrome_path,
                headless=False
            )

        return self.browser

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()
