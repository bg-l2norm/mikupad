import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        await page.wait_for_timeout(500)

        await page.click('[title="Hide Chat Templates"]')

        await page.wait_for_timeout(500)

        # In hide chat templates mode, writing full raw prompt structure is not expected (since it's supposed to be clean).
        # So we write some user text.
        await page.fill('#prompt-area', 'User text here')

        await page.wait_for_timeout(500)

        # Then unhide
        await page.click('[title="Show Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after unhide:", repr(content))

        await browser.close()

asyncio.run(main())
