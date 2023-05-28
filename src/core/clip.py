# -*- coding: utf-8 -*-
# @Time    : 2023/5/27
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : clip.py
# @Software: PyCharm
import subprocess
import time

from src.config.setupsetting import sysname, Platform, ROOT_DIR


class ClipboardError(Exception):
    pass


class Clipboard:
    def __init__(self):
        self.change = self.get_change()
        self.setup()

    def setup(self):
        self.get_change()

    def change_state(self):
        status = self.change != self.get_change()
        self.change = self.get_change()
        return status

    def get_change(self):
        return Clipboard.status()

    @staticmethod
    def status():
        if sysname == Platform.MACOS:
            try:
                return Clipboard.paste()
            except subprocess.CalledProcessError as error:
                raise ClipboardError(f"Error occurred while counting from Clipboard: {error}")
        elif sysname == Platform.LINUX:
            return Clipboard.paste()
        elif sysname == Platform.WINDOWS:
            import pywintypes
            try:
                import win32clipboard
                win32clipboard.OpenClipboard()
                change_count = win32clipboard.GetClipboardSequenceNumber()
                win32clipboard.CloseClipboard()
                return change_count
            except pywintypes.error as e:
                if e.winerror == 5:  # Access denied
                    time.sleep(0.1)  # Wait for a short time and try again
                else:
                    raise e
        elif sysname == Platform.IOS:
            try:
                process = subprocess.run(["pbcount"], capture_output=True, text=True, check=True)
                return int(process.stdout)
            except subprocess.CalledProcessError as error:
                print(f"Error occurred while counting from Clipboard: {error}")
                raise ClipboardError(f"Error occurred while counting from Clipboard: {error}")
        elif sysname == Platform.ANDROID:
            return Clipboard.paste()
        else:
            raise ClipboardError(f"无法识别的系统类型: {sysname}")

    @staticmethod
    def copy(data: str):
        if sysname == Platform.MACOS:
            import pyperclip
            pyperclip.copy(data)
        elif sysname == Platform.LINUX:
            import pyperclip
            pyperclip.copy(data)
        elif sysname == Platform.WINDOWS:
            import pyperclip
            pyperclip.copy(data)
        elif sysname == Platform.IOS:
            Clipboard._ios_set_clipboard(data)
        elif sysname == Platform.ANDROID:
            Clipboard._android_set_clipboard(data)
        else:
            raise ClipboardError(f"无法识别的系统类型: {sysname}")

    @staticmethod
    def paste():
        if sysname == Platform.MACOS:
            import pyperclip
            return pyperclip.paste()
        elif sysname == Platform.LINUX:
            import pyperclip
            return pyperclip.paste()
        elif sysname == Platform.WINDOWS:
            import pyperclip
            return pyperclip.paste()
        elif sysname == Platform.IOS:
            return Clipboard._ios_get_clipboard()
        elif sysname == Platform.ANDROID:
            return Clipboard._android_get_clipboard()
        else:
            raise ClipboardError(f"无法识别的系统类型: {sysname}")

    @staticmethod
    def _ios_set_clipboard(data: str):  # 复制到剪切板
        process = subprocess.run([ROOT_DIR / "IOS/pbcopy/pbcopy"], input=data, text=True, check=True)
        return process.returncode

    @staticmethod
    def _ios_get_clipboard():  # 从剪切板粘贴(获取内容)
        process = subprocess.run([ROOT_DIR / "IOS/pbpaste/pbpaste"], capture_output=True, text=True, check=True)
        return process.stdout

    @staticmethod
    def _android_set_clipboard(data: str):
        from jnius import autoclass

        Context = autoclass('android.content.Context')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        clipboard = activity.getSystemService(Context.CLIPBOARD_SERVICE)
        ClipData = autoclass('android.content.ClipData')
        clip = ClipData.newPlainText("label", data)
        clipboard.setPrimaryClip(clip)

    @staticmethod
    def _android_get_clipboard():
        from jnius import autoclass

        Context = autoclass('android.content.Context')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        clipboard = activity.getSystemService(Context.CLIPBOARD_SERVICE)
        if clipboard.hasPrimaryClip():
            item = clipboard.getPrimaryClip().getItemAt(0)
            text = item.getText()
            return str(text)
        return None