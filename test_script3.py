import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        # Type some text without selecting an explicit template.
        await page.fill('#prompt-area', '[SYS]\nSystem text here[/SYS]\n[INST]\nUser text here[/INST]')

        await page.wait_for_timeout(500)

        # Click the "Hide Chat Templates" button
        await page.click('[title="Hide Chat Templates"]')

        await page.wait_for_timeout(500)

        # Check the text area content
        content = await page.input_value('#prompt-area')
        print("Content after hide:", repr(content))

        # Click "Show Chat Templates"
        await page.click('[title="Show Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after unhide:", repr(content))

        await browser.close()

asyncio.run(main())
