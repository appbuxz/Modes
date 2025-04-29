from dearpygui import dearpygui as dpg
import webbrowser
import os
import subprocess
import time
import screen_brightness_control as sbc
import threading
import shutil
import winshell
import sys

dpg.create_context()
app_name = "python"
def restart(sender, app_data):
    try:
        subprocess.run(["powershell", "-Command", f"Stop-Process -Name '{app_name}' -Force"], check=True)
        print(f"Приложение {app_name} закрыто.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при закрытии приложения {app_name}: {e}")
    #"Перезапуск программы."
    python = sys.executable 
    script = os.path.abspath(__file__) 
    subprocess.Popen([python, script] + sys.argv[1:])

def add_vbs_to_startup():
    vbs_src = r"C:\VS CODE\Projects\taskGUI\launch_task_mode.vbs"
    vbs_dst = os.path.join(winshell.startup(), "launch_task_mode.vbs")

    try:
        shutil.copyfile(vbs_src, vbs_dst)
        print(f"VBS-файл автозапуска успешно добавлен в: {vbs_dst}")
    except Exception as e:
        print(f"Ошибка при копировании VBS-файла: {e}")

def reduce_brightness():
    try:
        subprocess.run([
            'powershell',
            '-Command',
            '(Get-WmiObject -Namespace root\\wmi -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,30)'
        ], check=True)
        print("Яркость снижена.")
    except Exception as e:
        print("Ошибка при снижении яркости:", e)

def kill_apps():
    apps = ["Discord.exe", "Steam.exe", "Telegram.exe", "OneDrive.exe"]
    for app in apps:
        subprocess.run(["taskkill", "/f", "/im", app], shell=True)

def on_button_click(sender, app_data):
        if sender == button_gaming:
            print("User choosed Gaming")

            url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"  # Замени на свой плейлист
            webbrowser.open(url)

            try:
                subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser'], check=True)
                subprocess.run(['powershell', '-Command', 'New-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" -Name "ToastEnabled" -Value 0 -PropertyType DWord -Force'], check=True)
                print("Уведомления отключены.")
            except Exception as e:
                print(f"Ошибка при отключении уведомлений: {e}")
            dpg.destroy_context()

        elif sender == button_study:
            print("User choosed study")
            try:
                subprocess.run(['powershell', '-Command', 'New-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" -Name "ToastEnabled" -Value 1 -PropertyType DWord -Force'], check=True)
                print("Все уведомления включены.")
            except Exception as e:
                print(f"Ошибка при включении уведомлений: {e}")
            try:
                subprocess.run([r"C:\Users\pauls\AppData\Local\Programs\Microsoft VS Code\Code.exe"])# Запуск VS Code
                print("VS Code открыт.")
            except FileNotFoundError:
                print("VS Code не найден. Убедитесь, что он установлен и добавлен в PATH.")
            dpg.destroy_context()

        elif sender == button_staying:
            print("User choosed staying")

            # Запускаем фоново действия staying
            threading.Thread(target=reduce_brightness).start()
            threading.Thread(target=kill_apps).start()
            subprocess.run(['powercfg', '/setactive', 'a1841308-3541-4fab-bc81-f71556f20b4a'])
            dpg.set_viewport_pos([500, 50])
            with dpg.window(label="Stay Mode", width=300, height=100, no_resize=True, no_move=True, no_title_bar=True):
                dpg.add_text("Computer on Stay Mode")
                back_button = dpg.add_button(label="Back", width=100, height=30, callback=restart)


  
with dpg.window(label="app",  no_title_bar=True, no_move=True, no_resize=True,no_background=True, width=300, height=100):
    with dpg.group(horizontal=True):
        button_gaming = dpg.add_button(label="Gaming", width= 90,height=70 ,callback= on_button_click)
        button_study = dpg.add_button(label="Study", width=90,height=70 ,callback= on_button_click)
        button_staying = dpg.add_button(label="Stay", width=100,height=70 ,callback= on_button_click)


dpg.create_viewport(title=" ", width=307, height=100, decorated=False) # decorated = не отображать.
dpg.set_viewport_pos([500, 50])


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
add_vbs_to_startup()

dpg.destroy_context()