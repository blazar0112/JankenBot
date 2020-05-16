# JankenBot

Bot to auto select janken of event [bjm2020](https://p.eagate.573.jp/game/bemani/bjm2020/index.html) everyday.

## Getting Started

下載 jankenbot.py

先看 Prerequisites 準備好前置需求

在 jankenbot.py 資料夾 Shift+按右鍵 -> 在這裡開啟 PowerShell (Win10) / 命令提示(即CMD, Win7) 視窗

PowerShell視窗輸入  python.exe .\jankenbot.py 按 ENTER

會跳出一個 Chrome 視窗, 'Chrome目前受到自動測試軟體控制'

手動登入 eagate 帳號

回到 PowerShell 視窗隨便輸入東西按 ENTER

放置 PowerShell 視窗跟那個 Chrome 視窗


### Prerequisites

1. Python

	Go to python https://www.python.org/ and install python if you don't have python.
	
	Make sure choose *ADD PYTHON TO ENVIRONMENT PATH* 安裝記得選加到環境變數 PATH, 才能在 PowerShell 內簡單打 python.exe
	
	安裝需要用到的額外 module
	
	在任何資料夾 Shift+右鍵開啟 PowerShell
	
	輸入 python.exe -m pip install schedule
	
	輸入 python.exe -m pip install selenium

2. Chrome driver

	Go to chrome driver https://chromedriver.chromium.org/ download 
	
	放到某個位置
	
	修改 jankenbot.py 內的
	
	chrome_driver_path = R'D:\install\chromedriver_win32\chromedriver.exe' 到你放的位置 例： R'E:\my_folder\chromedriver_win32\chromedriver.exe'
	
	路徑可以點資料夾上方的位置 會變成 D:\install\chromedriver_win32 格式可以複製, 自己補上 chromedriver.exe

3. Config JankenBot

	可以透過 jankenbot.py 的 23 行修改要每天固定出同樣的或者隨機
	
	22 `# you can change strategy to Strategy.Fixed or Strategy.Random`
	
	23 `strategy = Strategy.Fixed`
	
	可以透過 jankenbot.py 的 25 行修改要每天固定出的要是哪一種
	
	24 `# you can change fixed move, only used when strategy is Strategy.Fixed`
	
	25 `fixed_move = Move.Scissors`