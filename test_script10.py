import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        await page.wait_for_timeout(500)

        # Select another template, like Alpaca
        await page.select_option('select[title="Instruct Template"]', label='Alpaca')

        await page.wait_for_timeout(500)

        alpaca_text = "### System:\nSystem text here\n\n### Instruction:\nUser text here\n\n### Response:"
        await page.fill('#prompt-area', alpaca_text)

        await page.wait_for_timeout(500)

        await page.click('[title="Hide Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after hide (Alpaca):", repr(content))

        await page.type('#prompt-area', ' abc')

        await page.wait_for_timeout(500)
        content = await page.input_value('#prompt-area')
        print("Content after typing (Alpaca):", repr(content))

        await page.click('[title="Show Chat Templates"]')

        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after unhide (Alpaca):", repr(content))

        await browser.close()

asyncio.run(main())
