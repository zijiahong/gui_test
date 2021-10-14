import win32gui
import win32api
import win32con
import time


def doClick(cx, cy, hwnd):
    # hwnd为需要点击的窗口控件句柄，cx、cy为点击位置在该窗口的相对坐标
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                         win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    time.sleep(0.1)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP,
                         win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


wegame = win32gui.FindWindow(None, "WeGame")
def open_dnf():
    win32gui.ShowWindow(wegame, win32con.SW_SHOWNOACTIVATE)
    # win32gui.SetForegroundWindow(wegame)
    time.sleep(1)
    doClick(400, 53, wegame)
    time.sleep(1)
    doClick(100, 200, wegame)
    time.sleep(1)
    doClick(1150, 790, wegame)
    time.sleep(1)
    win32gui.ShowWindow(wegame, win32con.SW_HIDE)
    time.sleep(1)




def dnf():
	dnf = win32gui.FindWindow(None, "地下城与勇士")
	open_dnf()

	while dnf == 0:
		time.sleep(3)
		open_dnf()
	win32gui.ShowWindow(dnf, win32con.SW_SHOWNOACTIVATE)
	win32gui.SetForegroundWindow(dnf)

# win32gui.ShowWindow(wegame, win32con.SW_HIDE)
# time.sleep(2)
# dnf()

