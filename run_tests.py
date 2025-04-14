import os
import subprocess
import argparse
from datetime import datetime

def run_tests(test_file=None, report_name=None):
    """
    執行測試並生成報告
    
    Args:
        test_file (str, optional): 指定要執行的測試文件。如果為 None，則執行所有測試。
        report_name (str, optional): 指定報告名稱。如果為 None，則使用時間戳。
    """
    # 創建報告資料夾
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # 生成報告文件名
    if report_name:
        report_file = os.path.join(reports_dir, f"{report_name}.html")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(reports_dir, f"report_{timestamp}.html")

    # 構建 pytest 命令
    pytest_cmd = [
        "pytest",
        f"--html={report_file}",
        "--self-contained-html",
        "--capture=sys",
        "--verbose",
        "-v"
    ]

    # 加入測試文件（如果指定）
    if test_file:
        pytest_cmd.append(test_file)

    # 執行測試並生成報告
    subprocess.run(pytest_cmd)

    print(f"\n測試報告已生成: {report_file}")

def main():
    parser = argparse.ArgumentParser(description='執行 RentJoy UI 自動化測試')
    parser.add_argument('--test', '-t', help='指定要執行的測試文件')
    parser.add_argument('--report', '-r', help='指定報告名稱')
    parser.add_argument('--batch', '-b', action='store_true', help='執行批次測試')
    
    args = parser.parse_args()

    if args.batch:
        # 批次執行所有測試文件
        test_files = [
            "tests/test_basic.py",
            # 於此加入更多測試文件
        ]
        for test_file in test_files:
            print(f"\n執行測試: {test_file}")
            run_tests(test_file=test_file, report_name=os.path.basename(test_file).replace('.py', ''))
    else:
        # 單次執行指定或所有測試
        run_tests(test_file=args.test, report_name=args.report)

if __name__ == "__main__":
    main() 