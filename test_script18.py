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

        # Test just toggling hide and show
        await page.click('[title="Hide Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after hide:", repr(content))

        # Now show again. Should restore the system prompt.
        await page.click('[title="Show Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after unhide:", repr(content))

        await browser.close()

asyncio.run(main())
