import win32gui

handle = win32gui.FindWindow(None, "WeGame") 
# subHandle = win32gui.FindWindowEx(handle,0,"WeGame",None)
r = win32gui.GetMenu(handle)

print(r)

