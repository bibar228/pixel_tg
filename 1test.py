import time


import pyautogui
import telebot

slots = {1: [1047, 626], 2: [1046, 676], 3: [1046, 742], 4: [1104, 767], 5: [1161, 792], 6: [1222, 771], 7: [1279, 740], 8: [1274, 680], 9: [1275, 618],
         10: [1223, 598], 11: [1165, 573], 12: [1104, 590], 13: [1105, 654], 14: [1106, 708], 15: [1167, 737], 16: [1222, 713], 17: [1219, 649],
         18: [1164, 622], 19: [1161, 684]}

color_slots = {1: [1073, 578], 2: [1075, 624], 3: [1073, 683], 4: [1131, 715], 5: [1188, 744], 6: [1247, 701], 7: [1304, 683]}

main_slots = {1: [1074, 954], 2: [1174, 964], 3: [1270, 962]}

import webcolors
def get_colour_name(rgb_triplet):
    # full list: https://www.w3schools.com/tags/ref_colornames.asp
    myColors = {
        "red": "#ff0000",  # R
        "orange": "#ffa500",  # O
        "yellow": "#ffff00",  # Y
        "green": "#008000",  # G
        "blue": "#0000ff",  # B
        "magenta": "#ff00ff",  # I
        "purple": "#800080",  # V

        "coral": "#ff7f50",  # light red
        "maroon": "#800000",  # dark red
        "navy": "#000080",  # dark blue
        "cyan": "#00ffff",  # light blue
        "gold": "#ffd700",  # dark yellow
        "lime": "#00ff00",  # bright green
        "jade": "#00a36c",  # light green
        "olive": "#808000",  # dark green
        "grey": "#808080"}

    min_colours = {}
    for name, hex_val in myColors.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(hex_val)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name

    return min_colours[min(min_colours.keys())]


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

    #if currentWindow == "TelegramDesktop":
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
            # time.sleep(random.random())
            # pyautogui.moveTo(953, 852, 1)
            # time.sleep(random.random())
            # pyautogui.click()
            # count += 1

            if pyautogui.pixel(977, 552) != (255, 255, 255):
                pyautogui.click()
                count += 1


            # finish = time.time()
            # time.sleep(random.random())
            # pix_x = random.randint(x[0], x[1])
            # pix_y = random.randint(y[0], y[1])
            # pyautogui.moveTo(pix_x, pix_y)
            # # pyautogui.click()
            # # time.sleep(random.random())
            # # pyautogui.moveTo(953, 852, 1)
            # # time.sleep(random.random())
            # # pyautogui.click()
            # # count += 1
            #
            # if pyautogui.pixel(pix_x, pix_y) != (0, 0, 0):
            #     pyautogui.click()
            #     time.sleep(0.1)
            #     pyautogui.moveTo(953, 852)
            #     time.sleep(0.1)
            #     pyautogui.click()
            #     count += 1

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