# Pi_Pico_Macro_Keyboard
## 我是參考以下這篇文章做的  
http://blog.4dcu.be/diy/2021/04/05/Macropad.html

## 成品如下  
![image](https://github.com/Chihhao/Pi_Pico_Macro_Keyboard/blob/master/IMG_2939.jpg)  

## 九個按鍵的功能如下：  
| 左螢幕開關 | 未定義   | 兩個螢幕同時關閉 | 
|   :---:   |  :---:   |  :---:   |
| 左螢幕增亮 | 音量增加 | 右螢幕增亮 |  
| 左螢幕減亮 | 音量減少 | 右螢幕增亮 |  

## 這個專案有一點複雜，用了好幾個小軟體  
### (1) AutoHotKey: (請到官網下載)  
定義快捷鍵，其功能強大不必多說  
https://www.autohotkey.com/  
### (2) ControlMyMonitor.exe:  (內含，不必下載)  
能夠調整螢幕亮度  
https://www.nirsoft.net/utils/control_my_monitor.html  
### (3) MultiMonitorTool.exe: (內含，不必下載)  
能夠開關第二個螢幕  
https://www.nirsoft.net/utils/multi_monitor_tool.html  
### (4) Disable_Monitor.exe: (內含，不必下載)  
能夠同時關閉兩個螢幕 

## 準備 Rpi-Pico
### 安裝 CircuitPython
(1) 下載 UF2 檔案: https://circuitpython.org/board/raspberry_pi_pico/  
(2) 按住開發板 BOOTSEL 按鈕不要放開，將 Pico 接上 USB ，然後鬆開 BOOTSEL 按鈕，此時「我的電腦」裡會顯示一個磁碟機，就像隨身碟一樣  
(3) 將 UF2 檔案放進根目錄，此時 Pico 會自動重啟  
(4) 將 adafruit_hid 整個資料夾放在 lib 底下，此時 Pico 會自動重啟 (Library 來自 https://github.com/adafruit/Adafruit_CircuitPython_HID)  
(5) 將 code.py 放進根目錄（覆蓋原有的檔案），此時 Pico 會自動重啟  

### Rpi-Pico 線路圖









