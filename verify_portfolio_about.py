import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local index.html file
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # Click on 'About' just in case (though it's usually default)
        await page.click("button:has-text('About')")
        await asyncio.sleep(1)

        # Take a screenshot of the About section (including Services)
        await page.screenshot(path="verification/portfolio_about.png", full_page=True)

        # Verify Services
        services = ["Web Development", "Private Coding Tutor", "Custom Software Solutions", "Translation Services"]
        for service in services:
            if await page.get_by_role("heading", name=service).count() > 0:
                print(f"Service found: {service}")
            else:
                # If not a heading, maybe just text
                if await page.get_by_text(service).count() > 0:
                     print(f"Service text found: {service}")
                else:
                     print(f"Service NOT found: {service}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
