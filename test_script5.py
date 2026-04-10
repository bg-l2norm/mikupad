import asyncio
from playwright.async_api import async_playwright
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000/mikupad.html')
        await page.wait_for_selector('#prompt-area')

        # Get defaultTemplates instead
        script = await page.evaluate("() => JSON.stringify(defaultTemplates)")
        templates = json.loads(script)
        mistral = templates.get("Mistral")

        print("Mistral Template:", mistral)

        await browser.close()

asyncio.run(main())
