import win32gui
import win32process

def enum_windows_callback(hwnd, windows):
    window_info = {}
    window_info['id'] = hwnd
    window_info['title'] = win32gui.GetWindowText(hwnd)
    window_info['class_name'] = win32gui.GetClassName(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    window_info['process_id'] = pid
    window_info['rectangle'] = win32gui.GetWindowRect(hwnd)
    windows.append(window_info)

def enum_child_windows(parent_hwnd):
    windows = []
    win32gui.EnumChildWindows(parent_hwnd, enum_windows_callback, windows)
    return windows

def current_child(hwnd, lParam):
    parent_hwnd, child_windows = lParam
    if win32gui.GetParent(hwnd) == parent_hwnd:
        window_info = {}
        window_info['id'] = hwnd
        window_info['title'] = win32gui.GetWindowText(hwnd)
        window_info['class_name'] = win32gui.GetClassName(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        window_info['process_id'] = pid
        window_info['rectangle'] = win32gui.GetWindowRect(hwnd)
        child_windows.append(window_info)
    return True

def get_current_child_windows(parent_hwnd):
    child_windows = []
    win32gui.EnumChildWindows(parent_hwnd, current_child, (parent_hwnd, child_windows))
    return child_windows
