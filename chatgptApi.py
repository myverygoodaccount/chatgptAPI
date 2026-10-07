import requests
import asyncio
import subprocess
import os
import time
import threading
from playwright.sync_api import sync_playwright

chrome_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
)


CDP_URL = "http://127.0.0.1:9222"


def chrome_available():
    try:
        return requests.get(
            f"{CDP_URL}/json/version",
            timeout=0.2
        ).ok
    except requests.RequestException:
        return False
    
    
    
    

a = "document.querySelector('#_r_36_')"

with sync_playwright() as p:
    browser = None
    
    
    if chrome_available():
        browser = p.chromium.connect_over_cdp(CDP_URL)
    else:
        subprocess.Popen([
            chrome_path,
            "--remote-debugging-port=9222",
            "--disable-extensions",
            "--disable-background-networking",
        ])
        
        for _ in range(100):
            if chrome_available():
                break
            time.sleep(0.2)
            
        browser = p.chromium.connect_over_cdp(CDP_URL)
    
    
    
    
    
    #browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    page = browser.new_page()
    
    page.goto(f"https://chatgpt.com", timeout=60000)
    
    
    inp = input("ask gpt: ")

    page.mouse.click(742, 381)

    page.wait_for_timeout(1)
    
    #page.query_selector("#_R_36_").fill(inp)
    page.mouse.click(742, 381)

    
    textarea = page.query_selector("#mobile-composer-prompt")

    textarea.focus()

    #textarea.value = inp
    textarea.input_value(inp)
    #await
    textarea.dispatch_event("input", {"bubbles": True})

    page.locator('button[data-composer-submit][aria-label="Send message"]').click()
    #page.get_by_role("button", name="Send message").click()
    
    '''
    1) <button type="submit" data-icon-only="" data-radius="full" data-size="medium" data-oai-tooltip="" aria-disabled="true" data-variant="primary" data-composer-submit="" aria-label="Send message" data-visually-disabled="" data-w-component="button" data-icon-position="start" data-icon-shape="non-circular" data-oai-tooltip-side="bottom" data-send-label="Send message" data-stop-label="Stop generating" data-octane-bindings="d:c95d6a90" class="xlpm8z4 xxyica1 x1cpjm7i x1dxl39w x1hmns74 xjbqb8w xn3w4p2 xnvt7iq …>…</button> aka get_by_role("button", name="Send message")
    2) <button tabindex="-1" type="submit" value="backdrop" aria-label="Dismiss" data-bottom-sheet-dismiss-button="" class="xjyslct xjbqb8w x5yr21d xu82sp8 xh8yej3 x1717udv"></button> aka get_by_label("Clear current chat?").get_by_label("Dismiss")
    3) <button type="submit" data-icon-only="" aria-label="Close" data-radius="full" data-size="medium" data-variant="ghost" data-w-component="but
    '''
    
    
    page.evaluate("""
    () => {
        document.addEventListener('click', e => {
            console.log(`CLICK: x=${e.clientX}, y=${e.clientY}`);
        });
    }
    """)

    
    
    time.sleep(1)
    
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




'''
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

#asyncio.run(main())
'''

'''
document.querySelector("#mobile-composer-prompt").value = "hi \n"
document.querySelector("#web-mobile-root > div > main > div > div.x5yr21d.xrvj5dj.x67ebes.xh8yej3.x1o0tod.x2lwn1j.xeuugli.x7giv3.x7wzq59.x1vjfegm.xwms9i0.x1u6ievf.x7fofa6.xtgieia.x19s4qmo.x13c060r.x1esw782 > div > div > div > div > div.x172wjan.xabbh08.x4z00pl.x1hnil0i.x3j6cwj.x1dc41vb.x1frdjf4.x4f1b6v.x178on7p.x46cnko.xadup9s.xivmg67.xpd13jm.x6a7w3q.xztv9e7.xudtftn.xh8yej3.xvueqy4.x193iq5w.xtgm0af.x1bbat7l.x17po7al.xrm5kiu.xqxn4yg.xihj1zt.x83h6r0.x1n2onr6.x3lm4xc.x15rfrr.x18hqigf.xusb7v9.x1oge7uf.xwkhwih.x1bilc9u.x1pnycol.x1roalzr.xj6zwfq.x1uss67b.x1v2d32w.xe9yzev.x34ol0i > div.x1hmns74.xy5mcqj.xkeh78v.x17r8v38.xnahlnb.xr1uyzm.xkk1bqk.x1fw5fud.x8e1do1.xtikakg.xnq4lqx.x1n2onr6.x9ts1ie.x1355zze.x1hh5tl3.xwztkqq.x8q0l7n.xmx4vpt.x18lq4fh > div > div > div > form").click()


const but = document.querySelector("#web-mobile-root > div > main > div > div.x5yr21d.xrvj5dj.x67ebes.xh8yej3.x1o0tod.x2lwn1j.xeuugli.x7giv3.x7wzq59.x1vjfegm.xwms9i0.x1u6ievf.x7fofa6.xtgieia.x19s4qmo.x13c060r.x1esw782 > div > div > div > div > div.x172wjan.xabbh08.x4z00pl.x1hnil0i.x3j6cwj.x1dc41vb.x1frdjf4.x4f1b6v.x178on7p.x46cnko.xadup9s.xivmg67.xpd13jm.x6a7w3q.xztv9e7.xudtftn.xh8yej3.xvueqy4.x193iq5w.xtgm0af.x1bbat7l.x17po7al.xrm5kiu.xqxn4yg.xihj1zt.x83h6r0.x1n2onr6.x3lm4xc.x15rfrr.x18hqigf.xusb7v9.x1oge7uf.xwkhwih.x1bilc9u.x1pnycol.x1roalzr.xj6zwfq.x1uss67b.x1v2d32w.xe9yzev.x34ol0i > div.x1hmns74.xy5mcqj.xkeh78v.x17r8v38.xnahlnb.xr1uyzm.xkk1bqk.x1fw5fud.x8e1do1.xtikakg.xnq4lqx.x1n2onr6.x9ts1ie.x1355zze.x1hh5tl3.xwztkqq.x8q0l7n.xmx4vpt.x18lq4fh > div > div > div > form")

const t = document.querySelector("#mobile-composer-prompt")

t.focus()

t.value = "yoo"

t.dispatchEvent(new Event('input', {bubbles: true}));

but.click()
'''