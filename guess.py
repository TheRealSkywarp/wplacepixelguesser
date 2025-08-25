import warnings
warnings.filterwarnings("ignore")

import os
import sys
import subprocess
from datetime import datetime, timedelta

pixelreloadtime = 30

def requirements():
    try:
        import win10toast
    except ImportError:
        print("⬇️ win10toast not found, installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "win10toast"])
        print("✅ win10toast installed!")
    global ToastNotifier
    from win10toast import ToastNotifier

def math(pixelreloadtime):
    total_seconds = pixelreloadtime * 30
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return total_seconds, hours, minutes, seconds

def main():
    requirements()
    currentpixels = int(input("🎯 How many pixels do you currently have? "))
    maxpixels = int(input("📦 What is your maximum pixel stock? "))
    pixelreloadtime = max(0, maxpixels - currentpixels)
    if pixelreloadtime == 0:
        print("🎉 Your stock is already full!")
        return
    total_seconds, hours, minutes, seconds = math(pixelreloadtime)
    end = datetime.now() + timedelta(seconds=total_seconds)
    print(f"📉 Pixels to reload: {pixelreloadtime}")
    print(f"⏳ Total time: {hours}h {minutes}m {seconds}s")
    print(f"🕒 Stock full at: {end.strftime('%H:%M:%S')}")
    consent = input("📢 Do you want me to schedule a Windows notification in the background? (y/n): ").strip().lower()
    if consent != "o":
        print("❌ No reminder created.")
        return
    script_path = os.path.join(os.environ['TEMP'], 'wplacereminder.py')
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(
            "import time\n"
            "from win10toast import ToastNotifier\n"
            f"time.sleep({total_seconds})\n"
            "toaster = ToastNotifier()\n"
            "toaster.show_toast(\"🎉 Stock full\", \"Your pixel stock has now fully refilled!\", duration=10)\n"
        )
    subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NO_WINDOW)
    print(f"✅ Notification scheduled in the background for {end.strftime('%H:%M:%S')}.")

if __name__ == "__main__":
    main()