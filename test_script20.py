import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        await page.wait_for_timeout(500)

        mistral_text = "<<SYS>>\nSystem text here<</SYS>>\n\n</s>[INST]User text here[/INST]"
        await page.fill('#prompt-area', mistral_text)

        await page.wait_for_timeout(500)

        # Unhide is already the default state. Let's just click hide and verify the bug.

        print("Wait, what if we type into the textarea using 'insertText' like the browser does?")

        await browser.close()

asyncio.run(main())
