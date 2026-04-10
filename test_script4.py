import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        await page.wait_for_timeout(500)

        # We need to find the correct select for template. Let's inspect the options.
        # Let's type some text.
        await page.fill('#prompt-area', '[SYS]\nSystem text here[/SYS]\n[INST]\nUser text here[/INST]')

        await page.wait_for_timeout(500)

        # Click the "Hide Chat Templates" button
        # Oh, if we just type text that contains Mistral (the default) template.
        # What is the Mistral template? It's "[INST]" and "[/INST]" and "[SYS]"...? Actually we need to check default Mistral template.
        pass

        await browser.close()

asyncio.run(main())
