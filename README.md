# 🎯 WPlace Pixel Guesser

A lightweight Python tool to estimate how long it will take for your WPlace pixel stock to fully recharge — with an optional Windows notification to remind you when it's ready.

## 📦 Features

- Calculates remaining pixel recharge time  
- Displays the exact time your stock will be full  
- Offers to schedule a Windows notification in the background  
- Automatically installs `win10toast` if missing  

## 🚀 Installation

Make sure you have Python installed on your Windows machine.

Clone the repository:

```git clone https://github.com/TheRealSkywarp/wplacepixelguesser.git```

Navigate to the project folder:

```cd wplacepixelguesser```

Run the script:

```py guess.py```

💡 The script will auto-install win10toast if it's not already installed.

## 🛠️ Usage

Enter your current pixel count

Enter your maximum pixel stock on WPlace

The script will display:

Pixels left to recharge

Total estimated time

Exact time your stock will be full

You can choose to receive a Windows notification at that time

## 🔔 Example Notification

```🎉 Stock full```
```Your pixel stock has now fully refilled!```

## 🧪 Dependencies
win10toast

## 🖥️ Compatibility

✅ Windows only (uses win10toast for notifications)
❌ Not compatible with macOS or Linux

## 📄 Main File
guess.py — the main script

## 📬 Contributing
Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

# Made with ❤️ for WPlace
