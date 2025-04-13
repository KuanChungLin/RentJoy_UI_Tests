from playwright.sync_api import Page, expect

class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    # 選擇下拉選單選項選擇下拉選單選項
    def option_click(self, select_name: str, select_id: str, option_number: str):
        """選擇下拉選單選項"""
        # 方法1：使用 select 元素的 value 屬性
        try:
            select = self.page.locator(f"select[name='{select_name}'][id='{select_id}']").first
            select.select_option(index=int(option_number) - 1)
            return
        except Exception as e:
            print(f"方法1失敗: {e}")

        # 方法2：使用 JavaScript 直接設置值
        try:
            self.page.evaluate(f"""
                document.querySelector("select[name='{select_name}'][id='{select_id}']").value = '{option_number}';
                document.querySelector("select[name='{select_name}'][id='{select_id}']").dispatchEvent(new Event('change'));
            """)
            return
        except Exception as e:
            print(f"方法2失敗: {e}")

        # 方法3：模擬鍵盤操作
        try:
            select = self.page.locator(f"select[name='{select_name}'][id='{select_id}']").first
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

    # 執行搜尋流程
    def search(self):
        """執行搜索流程"""
        # 選擇活動類型
        self.option_click("ActivityId", "activity_select", "3")

        # 選擇城市
        self.option_click("City", "citySelect", "3")

        # 選擇人數
        self.option_click("NumberOfPeople", "people_select", "11")

        # 點擊搜索按鈕
        search_button = self.page.locator("button.btn-orange").first
        search_button.click()

        # 等待搜索結果加載
        self.page.wait_for_load_state("networkidle")

        # 點擊第一個搜索結果
        first_result = self.page.locator("a.product-imga").first
        first_result.click()

        # 等待頁面加載
        self.page.wait_for_load_state("networkidle")

        # 驗證搜索結果頁面
        expect(self.page).to_have_url("https://rentjoy-test.azurewebsites.net/Venues/VenuesPage?venueId=4")
