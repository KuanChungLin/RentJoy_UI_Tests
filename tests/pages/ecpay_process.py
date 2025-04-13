from playwright.sync_api import Page, expect
from tests.utils.page_utils import PageUtils
import time

class EcpayProcess:
    def __init__(self, page: Page):
        self.page = page

    def ecpay_input(self, input_id: str, number: str):
        """輸入綠界支付表單資料"""
        input_element = self.page.locator(f"input#{input_id}").first
        PageUtils.scroll_to_element(self.page, input_element)
        
        # 逐字輸入數字以避免未成功輸入的問題
        for char in number:
            input_element.type(char)
            time.sleep(0.1)

    def process(self):
        """執行綠界支付流程"""
        # 輸入信用卡號
        self.ecpay_input("CCpart1", "4311")
        self.ecpay_input("CCpart2", "9522")
        self.ecpay_input("CCpart3", "2222")
        self.ecpay_input("CCpart4", "2222")

        # 輸入信用卡到期日
        self.ecpay_input("creditMM", "12")
        self.ecpay_input("creditYY", "30")

        # 輸入信用卡安全碼
        self.ecpay_input("CreditBackThree", "222")

        # 輸入手機號碼
        self.ecpay_input("CellPhoneCheck", "0900000000")

        # 點擊提交按鈕
        pay_submit_button = self.page.locator("div.scw-btn-block a#CreditPaySubmit").first
        PageUtils.scroll_to_element(self.page, pay_submit_button)
        pay_submit_button.click()

        # 點擊關閉按鈕
        close_button = self.page.locator("div.simplert.simplert--shown button#btnClose").first
        PageUtils.scroll_to_element(self.page, close_button)
        close_button.click()

        # 等待2秒
        time.sleep(2)

        # 再次點擊提交按鈕
        pay_submit_button.click()

        # 點擊確認按鈕
        confirm_button = self.page.locator("div.simplert.simplert--shown button#btnConfirm").first
        confirm_button.click()

        # 等待並點擊獲取OTP按鈕
        get_otp_button = self.page.locator("#GetOTPPwd").first
        get_otp_button.wait_for(state="visible")
        get_otp_button.click()

        # 輸入OTP
        self.ecpay_input("OTP", "1234")

        # 等待並點擊發送OTP按鈕
        otp_send_button = self.page.locator("#OTPSend").first
        otp_send_button.wait_for(state="visible")
        otp_send_button.click()

        # 等待並點擊訂單狀態
        order_state = self.page.locator(".order-state").first
        order_state.wait_for(state="visible")
        order_state.click()
