import os
import requests 
import ctypes


def set_wallpaper(path):
    # Set the image as desktop and lockscreen wallpaper.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    os.system(f'igcmdWin10.exe setlockimage {path}')


def get_screen_resolution():
    # Call Windows OS functions, to get screen resolution.
    return ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)


def unsplash_wallpaper():
    width, height = get_screen_resolution()

    # Send GET request to Unsplash backend, to get the wallpaper. 
    request_image = requests.get(f"https://source.unsplash.com/random/{width}x{height}/?wallpaper")

    if request_image.ok:
        # If response is ok, get path to Pictures directory of the current user, and add temp.jpg to it.
        image_path = os.path.join(os.environ["USERPROFILE"], "Pictures", "temp.jpg")
        with open(image_path, "wb") as image_file:
            # Write the received file to the path, then set the wallpaper.
            image_file.write(request_image.content)
        set_wallpaper(image_path)


if __name__ == "__main__":
    unsplash_wallpaper()
