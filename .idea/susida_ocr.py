import os

import pyocr
import time
import pyautogui
from PIL import Image
from pynput.keyboard import Controller

# Tesseractのパスを指定
pyocr.tesseract.TESSERACT_CMD = r'E:/dev/Tesseract-OCR/tesseract.exe'

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("OCRツールを取得できませんでした。")
    exit(2)

tools = tools[0]
keyboard = Controller()

# スクリーンショット保存パス
screenshot_folader = r'E:\dev\OCR_test'

# 試行回数
attempts = 1000
# 撮影する範囲指定
region = (700, 430, 450, 35)
time.sleep(0.5)
print("処理開始")
try:
    for i in range(attempts):
        screenshot = os.path.join(screenshot_folader, f'screenshot_{i}.png')
        pyautogui.screenshot(screenshot, region=region)

        img = Image.open(screenshot)
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        text = tools.image_to_string(img, lang='jpn', builder=builder)

        for char in text:
            keyboard.type(char)

except KeyboardInterrupt:
    print("割り込みが発生しました。")


# 終了時スクリーンショットを削除する
def delete_png_files():
    for tidying in os.listdir(screenshot_folader):
        if tidying.endswith('.png'):
            file_path = os.path.join(screenshot_folader, tidying)
            os.remove(file_path)
    print("お片付け完了！")


delete_png_files()
