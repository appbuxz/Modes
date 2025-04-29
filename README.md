# 🖥️ Modes Launcher(Windows!)

Простое и удобное Python-приложение с графическим интерфейсом для переключения между режимами: "Gaming", "Study" и "Stay". Скрипт управляет яркостью, уведомлениями, фоновыми приложениями и автоматически добавляется в автозагрузку.

---

### 🚀 Функции:
- 🎮 **Gaming Mode** — запускает YouTube-плейлист и отключает уведомления.
- 📚 **Study Mode** — включает уведомления и запускает Visual Studio Code.
- 🌙 **Stay Mode** — снижает яркость, закрывает мессенджеры и активирует режим экономии энергии.
- 🧠 Работает через графику `DearPyGUI`
- 🔄 Автоматически добавляется в автозагрузку с помощью скрытого `.vbs`-файла.

---

### 🛠 Установка:
1. Установи зависимости:
   ```bash
   pip install dearpygui screen_brightness_control winshell

    Запусти modes.py

    При первом запуске приложение автоматически добавит себя в автозагрузку (скрыто).

🖥️ Modes Launcher (Windows)

A simple and lightweight Python GUI app to switch between modes: Gaming, Study, and Stay. Controls brightness, notifications, background apps, and adds itself to startup silently.
🚀 Features:

    🎮 Gaming Mode — opens a YouTube playlist and disables notifications.

    📚 Study Mode — enables notifications and launches Visual Studio Code.

    🌙 Stay Mode — reduces brightness, kills messengers, and activates power saving.

    🧠 Built with DearPyGUI

    🔄 Automatically adds itself to Windows startup using a hidden .vbs launcher.

🛠 Installation:

    Install dependencies:

    pip install dearpygui screen_brightness_control winshell

    Run modes.py

    On first launch, it adds itself to Windows startup automatically (hidden).

📁 Автозагрузка:
.bat запускается через .vbs без отображения окна.

📃 Автор: [appbuxz]
