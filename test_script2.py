import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        # Select "Llama 3" template maybe?
        # Actually we need to select a template from the dropdown to make sure hide chat templates matches affixes.
        await page.select_option('select[title="Select a template"]', label='Llama 3')

        await page.wait_for_timeout(500)

        await page.fill('#prompt-area', '<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nSystem text here<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nUser text here<|eot_id|>')

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
