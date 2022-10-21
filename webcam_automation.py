import os, pyautogui,time, schedule, webbrowser, random, keyboard, winsound
from tkinter import messagebox as msgbox
zoomPath = "C:/Users/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom"
zoomURL = "https://us02web.zoom.us/j/7172236543?pwd=R3gxSnpCY2lIUWdmSkNvK2kzQmROZz09"
newMeetingCoor = [593,432] #새 회의로 돌아가기 버튼의 좌표

#좌표확인
def coordinate():
    import pyautogui
    while True:
        print(pyautogui.position())

#출결체크
def checkIn():
    msgbox.showwarning("ATTENDANCE", "입실 체크하세요.")
def checkOut():
    msgbox.showwarning("ATTENDANCE", "퇴실 체크하세요.")

#알림음
def beep(): # 알림음 재생
    winsound.Beep(
        frequency=440,  # Hz
        duration=1000  # milliseconds
    )
    winsound.PlaySound("example.wav", winsound.SND_FILENAME)

#줌시작
def startZoom():
    beep()
    os.startfile(zoomPath)
    time.sleep(5)
    webbrowser.open(zoomURL)
    time.sleep(10)
    checkIn()

#카메라 on/pff
def turnOnOff():
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    beep()
    time.sleep(5)
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('v')  # v key를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(240)
    #쉬는시간 끝나고 시작캡쳐 실행
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    beep()
    time.sleep(5)
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('v')  # v 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(3)

#줌중료
def systemOff():
    beep()
    time.sleep(5)
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('q')  # q 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(1)
    pyautogui.press('enter')  # enter 키를 누릅니다.
    time.sleep(2)
    checkOut()

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
    beep()
    time.sleep(5)
    pyautogui.keyDown('alt')  # alt 키를 누른 상태를 유지합니다.
    pyautogui.press('h')  # v 를 입력합니다.
    pyautogui.keyUp('alt')  # alt 키를 뗍니다.
    time.sleep(3)
    keyboard.write(todaysLine) #키보드로 '안녕하세요'작성
    keyboard.press_and_release('enter') #전송
    time.sleep(3)

#수고하셨습니다
def bye():
    todaysLine = "수고하셨습니다!"
    os.startfile(zoomPath)
    time.sleep(3)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    time.sleep(4)
    pyautogui.click(newMeetingCoor[0], newMeetingCoor[1], button='left', clicks=1,interval=1)  # 카메라 마우스 좌표 필요, 해당 좌표(x,y)로 마우스 커서 이동 후 클릭
    beep()
    time.sleep(5)
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
schedule.every().day.at("09:48").do(turnOnOff)
#2교시
schedule.every().day.at("10:03").do(turnOnOff)
schedule.every().day.at("10:48").do(turnOnOff)
#3교시
schedule.every().day.at("11:03").do(turnOnOff)
schedule.every().day.at("11:48").do(turnOnOff)
#4교시
schedule.every().day.at("12:03").do(turnOnOff)
schedule.every().day.at("12:48").do(turnOnOff)

#점심시간 13:00~14:00
schedule.every().day.at("12:57").do(lunch)
schedule.every().day.at("12:58").do(systemOff)
schedule.every().day.at("13:58").do(startZoom)

#5교시
schedule.every().day.at("14:03").do(turnOnOff)
schedule.every().day.at("14:48").do(turnOnOff)
#6교시
schedule.every().day.at("15:03").do(turnOnOff)
schedule.every().day.at("15:48").do(turnOnOff)
#7교시
schedule.every().day.at("16:03").do(turnOnOff)
schedule.every().day.at("16:48").do(turnOnOff)
#8교시
schedule.every().day.at("17:03").do(turnOnOff)
schedule.every().day.at("17:48").do(turnOnOff)
#시스템 종료
schedule.every().day.at("17:53").do(bye)
schedule.every().day.at("17:54").do(systemOff)

while True:
    schedule.run_pending()
    time.sleep(1)

