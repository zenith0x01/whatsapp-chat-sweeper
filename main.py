import pyautogui
import time
import sys

user_name = sys.argv[1]
user_count = int(sys.argv[2])

pyautogui.FAILSAFE = True


#open search tab
pyautogui.press("win")
time.sleep(.2)

#open whatsapp
pyautogui.typewrite("Whatsapp")
time.sleep(.2)
pyautogui.press("enter")
time.sleep(7)

pyautogui.click(258, 97)
time.sleep(0.3)



#go to search and search for the use
pyautogui.hotkey("ctrl","f")
time.sleep(.2)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.1)
pyautogui.press("backspace")
time.sleep(0.2)


pyautogui.typewrite(user_name, interval=0.05)
time.sleep(.5)
pyautogui.press("enter")
time.sleep(.5)
pyautogui.press("enter")

time.sleep(1)

region_for_3dots = (1846, 52, 1894 , 106 )
region_for_selected = (164, 153, 1853, 191 )
region_to_search = (523, 117, 673, 1060)


pyautogui.screenshot("debug_view.png", region=region_to_search)
print("Saved 'debug_view.png'.")


remaining = user_count

try:
    while remaining > 0:

        # ---- ENTER SELECT MODE (EVERY TIME) ----
        a = pyautogui.locateOnScreen('3dots.png', region=region_for_3dots, confidence=0.8)
        if not a:
            break
        pyautogui.click(pyautogui.center(a))
        time.sleep(0.3)

        b = pyautogui.locateOnScreen('select.png', region=region_for_selected, confidence=0.8)
        if not b:
            break
        pyautogui.click(pyautogui.center(b))
        time.sleep(0.5)

        # ---- DETECT SELECTION BOXES ----
        all_locations = list(pyautogui.locateAllOnScreen('symbol.png',region=region_to_search,confidence=0.6))

        if not all_locations:
            break

        all_locations.sort(key=lambda loc: loc.top)

        unique_locations = [all_locations[0]]
        for box in all_locations[1:]:
            if box.top > unique_locations[-1].top + 20:
                unique_locations.append(box)

        unique_locations.sort(key=lambda loc: loc.top, reverse=True)

        to_delete_now = min(remaining, len(unique_locations))
        if to_delete_now == 0:
            break

        # ---- SELECT MESSAGES ----
        for i in range(to_delete_now):
            pyautogui.click(pyautogui.center(unique_locations[i]))
            time.sleep(0.1)

        # ---- DELETE ----
        time.sleep(0.5)
        pyautogui.moveTo(1736, 1111)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(1152, 629)
        pyautogui.click()

        remaining -= to_delete_now
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

