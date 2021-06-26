import sys
import platform
import re
from enum import Enum
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from xtool import Ui_MainWindow

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


# 号码状态
class PhoneState(Enum):
    Waiting = 1,
    Succeed = 2,
    Failed = 3

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
        # QMessageBox.warning(self, "标题", "警告消息正文")

    def start_invite(self):
        QMessageBox.information(self, "执行", "点击了执行按钮")


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
