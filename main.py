import ctypes
import multiprocessing
from ctypes import wintypes
import win32gui
import win32con
import win32api
from ctypes import byref
import win32process
import operator

from find_window import find_windows_by_title
from enum_windows import enum_windows
from enum_child import enum_child_windows,get_current_child_windows
import  bg_black_window


def _dwmwa_dark_mode(hwnd):
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    value = wintypes.BOOL(True)
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd,
                                               DWMWA_USE_IMMERSIVE_DARK_MODE,
                                               ctypes.byref(value),
                                               ctypes.sizeof(value))

def _minimise(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def _hide(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

def hyper_dark_mode():
    all_windows = enum_windows()
    windows_handles = find_windows_by_title(all_windows, ".*Virtual Machine.*")
    print(windows_handles)

    for window_handle in windows_handles:
        child_wins = get_current_child_windows(window_handle["id"])
        child_wins = [win for win in child_wins if
                      win['rectangle'][2] - win['rectangle'][0] != 0 and win['rectangle'][3] - win['rectangle'][1] != 0]

        child_wins.sort(key=lambda win: win['rectangle'][1],reverse=True)
        print(child_wins)

        hyper_v_child_windows_count = sum(
            1 for child_win in child_wins if child_win["class_name"] == "WindowsForms10.Window.8.app.0.aa0c13_r6_ad1"
        )

        if hyper_v_child_windows_count == 4:
            _hide(child_wins[0]["id"])
            _hide(child_wins[1]["id"])
            _hide(child_wins[3]["id"])
        elif hyper_v_child_windows_count == 3:
            _hide(child_wins[0]["id"])
            _hide(child_wins[2]["id"])

        _dwmwa_dark_mode(window_handle["id"])
        bg_process = multiprocessing.Process(target=bg_black_window.main, args=(window_handle["id"],))
        bg_process.start()
        bg_process.join()



if __name__ == '__main__':
    hyper_dark_mode()





