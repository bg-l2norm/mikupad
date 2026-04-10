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

        # Hide templates
        await page.click('[title="Hide Chat Templates"]')
        await page.wait_for_timeout(500)

        # Look for system prompt textarea
        sys_prompt = await page.input_value('#system-prompt-area')
        print("System prompt area content:", repr(sys_prompt))

        # Modify the system prompt area
        await page.fill('#system-prompt-area', 'Modified system text')
        await page.wait_for_timeout(500)

        # Show templates
        await page.click('[title="Show Chat Templates"]')
        await page.wait_for_timeout(500)

        content = await page.input_value('#prompt-area')
        print("Content after unhide with modified system prompt:", repr(content))

        await browser.close()

asyncio.run(main())
