import sys
import platform
import re
import time
from enum import Enum
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from xtool import Ui_MainWindow
import pyautogui

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


# 号码状态
class PhoneState(Enum):
    Waiting = 1,  # 等待添加
    Succeed = 2,  # 添加成功
    Failed = 3,  # 添加失败

    def __str__(self):
        if self == PhoneState.Waiting:
            return "等待"
        if self == PhoneState.Succeed:
            return "成功"
        if self == PhoneState.Failed:
            return "失败"


# 组合ui和逻辑
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.phoneTable.setColumnWidth(0, 50)
        self.phoneTable.setColumnWidth(1, 150)
        self.phoneTable.setColumnWidth(2, 80)
        self.setWindowTitle("企业微信自动加人工具")
        # 绑定导入按钮
        self.importBtn.clicked.connect(self.import_phone)
        # 存储好友信息
        self.friend_infos = []
        # 绑定执行按钮
        self.playBtn.clicked.connect(self.start_invite)

    def import_phone(self):
        phone_file_name, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "Text files (*.txt)")
        phone_file = open(phone_file_name, 'r')
        self.friend_infos = []
        idx = 1
        for line in phone_file.readlines():
            phone = re.search("[0-9]+", line)
            if phone:
                friend_info = {
                    'idx': idx,
                    'phone': phone.group(),
                    'state': PhoneState.Waiting
                }
                self.friend_infos.append(friend_info)
                idx = idx + 1
        if len(self.friend_infos) != 0:
            self.phoneTable.verticalHeader().setHidden(True)
            self.phoneTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.phoneTable.setRowCount(len(self.friend_infos))
            for [row, friend_info] in enumerate(self.friend_infos):
                self.phoneTable.setItem(row, 0, QTableWidgetItem(str(friend_info["idx"])))
                self.phoneTable.setItem(row, 1, QTableWidgetItem(str(friend_info["phone"])))
                state_item = QTableWidgetItem(str(friend_info["state"]))
                if friend_info["state"] == PhoneState.Failed:
                    state_item.setBackground(QColor(255, 0, 0))
                elif friend_info["state"] == PhoneState.Succeed:
                    state_item.setBackground(QColor(0, 255, 0))

                self.phoneTable.setItem(row, 2, state_item)

    def start_invite(self):
        # 第一步切换到企业微信组织架构页面
        select_location = pyautogui.locateCenterOnScreen('./stepPic/select.png', confidence=0.9)
        if not select_location:
            un_select_location = pyautogui.locateCenterOnScreen('./stepPic/un_select.png', confidence=0.9)
            if not un_select_location:
                QMessageBox.warning(self, "错误", "未找到组织架构这一菜单栏")
                return
            # 进入组织架构
            pyautogui.click(un_select_location)

        new_customer_selected = pyautogui.locateCenterOnScreen('./stepPic/new_customer_selected.png', confidence=0.9)
        if not new_customer_selected:
            new_customer_un_select = pyautogui.locateCenterOnScreen('./stepPic/new_customer_un_select.png',
                                                                    confidence=0.9)
            if not new_customer_un_select:
                QMessageBox.warning(self, "错误", "未找到<新的客户>")
                return
            pyautogui.click(new_customer_un_select)

        # 开始循环添加用户
        for [row, friend_info] in enumerate(self.friend_infos):
            if friend_info["state"] != PhoneState.Waiting:
                continue
            try:
                state = self.add_friend(friend_info["phone"])
            except RuntimeError as e:
                QMessageBox.warning(self, "错误", str(e))
                return
            state_item = QTableWidgetItem(str(state))
            if friend_info["state"] == PhoneState.Failed:
                state_item.setBackground(QColor(255, 0, 0))
            elif friend_info["state"] == PhoneState.Succeed:
                state_item.setBackground(QColor(0, 255, 0))
            self.phoneTable.setItem(row, 2, state_item)

            # 间隔指定秒数
            time.sleep(self.delayTimeBox.Value())

        QMessageBox.information(self, "信息", "完成添加任务")

    @staticmethod
    def add_friend(phone):
        add_icon = pyautogui.locateCenterOnScreen('./stepPic/add_icon.png', confidence=0.9)
        if not add_icon:
            raise RuntimeError("未找到添加按钮")
        pyautogui.click(add_icon)
        input_tel_icon = pyautogui.locateCenterOnScreen('./stepPic/input_tel_icon.png', confidence=0.9)
        if not input_tel_icon:
            raise RuntimeError("未找到输入栏")
        pyautogui.click(input_tel_icon)
        pyautogui.typewrite(phone, interval=0.25)
        time.sleep(1)
        # 查找用户
        search_result = pyautogui.locateCenterOnScreen('./stepPic/search_result.png', confidence=0.9)
        if not search_result:
            not_found_user = pyautogui.locateCenterOnScreen('./stepPic/not_found_user.png', confidence=0.9)
            if not_found_user:
                confirm_not_found_user = pyautogui.locateCenterOnScreen('./stepPic/confirm_not_user.png', confidence=0.9)
                pyautogui.click(confirm_not_found_user)
                return PhoneState.Failed
        # 处理已添加 和 未添加
        add = pyautogui.locateCenterOnScreen('./stepPic/add.png')
        if not add:
            has_added = pyautogui.locateCenterOnScreen('./stepPic/has_added.png')
            if has_added:
                return PhoneState.Succeed
            else:
                raise RuntimeError("未知错误")
        pyautogui.click(add)
        time.sleep(2)
        send = pyautogui.locateCenterOnScreen('./stepPic/send.png', confidence=0.9)
        if not send:
            raise RuntimeError("未找到发送按钮")
        pyautogui.click(send)
        time.sleep(2)
        return PhoneState.Succeed

def main():
    # 初始化app
    app = QApplication(sys.argv)
    # 设置软件图标
    app.setWindowIcon(QIcon("ui/resources/logo.ico"))
    # 初始化第一个窗口
    my_win = MyMainWindow()
    # 显示窗口
    my_win.show()
    # 如果碰到软件关闭则关闭进程
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
