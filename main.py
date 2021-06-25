import sys
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import xtool

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

if __name__ == '__main__':
    # 初始化app
    app = QApplication(sys.argv)
    # 初始化第一个窗口
    MainWindow = QMainWindow()
    # 调用ui绘制窗口
    ui = xtool.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # 设置软件图标
    app.setWindowIcon(QIcon("ui/resources/logo.ico"))
    # 设置软件标题
    MainWindow.setWindowTitle("企业微信自动加人工具")
    # 显示窗口
    MainWindow.show()
    # 如果碰到软件关闭则关闭进程
    sys.exit(app.exec_())
