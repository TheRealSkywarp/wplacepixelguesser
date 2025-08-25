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
        print("⬇️ win10toast non trouvé, installation en cours...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "win10toast"])
        print("✅ win10toast installé !")
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
    currentpixels = int(input("🎯 Combien de pixels as-tu actuellement ? "))
    maxpixels = int(input("📦 Quel est ton stock maximum de pixels ? "))
    pixelreloadtime = max(0, maxpixels - currentpixels)
    if pixelreloadtime == 0:
        print("🎉 Ton stock est déjà plein !")
        return
    total_seconds, hours, minutes, seconds = math(pixelreloadtime)
    end = datetime.now() + timedelta(seconds=total_seconds)
    print(f"📉 Pixels à recharger : {pixelreloadtime}")
    print(f"⏳ Temps total : {hours}h {minutes}m {seconds}s")
    print(f"🕒 Stock plein à : {end.strftime('%H:%M:%S')}")
    consent = input("📢 Veux-tu que je programme une notification Windows en arrière-plan ? (o/n) : ").strip().lower()
    if consent != "o":
        print("❌ Aucun rappel créé.")
        return
    script_path = os.path.join(os.environ['TEMP'], 'rappelwplace.py')
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(
            "import time\n"
            "from win10toast import ToastNotifier\n"
            f"time.sleep({total_seconds})\n"
            "toaster = ToastNotifier()\n"
            "toaster.show_toast(\"Stock plein 🎉\", \"Ton stock de pixels est maintenant au maximum !\", duration=10)\n"
        )
    subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NO_WINDOW)
    print(f"✅ Notification programmée en arrière-plan pour {end.strftime('%H:%M:%S')}.")

if __name__ == "__main__":
    main()