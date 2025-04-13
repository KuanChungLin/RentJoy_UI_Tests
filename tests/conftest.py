import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # 啟動 Playwright
    with sync_playwright() as p:
        # 啟動瀏覽器（設置為非無頭模式，方便觀察）
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    # 創建新的上下文
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        screen={"width": 1920, "height": 1080}
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    # 創建新的頁面
    page = context.new_page()
    yield page
    page.close() 