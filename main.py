import ctypes
import time

# define file paths for the wallpapers
morning_wallpaper = ''
day_wallpaper = ''
evening_wallpaper = ''
night_wallpaper = ''

# define the times of day in 24-hour format
morning_hour = 6
day_hour = 11
evening_hour = 17
night_hour = 21

while True:
    # get the current hour in 24-hour format
    current_hour = time.localtime().tm_hour

    # set the wallpaper based on the time of day
    if current_hour >= morning_hour and current_hour < day_hour:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, morning_wallpaper, 0)
    elif current_hour >= day_hour and current_hour < evening_hour:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, day_wallpaper, 0)
    elif current_hour >= evening_hour and current_hour < night_hour:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, evening_wallpaper, 0)
    else:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, night_wallpaper, 0)

    # wait for 10 seconds before checking the time again
    time.sleep(10)
