import re

from enum_windows import enum_windows


def find_windows_by_title(window_dict, regex_pattern):
    matching_windows = []
    pattern = re.compile(regex_pattern, re.IGNORECASE)

    for window in window_dict:
        title = window['title']
        if re.search(pattern, title):
            matching_windows.append(window)

    return matching_windows

