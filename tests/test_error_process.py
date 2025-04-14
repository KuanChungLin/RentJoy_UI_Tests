from playwright.sync_api import Page, expect
from .pages.login_process import LoginPage
from .pages.search_process import SearchPage
from .pages.reserve_process import ReservePage
from .pages.reserve_detail_process import ReserveDetailPage
from .pages.ecpay_process import EcpayProcess
from urllib.parse import urlparse, parse_qs

def test_process(page: Page):
    # 網站首頁
    page.goto("https://rentjoy-test.azurewebsites.net/")
    
    # 等待頁面載入
    page.wait_for_load_state("networkidle")
    
    # 驗證網頁標題
    expect(page).to_have_title("Home Page - RentJoy.Web")
    
    # 執行搜尋場地流程
    search_page = SearchPage(page)
    search_page.search()
    
    # 執行場地頁面預訂時間流程
    reserve_page = ReservePage(page)
    reserve_page.process_reserve()

    # 執行登入帳號流程
    login_page = LoginPage(page)
    login_page.login()
