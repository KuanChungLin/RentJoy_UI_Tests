# RentJoy UI 自動化測試專案

這是一個使用 Playwright 框架開發的 UI 自動化測試專案，用於測試 RentJoy 網站的各項功能。

## 專案結構

```
RentJoy-UI-Tests/
├── tests/                      # 測試相關檔案
│   ├── pages/                 # 頁面物件模型
│   │   ├── ecpay_process.py   # 綠界支付流程
│   │   ├── login_process.py   # 登入流程
│   │   ├── reserve_process.py   # 預訂場地處理流程
│   │   ├── reserve_detail_process.py  # 預訂場地資料填寫流程
│   │   └── search_process.py  # 搜尋流程
│   ├── utils/                 # 工具類
│   │   └── page_utils.py      # 頁面操作工具
│   ├── conftest.py           # pytest 設定檔
│   └── test_basic.py         # 主要測試案例
├── .pytest_cache/            # pytest 快取資料夾
├── __pycache__/             # Python 編譯快取
├── state.json               # 瀏覽器狀態儲存檔
└── requirements.txt         # 專案依賴套件
```

## 檔案說明

### 測試頁面物件 (tests/pages/)
- `ecpay_process.py`: 處理綠界支付流程，包含信用卡資訊輸入、OTP 驗證等
- `login_process.py`: 處理使用者登入流程
- `reserve_process.py`: 處理預訂場地時間日期相關操作
- `reserve_detail_process.py`: 處理預訂詳情資料填寫流程
- `search_process.py`: 處理場地搜尋流程

### 工具類 (tests/utils/)
- `page_utils.py`: 提供常用的頁面操作工具，如滾動、等待等

### 設定檔
- `conftest.py`: pytest 設定檔，包含：
  - 瀏覽器設定（視窗大小、啟動參數）
  - 基礎 URL 設定
  - 儲存狀態設定
  - 共用 fixture 定義

### 主要測試檔案
- `test_basic.py`: 主要的測試案例，整合了所有頁面物件的測試流程

## 環境需求

- Python 3.8+
- Playwright
- 其他依賴套件（詳見 requirements.txt）

## 環境設置步驟

### 1. Clone專案
```bash
git clone [專案URL]
cd RentJoy-UI-Tests
```

### 2. 創建虛擬環境
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 3. 啟動虛擬環境
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 4. 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 5. 安裝 Playwright 瀏覽器
```bash
playwright install
```

## 執行測試

執行測試流程：
```bash
pytest tests/test_basic.py
```

## 注意事項

- `.pytest_cache/` 和 `__pycache__/` 是自動生成的快取資料夾，可以安全刪除
- `state.json` 用於儲存瀏覽器狀態，建議加入 `.gitignore`
- 測試執行時會開啟瀏覽器視窗，可以通過修改 `conftest.py` 中的 `headless` 參數來控制
- 每次更新專案後，建議執行 `pip install -r requirements.txt` 確保依賴套件是最新的

## 開發指南

1. 新增頁面物件：
   - 在 `tests/pages/` 下創建新的 Python 檔案
   - 繼承基本頁面類別
   - 實現頁面特定的操作方法

2. 新增測試案例：
   - 在 `test_basic.py` 中添加新的測試函數
   - 使用現有的頁面物件進行測試

3. 修改設定：
   - 編輯 `conftest.py` 修改共用設定
   - 編輯 `requirements.txt` 更新依賴套件

4. 提交更改：
   - 確保 `venv` 資料夾在 `.gitignore` 中
   - 更新 `requirements.txt` 如果有新增依賴
   - 提交前執行測試確保功能正常 