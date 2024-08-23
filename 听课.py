import pyautogui
import time
import threading

a = 0

def ds():
    pyautogui.scroll(-1000)
    try:
        if pyautogui.locateOnScreen(r'D:\Pictures\加载.PNG'):
            left6, top6, width6, height6 = pyautogui.locateOnScreen(r'D:\Pictures\加载.PNG')
            pyautogui.click(left6 + 10, top6 + 10)
            pyautogui.moveTo(90, 709)
    except:
        pass
    time.sleep(1)
    pyautogui.scroll(1000)
def dianji():

    try:
        if pyautogui.locateOnScreen(r'D:\Pictures\未开始1.PNG'):
            print("去听课已识别")
            time.sleep(0.5)  # 等待 0.5 秒
            left, top, width, height = pyautogui.locateOnScreen(r'D:\Pictures\未开始1.PNG')
            left1, top1, width1, height1 = pyautogui.locateOnScreen(r'D:\Pictures\未开始1.PNG')
            left2, top2, width2, height2 = pyautogui.locateOnScreen(r'D:\Pictures\未开始1.PNG')
            if top > 211 and top < 341:
                center = pyautogui.center((left, top, width, height))
                pyautogui.click(center)
                print("已点击坐标", left, top)
                time.sleep(3)
            else:
                print("未找到目标1")
                pyautogui.scroll(-141)
                xunzhao()
        else:
            print("未找到目标")
            pyautogui.scroll(-141)
            xunzhao()
    except:
        print("未找到，已下划")
        pyautogui.scroll(-141)
        global a
        a += 1
        if a >= 8:
            a = 0
            print("检测到本天任务已完成，已帮您自动切换至下一天")
            pyautogui.scroll(3500)
            pyautogui.scroll(-785)
            time.sleep(3)
            pyautogui.click(1136, 279)
            time.sleep(3)
            pyautogui.scroll(-240)
            ds()
            xunzhao()
        else:
            xunzhao()

def xunzhao():
    try:
        if pyautogui.locateOnScreen(r'D:\Pictures\shijuan.PNG'):
            print('ok')
            # pyautogui.moveTo(585, 709)
            left, top, width, height = pyautogui.locateOnScreen(r'D:\Pictures\shijuan.PNG')
            left1, top1, width1, height1 = pyautogui.locateOnScreen(r'D:\Pictures\shijuan.PNG')
            left2, top2, width2, height2 = pyautogui.locateOnScreen(r'D:\Pictures\shijuan.PNG')
            if top > 230 and top < 353:
                print("试卷不符合要求, top坐标为", left, top)
                pyautogui.scroll(-141)
                xunzhao()
            else:
                print("执行点击程序top", left, top)
                dianji()
        else:
            print("未识别试卷，执行点击程序")
            dianji()

    except:
        print("未识别试卷，执行点击程序")
        dianji()
def main():
    time.sleep(5)
    ds()
    time.sleep(5)
    xunzhao()
    fun2.start()
    while True:
        time.sleep(10)
        pyautogui.click(585, 709)
        time.sleep(1)
        """pyautogui.moveTo(936, 992)
        time.sleep(1)
        pyautogui.click(935, 828)
        time.sleep(1)
        pyautogui.moveTo(163, 704)"""
        time.sleep(400)
        pyautogui.click(747, 17)
        time.sleep(3)
        pyautogui.click(289, 10)
        time.sleep(3)
        pyautogui.moveTo(163, 704)
        time.sleep(3)
        pyautogui.scroll(-141)
        xunzhao()
def main2():
    while True:
        time.sleep(30)
        pyautogui.click(90, 709)
        time.sleep(0.5)
        pyautogui.click(90,709)

if __name__ == '__main__':
    fun1 = threading.Thread(target=main)
    fun1.start()
    fun2 = threading.Thread(target=main2)