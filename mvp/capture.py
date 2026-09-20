import asyncio, sys
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8099/mvp/index.html"
OUT = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\mvp\shots"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        # phone
        pg = await b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
        await pg.goto(URL, wait_until="networkidle")
        await pg.wait_for_timeout(800)
        await pg.screenshot(path=f"{OUT}/01_landing.png", full_page=True)
        await pg.click("#v-landing .cta")
        await pg.fill("#nm", "Ramesh")
        await pg.click("#useSample")
        await pg.click("#scanBtn")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=f"{OUT}/02_fill_ocr.png", full_page=True)
        await pg.click("#expBtn")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=f"{OUT}/03_result.png", full_page=True)
        await pg.click('#tabbar button[data-go="fill"]')
        await pg.click("#addBtn")
        await pg.click("#expBtn")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=f"{OUT}/04_alert.png", full_page=True)
        await pg.click('#tabbar button[data-go="suvidha"]')
        await pg.fill("#jaq", "metformin")
        await pg.fill("#abq", "delivery")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=f"{OUT}/05_suvidha.png", full_page=True)
        await pg.click("#menuBtn")
        await pg.wait_for_timeout(400)
        await pg.screenshot(path=f"{OUT}/06_drawer.png")
        # desktop device sandbox
        pg2 = await b.new_page(viewport={"width": 1400, "height": 900})
        await pg2.goto(URL, wait_until="networkidle")
        await pg2.wait_for_timeout(800)
        await pg2.screenshot(path=f"{OUT}/07_desktop.png")
        await b.close()
        print("shots done")

asyncio.run(main())
