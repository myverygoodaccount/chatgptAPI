import requests
import playwright
import asyncio

'''
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, )
    page = browser.new_page()
    
    kahootCode = ""
    page.goto("https://kahoot.it")
    
    
    #browser.close()
''' 
    
import os
import time
import threading
from playwright.sync_api import sync_playwright

chrome_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
)


a = "document.querySelector('#_r_36_')"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    page = browser.new_page()
    
    page.goto(f"https://kahoot.it")
    
    
    inp = input("kahoot code: ")
    #page.click(position=(100,100))
    time.sleep(1)
    #//*[@id="_r_8_"]
    #<input placeholder="Enter PIN" inputmode="numeric" aria-invalid="false" id="_r_8_" data-functional-selector="game-pin-input" class="game-input__GameInput-sc-mmat23-2 izKRqY enter-pin-form__GameInput-sc-n5kf07-0 decIfN" autocomplete="off" dir="auto" value="" name="gameId">
    #_r_8_
    
    #page.query_selector("#_R_36_").fill(inp)
    
    time.sleep(1)
    #page.query_selector("#root > div.app__AppWrapper-sc-c94bpl-0.dTqLyh > div > div > div.background__Background-sc-7xwc88-0.ctKtra.page-wrapper__Background-sc-ocvjvt-0.dQyMAK > div > div.game-id__SecondWrapper-sc-8omzir-1.eIyxOL > div.vertical-alignment__VerticalAlignment-sc-9hefpt-0.kKOQzR > main > div > form > button").click()
    #document.querySelector("#root > div.app__AppWrapper-sc-c94bpl-0.dTqLyh > div > div > div.background__Background-sc-7xwc88-0.ctKtra.page-wrapper__Background-sc-ocvjvt-0.dQyMAK > div > div.game-id__SecondWrapper-sc-8omzir-1.eIyxOL > div.vertical-alignment__VerticalAlignment-sc-9hefpt-0.kKOQzR > main > div > form > button")
    #root > div.app__AppWrapper-sc-c94bpl-0.dTqLyh > div > div > div.background__Background-sc-7xwc88-0.ctKtra.page-wrapper__Background-sc-ocvjvt-0.dQyMAK > div > div.game-id__SecondWrapper-sc-8omzir-1.eIyxOL > div.vertical-alignment__VerticalAlignment-sc-9hefpt-0.kKOQzR > main > div > form > button
    
    
    
    #print(page.title())

    #browser.close()
    stop = threading.Event()

    def wait_for_close():
        input("Press Enter to close: ")
        stop.set()

    threading.Thread(target=wait_for_close, daemon=True).start()

    # Keep the Playwright thread alive
    stop.wait()

    browser.close()


from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

#asyncio.run(main())