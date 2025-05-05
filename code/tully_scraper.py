import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    #main function to scrape Tully's menu
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    menu_items = []

#select all menu sections by CSS selector
    sections = page.locator('.menu-section') #this is a placeholder CSS selector

    for section in sections:
        title = section.locator('.section-title').inner_text() #grab the title of the section
        menu_items_data = section.locator('.row').inner_text() #grab all items under this section

        #process each menu item
        items = menu_items_data.split("\n")
        for item_text in items:
            menu_item = extract_menu_item(title, item_text)
            menu_items.append(menu_item.to_dict())
   
    #convert lists of dicts into a DataFrame and save it as a CSV
    df = pd.DataFrame(menu_items)
    df.to_csv("cache/tullys_menu.csv", index=False)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
