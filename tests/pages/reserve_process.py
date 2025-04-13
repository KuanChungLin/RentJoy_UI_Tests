from playwright.sync_api import Page
from tests.utils.page_utils import PageUtils

class ReservePage:
    def __init__(self, page: Page):
        self.page = page
        
    def select_date(self):
        """選擇可用的日期"""
        col_sort = 1
        while True:
            # 查找可用的日期元素
            date_element = self.page.locator(f"(//div[@class='col']//div[contains(@class,'date') and not(contains(@class,'text-decoration-line-through'))])[{col_sort}]").first
            
            # 如果找不到元素，跳出循環
            if not date_element.is_visible():
                break
                
            # 滾動到元素並點擊
            PageUtils.scroll_to_element(self.page, date_element)
            date_element.click()
            
            # 等待 1 秒
            self.page.wait_for_timeout(1000)
            
            # 檢查是否還有無選項的時間段
            no_options = self.page.locator("//div[@class='time-period no-options d-flex' and not(ancestor::div[@id='footerCalenderModal'])]")
            if not no_options.is_visible():
                break
                
            col_sort += 1

    def select_time_period(self):
        """選擇時間段"""
        try:
            # 選擇開始時間
            start_time_button = self.page.locator("//div[contains(@class, 'start-time')]/button[contains(@class, 'start')]").first
            PageUtils.scroll_to_element(self.page, start_time_button)
            start_time_button.click()

            start_time_option = self.page.locator("//div[contains(@class, 'start-time')]/ul[contains(@class, 'start-menu')]/li[1]").first
            PageUtils.scroll_to_element(self.page, start_time_option)
            start_time_option.click()

            # 選擇結束時間
            end_time_button = self.page.locator("//div[contains(@class, 'end-time')]/button[contains(@class, 'end')]").first
            PageUtils.scroll_to_element(self.page, end_time_button)
            end_time_button.click()

            end_time_option = self.page.locator("//div[contains(@class, 'end-time')]/ul[contains(@class, 'end-menu')]/li[2]").first
            PageUtils.scroll_to_element(self.page, end_time_option)
            end_time_option.click()

            # 點擊預訂按鈕
            order_button = self.page.locator("//div[contains(@class, 'reserved')]/a[contains(@class, 'btn')]").first
            PageUtils.scroll_to_element(self.page, order_button)
            order_button.click()

        except Exception:
            # 如果出現錯誤，嘗試使用備選方案
            select_time_button = self.page.locator("(//div[contains(@class, 'time-period-select')]/div[contains(@class, 'select-time')])[1]").first
            PageUtils.scroll_to_element(self.page, select_time_button)
            select_time_button.click()

            order_button = self.page.locator("//div[contains(@class, 'reserved')]/a[contains(@class, 'btn')]").first
            PageUtils.scroll_to_element(self.page, order_button)
            order_button.click()

    def process_reserve(self):
        """執行完整的訂單流程"""
        # 選擇日期
        self.select_date()
        
        # 選擇時間段
        self.select_time_period()
        
        # 等待頁面加載
        PageUtils.wait_for_network_idle(self.page) 