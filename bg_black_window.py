import win32gui
import win32con
import win32api
from ctypes import byref
import sys

def create_child_window(main_window_handle):
    child_window_class = win32gui.WNDCLASS()
    child_window_class.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    child_window_class.lpfnWndProc = win32gui.DefWindowProc
    child_window_class.hInstance = win32api.GetModuleHandle(None)
    child_window_class.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    child_window_class.hbrBackground = win32gui.GetStockObject(win32con.BLACK_BRUSH)
    child_window_class.lpszClassName = "Child Window"
    win32gui.RegisterClass(child_window_class)

    child_window = win32gui.CreateWindow(
        child_window_class.lpszClassName,
        "Child Window",
        win32con.WS_CHILD | win32con.WS_VISIBLE,
        0,
        0,
        2048,
        2048,
        main_window_handle,
        0,
        win32api.GetModuleHandle(None),
        None,
    )

    win32gui.PumpMessages()

def main(main_window_handle):
    # Your main logic goes here
    create_child_window(main_window_handle)
    # Additional code...

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the main window handle as a command-line argument.")
    else:
        try:
            main_window = int(sys.argv[1])  # Parse the main window handle as an integer in hexadecimal format
            main(main_window)
        except ValueError:
            print("Invalid main window handle. Please provide a valid hexadecimal value.")
