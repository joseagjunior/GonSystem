from PySide6.QtWidgets import(QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")

        self.btn_login.clicked.connect(self.open_system)
        self.btn_exit.clicked.connect(self.close)
    
    def open_system(self):

        if (self.txt_password.text() == 'gym4078'):
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            QMessageBox.about(self,"Alerta","Senha Inválida!")
            


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("GonSystem")
        
        #*******************PAGINAS DO SISTEMA*******************
        self.actionVoltar.triggered.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_Home))
        self.actionSair.triggered.connect(lambda: self.close())
        self.actionFuncionarios.triggered.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_CadFuncionario))
        self.actionAlunos.triggered.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_CadAluno))
        self.actionTurmas.triggered.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_CadTurma))

        #****************Botões PageFuncionario******************
        self.actionFuncionarios.triggered.connect(lambda: self.pagesFuncionario.setCurrentWidget(self.pgListFuncionario))
        self.btn_CadFuncionario.clicked.connect(lambda: self.pagesFuncionario.setCurrentWidget(self.pgCadFuncionario))
        self.btn_BackListFuncionario.clicked.connect(lambda: self.pagesFuncionario.setCurrentWidget(self.pgListFuncionario))
        self.btn_CancelFuncionario.clicked.connect(lambda: self.pagesFuncionario.setCurrentWidget(self.pgListFuncionario))
        self.btn_CancelFuncionario.clicked.connect(lambda: QMessageBox.about(self,"Cadastro","Cadastro Cancelado!"))
        self.btn_ExitCadFuncionario.clicked.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_Home))

        #****************Botões PageAluno******************
        self.actionAlunos.triggered.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgListAluno))
        self.btn_CadAluno.clicked.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgCadAluno))
        self.btn_BackListAluno.clicked.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgListAluno))
        self.btn_CancelAluno.clicked.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgListAluno))
        self.btn_CancelAluno.clicked.connect(lambda: QMessageBox.about(self,"Cadastro","Cadastro Cancelado!"))
        self.btn_ExitCadAluno.clicked.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_Home))

        #****************Botões PageTurma******************
        self.actionTurmas.triggered.connect(lambda: self.pagesTurma.setCurrentWidget(self.pgListTurma))
        self.btn_CadTurma.clicked.connect(lambda: self.pagesTurma.setCurrentWidget(self.pgCadTurma))
        self.btn_BackListAluno.clicked.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgListAluno))
        self.btn_CancelAluno.clicked.connect(lambda: self.pagesAluno.setCurrentWidget(self.pgListAluno))
        self.btn_CancelAluno.clicked.connect(lambda: QMessageBox.about(self,"Cadastro","Cadastro Cancelado!"))
        self.btn_ExitCadAluno.clicked.connect(lambda: self.pagesGeral.setCurrentWidget(self.pageG_Home))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()