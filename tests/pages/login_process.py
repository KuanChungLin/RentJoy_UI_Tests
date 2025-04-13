from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.locator("a[name='LoginJump']")
        self.account_input = page.locator("input[name='Account']")
        self.password_input = page.locator("input[name='Password']")
        self.submit_button = page.locator("button.login-btn")

    def login(self):
        # 點擊登入按鈕
        self.login_button.click()

        # 輸入帳號
        self.account_input.fill("test1@gmail.com")

        # 輸入密碼
        self.password_input.fill("Ab12345")

        # 點擊登入按鈕
        self.submit_button.click()

        # 等待頁面加載完成
        self.page.wait_for_load_state("networkidle")

        # 驗證登入後的頁面
        expect(self.page).to_have_url("https://rentjoy-test.azurewebsites.net/")