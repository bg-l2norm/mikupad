import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # we will record a video to visually inspect
        context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        await page.wait_for_timeout(500)

        # Change template to Mistral
        mistral_text = "<<SYS>>\nSystem text here<</SYS>>\n\n</s>[INST]User text here[/INST]"
        await page.fill('#prompt-area', mistral_text)

        await page.wait_for_timeout(500)

        # Hide templates
        await page.click('[title="Hide Chat Templates"]')
        await page.wait_for_timeout(500)

        # Type in the hidden mode
        await page.type('#prompt-area', ' Typing hidden text.')
        await page.wait_for_timeout(500)

        # Modify the system prompt area
        await page.fill('#system-prompt-area', 'Modified system text')
        await page.wait_for_timeout(500)

        # Show templates
        await page.click('[title="Show Chat Templates"]')
        await page.wait_for_timeout(500)

        # Take a screenshot
        await page.screenshot(path="screenshot.png")

        await context.close()
        await browser.close()

asyncio.run(main())
