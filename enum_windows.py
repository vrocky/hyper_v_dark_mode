import win32gui
import win32process

def enum_windows_callback(hwnd, windows):
    window_info = {}
    window_info['id'] = hwnd
    window_info['title'] = win32gui.GetWindowText(hwnd)
    window_info['class_name'] = win32gui.GetClassName(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    window_info['process_id'] = pid
    windows.append(window_info)

def enum_windows():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows




