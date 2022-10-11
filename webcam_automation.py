import os, pyautogui,time, schedule, webbrowser, random, keyboard
zoomPath = "Microsoft/Windows/Start Menu/Programs/Zoom/Zoom"
zoomURL = "zoom URL"
newMeetingCoor = [593,432] #새 회의로 돌아가기 버튼의 좌표
# cameraCoor = [459,900]
# zoomshutdownCoor = [780,900]
# reallyshutdownCoor = [670,781]

#좌표확인
# import pyautogui
# while True:
#     print(pyautogui.position())

def startZoom():
    os.startfile(zoomPath)
    time.sleep(5)
    webbrowser.open(zoomURL)
    time.sleep(10)

def turnOnOff():
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    # pyautogui.click(cameraCoor[0], cameraCoor[1], button='left', clicks=1, interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('v')  # v key를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(540)
    # pyautogui.click(cameraCoor[0], cameraCoor[1], button='left', clicks=1, interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('v')  # v 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(3)

def systemOff():
    # pyautogui.click(zoomshutdownCoor[0], zoomshutdownCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    # time.sleep(3)
    # pyautogui.click(reallyshutdownCoor[0], reallyshutdownCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    # time.sleep(3)
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('q')  # v 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(2)
    pyautogui.press('enter')  # enter 키를 누릅니다.
    time.sleep(2)

#점심인사
def lunch():
    lines = ['식사 맛있게 하세요^^', '맛점하세요!','점심 맛있게 드세요~']
    randN = random.randrange(0,3)
    todaysLine = str(lines[randN])
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(4)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('h')  # v 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(3)
    keyboard.write(todaysLine) #키보드로 '안녕하세요'작성
    keyboard.press_and_release('enter') #전송
    time.sleep(3)

#program start
schedule.every().day.at("08:57").do(startZoom)

#1교시
schedule.every().day.at("09:03").do(turnOnOff)
schedule.every().day.at("09:49").do(turnOnOff)
#2교시
schedule.every().day.at("10:03").do(turnOnOff)
schedule.every().day.at("10:49").do(turnOnOff)
#3교시
schedule.every().day.at("11:03").do(turnOnOff)
schedule.every().day.at("11:49").do(turnOnOff)
#4교시
schedule.every().day.at("12:03").do(turnOnOff)
schedule.every().day.at("12:49").do(turnOnOff)
#점심시간 13:00~14:00
schedule.every().day.at("13:01").do(lunch)
#5교시
schedule.every().day.at("14:03").do(turnOnOff)
schedule.every().day.at("14:49").do(turnOnOff)
#6교시
schedule.every().day.at("15:03").do(turnOnOff)
schedule.every().day.at("15:49").do(turnOnOff)
#7교시
schedule.every().day.at("16:03").do(turnOnOff)
schedule.every().day.at("16:49").do(turnOnOff)
#8교시
schedule.every().day.at("17:03").do(turnOnOff)
schedule.every().day.at("16:49").do(turnOnOff)
#시스템 종료
schedule.every().day.at("17:55").do(systemOff)

while True:
    schedule.run_pending()
    time.sleep(1)
