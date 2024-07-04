import allure
from playwright.sync_api import sync_playwright


def take_screenshot(page, name):
    with allure.step(f"Take screenshot: {name}"):
        page.screenshot(path=f"{name}.png")
        allure.attach.file(f"{name}.png", attachment_type=allure.attachment_type.PNG)
