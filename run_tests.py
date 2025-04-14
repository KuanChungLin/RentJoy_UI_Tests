import os
import subprocess
from datetime import datetime

def run_tests():
    # 創建報告資料夾
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # 生成報告文件名（包含時間戳）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(reports_dir, f"report_{timestamp}.html")

    # 構建 pytest 命令
    pytest_cmd = [
        "pytest",
        "tests/test_basic.py",
        f"--html={report_file}",
        "--self-contained-html",
        "--capture=sys",
        "--verbose",
        "-v"
    ]

    # 執行測試並生成報告
    subprocess.run(pytest_cmd)

    print(f"\n測試報告已生成: {report_file}")

if __name__ == "__main__":
    run_tests() 