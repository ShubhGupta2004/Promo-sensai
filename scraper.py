import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse, parse_qs, unquote
import json

def clean_url(tracking_url):
    if not tracking_url:
        return None
    
    parsed = urlparse(tracking_url)
    query_params = parse_qs(parsed.query)
    
    if 'url' in query_params:
        return unquote(query_params['url'][0])
    return tracking_url

async def scrape_deals():
    deals = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to deals page
        await page.goto("https://www.grabon.in/deals/", wait_until="domcontentloaded")
        await page.wait_for_selector(".g-deal", timeout=10000)
        
        # Extract deals
        deal_elements = await page.locator(".g-deal").all()
        for element in deal_elements:
            try:
                # Get deal details
                title = await element.get_attribute("data-dealtitle")
                url = await element.get_attribute("data-dealurl")
                price = await element.get_attribute("data-afterprice")
                merchant = await element.get_attribute("data-dmname")
                discount = await element.locator("span").first.text_content()
                
                if title:
                    deals.append({
                        "title": title,
                        "description": title,
                        "deal_url": clean_url(url),
                        "brand_merchant": merchant,
                        "price": float(price) if price else None,
                        "discount": discount.strip()
                    })
            except Exception:
                continue
                
        await browser.close()
    return deals

def get_deals():
    deals = asyncio.run(scrape_deals())
    with open('offers.json', 'w') as f:
        json.dump(deals, f, indent=2)
    return deals

if __name__ == "__main__":
    get_deals()
