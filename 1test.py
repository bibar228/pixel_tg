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

    if currentWindow == "Not Pixel — Яндекс Браузер":
        # print(pyautogui.position())
        # #print(pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1]))
        # time.sleep(1)

        """Открываем игру"""
        pyautogui.moveTo(905, 1026, 1)
        pyautogui.click()
        time.sleep(random.randint(25, 30))

        pyautogui.moveTo(1123, 424, 1)
        pyautogui.click()

        """Проверка на темный экран"""
        check = [755, 328]
        if pyautogui.pixel(check[0], check[0]) == (23, 31, 42):
            pyautogui.moveTo(747, 242, 1)
            pyautogui.click()
            time.sleep(random.random())
            pyautogui.click()
            continue

        x = [835, 1007]

        y = [388, 643]
        """Приближаем поле"""

        pyautogui.moveTo(767, 446, 1)
        pyautogui.scroll(2400)


        time.sleep(2)



        """Проверяем на цвет и красим"""
        count = 0
        start = time.time()
        pyautogui.moveTo(random.randint(x[0], x[1]), random.randint(y[0], y[1]))
        pyautogui.click()

        while count < 16:
            finish = time.time()
            time.sleep(random.random())
            x_pix = random.randint(x[0], x[1])
            y_pix = random.randint(y[0], y[1])
            pyautogui.moveTo(x_pix, y_pix)
            pyautogui.click()

            if pyautogui.pixel(x_pix, y_pix) == (23, 31, 42):
                break

            if pyautogui.pixel(x_pix, y_pix) != (0, 0, 0) and pyautogui.pixel(x_pix, y_pix) != (54, 144, 234) and pyautogui.pixel(x_pix, y_pix) != (66, 166, 255):
                pyautogui.moveTo(954, 890)
                pyautogui.click()
                count += 1
                time.sleep(random.random())

            if finish - start > 180:
                break

        """Закрываем игру"""
        time.sleep(random.randint(5, 10))
        pyautogui.moveTo(769, 232, 1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(random.randint(2000, 2500))