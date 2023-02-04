import os
import requests 
import ctypes


def set_wallpaper(path):
    # Set the image as desktop and lockscreen wallpaper.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    os.system(f'igcmdWin10.exe setlockimage {path}')


def bing_wallpaper():
    # Send GET request to URL that responds with JSON that contains URL to daily wallpaper.
    request_for_url = requests.get("https://bing.biturl.top/")

    if request_for_url.ok:
        # If response is ok, get the URL from JSON, send GET request to it.
        daily_wallpaper_url = request_for_url.json()["url"]
        request_daily_wallpaper = requests.get(daily_wallpaper_url)

        if request_daily_wallpaper.ok:
            # Get path to Pictures directory of the current user, and add temp.jpg to it.
            image_path = os.path.join(os.environ["USERPROFILE"], "Pictures", "temp.jpg")
            with open(image_path, "wb") as image_file:
                # Write the received file to the path, then set the wallpaper.
                image_file.write(request_daily_wallpaper.content)
            set_wallpaper(image_path)


if __name__ == "__main__":
    bing_wallpaper()
