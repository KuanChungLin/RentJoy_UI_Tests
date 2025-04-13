from playwright.sync_api import Page, Locator

class PageUtils:
    @staticmethod
    def scroll_to_element(page: Page, element: Locator):
        """滾動到指定元素並等待
        
        Args:
            page: Playwright 頁面對象
            element: 要滾動到的元素
        """
        # 滾動到元素
        element.scroll_into_view_if_needed()
        
        # 等待 1 秒
        page.wait_for_timeout(1000)

    @staticmethod
    def wait_for_element(page: Page, selector: str, timeout: int = 5000):
        """等待元素出現
        
        Args:
            page: Playwright 頁面對象
            selector: 元素選擇器
            timeout: 等待超時時間（毫秒）
        """
        page.wait_for_selector(selector, timeout=timeout)

    @staticmethod
    def wait_for_network_idle(page: Page):
        """等待網絡請求完成
        
        Args:
            page: Playwright 頁面對象
        """
        page.wait_for_load_state("networkidle") 