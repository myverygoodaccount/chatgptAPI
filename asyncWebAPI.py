import asyncio
from playwright.async_api import async_playwright


class AsyncChrome:
    CDP_URL = "http://127.0.0.1:9222"

    def __init__(self, chrome_path=None, headless=False):
        self.chrome_path = chrome_path
        self.headless = headless

        self.playwright = None
        self.browser = None
        self._owns_browser = False

    async def __aenter__(self):
        self.playwright = await async_playwright().start()

        # First try to connect to an existing Chrome
        try:
            self.browser = await self.playwright.chromium.connect_over_cdp(
                self.CDP_URL,
                timeout=1000,
            )
            self._owns_browser = False

        except Exception:
            try:
                import os
                chrome_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
                # No debugging Chrome found → launch our own browser
                self.browser = await self.playwright.chromium.launch(
                    executable_path=self.chrome_path,
                    headless=self.headless,
                )
                self._owns_browser = True
            except Exception: #else just launch normally
                self.browser = await self.playwright.chromium.launch(headless=self.headless)
                self._owns_browser = True
        return self.browser

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Only close a browser that we launched ourselves.
        if self.browser and self._owns_browser:
            await self.browser.close()

        if self.playwright:
            await self.playwright.stop()
