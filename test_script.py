import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        # Select "Llama 3" template maybe? Or just Chat mode?
        # Let's type some text.
        await page.fill('#prompt-area', '<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nSystem text here<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nUser text here<|eot_id|>')

        # Wait a bit for state to update
        await page.wait_for_timeout(1000)

        # Click the "Hide Chat Templates" button
        # title="Hide Chat Templates"
        await page.click('[title="Hide Chat Templates"]')

        await page.wait_for_timeout(1000)

        # Check the text area content
        content = await page.input_value('#prompt-area')
        print("Content after hide:", repr(content))

        # Click "Show Chat Templates"
        await page.click('[title="Show Chat Templates"]')

        await page.wait_for_timeout(1000)

        content = await page.input_value('#prompt-area')
        print("Content after unhide:", repr(content))

        await browser.close()

asyncio.run(main())
