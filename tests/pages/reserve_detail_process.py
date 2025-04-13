from playwright.sync_api import Page
from tests.utils.page_utils import PageUtils

class ReserveDetailPage:
    def __init__(self, page: Page):
        self.page = page

    def option_click(self, select_name: str, option_number: str):
        """選擇下拉選單選項"""
        # 方法1：使用 select 元素的 value 屬性
        try:
            select = self.page.locator(f"select[name='{select_name}']").first
            select.select_option(index=int(option_number) - 1)
            return
        except Exception as e:
            print(f"方法1失敗: {e}")

        # 方法2：使用 JavaScript 直接設置值
        try:
            self.page.evaluate(f"""
                document.querySelector("select[name='{select_name}']").value = '{option_number}';
                document.querySelector("select[name='{select_name}']").dispatchEvent(new Event('change'));
            """)
            return
        except Exception as e:
            print(f"方法2失敗: {e}")

        # 方法3：模擬鍵盤操作
        try:
            select = self.page.locator(f"select[name='{select_name}']").first
            select.click()
            self.page.keyboard.press("ArrowDown")
            for _ in range(int(option_number) - 1):
                self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
            return
        except Exception as e:
            print(f"方法3失敗: {e}")

        # 如果所有方法都失敗，拋出異常
        raise Exception("無法選擇下拉選單選項")

    def process_reserve_detail(self):
        """執行預訂詳情填寫流程"""
        # 選擇活動類型
        activity_select = self.page.locator("select[name='Activity']").first
        activity_select.click()
        self.option_click("Activity", "2")

        # 點擊確認勾選框
        confirm_check = self.page.locator("div.checkmark").first
        PageUtils.scroll_to_element(self.page, confirm_check)
        confirm_check.click()

        # 點擊下一步按鈕
        next_step_btn = self.page.locator("input#nextStepBtn").first
        PageUtils.scroll_to_element(self.page, next_step_btn)
        next_step_btn.click()

        # 等待頁面加載
        PageUtils.wait_for_network_idle(self.page)

        # 填寫表單
        # 姓氏
        last_name_input = self.page.locator("input[name='LastName']").first
        last_name_input.fill("林")

        # 名字
        first_name_input = self.page.locator("input[name='FirstName']").first
        first_name_input.fill("阿河")

        # 電話
        phone_input = self.page.locator("input[name='Phone']").first
        phone_input.fill("0900000000")

        # 電子郵件
        email_input = self.page.locator("input[name='Email']").first
        email_input.fill("test1@gmail.com")

        # 點擊提交按鈕
        submit_button = self.page.locator("button#submitBtn").first
        PageUtils.scroll_to_element(self.page, submit_button)
        submit_button.click()

        # 等待頁面加載
        PageUtils.wait_for_network_idle(self.page)