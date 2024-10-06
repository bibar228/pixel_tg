import time
import pyautogui
import random

chat_id = -695765690

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

while True:
    time.sleep(random.random())
    try:
        currentWindow = pyautogui.getActiveWindow().title
        # print(currentWindow)
        # time.sleep(1)
    except:
        pass

    if currentWindow == "Telegram Web — Яндекс Браузер":
        # print(pyautogui.position())
        # time.sleep(1)

        """Открываем игру"""
        pyautogui.moveTo(880, 995, 1)
        pyautogui.click()
        time.sleep(random.randint(25, 30))

        """Проверка на темный экран"""
        check = [755, 328]
        if pyautogui.pixel(check[0], check[0]) == (23, 31, 42):
            pyautogui.moveTo(747, 242, 1)
            pyautogui.click()
            time.sleep(random.random())
            pyautogui.click()
            continue

        x = [808, 1111]

        y = [453, 758]
        """Приближаем поле"""
        #pyautogui.moveTo(961, 606, 1)
        pyautogui.moveTo(971, 595, 1)
        pyautogui.scroll(2300)

        time.sleep(2)
        """Проверяем на цвет и красим"""
        count = 0
        start = time.time()
        pyautogui.moveTo(977, 552, 1)
        pyautogui.click()
        pyautogui.moveTo(953, 852, 1)
        while count < 10:
            finish = time.time()
            time.sleep(random.random())

            if pyautogui.pixel(977, 552) != (255, 255, 255):
                pyautogui.click()
                count += 1

            if finish - start > 180:
                break

        """Закрываем игру"""
        time.sleep(random.randint(5, 10))
        pyautogui.moveTo(747, 242, 1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(random.randint(2000, 2500))