from PySide2 import QtWidgets, QtCore, QtGui


# FIXME: Raspodeliti nadleznosti na druge view-ove.
class MainWindow(QtWidgets.QMainWindow):
    """
    Klasa koja predstavlja glavni prozor.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Podesavanje prozora
        self.setWindowTitle("Rukovalac dokumentima")
        self.setWindowIcon(QtGui.QIcon("resources/icons/icons8-product-documents-32.png"))
        self.resize(640, 480)

        # Definisanje delova aplikacije
        self.menubar = QtWidgets.QMenuBar(self)
        self.help_menu = QtWidgets.QMenu("Help")
        self.toolbar = QtWidgets.QToolBar(self)
        self.central_widget = QtWidgets.QLabel("Centralni widget u izradi", self)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.project_dock = QtWidgets.QDockWidget(self)

        # Akcije menija
        # TODO: Dodati i ostale akcije
        self.menu_actions = {
            "about": QtWidgets.QAction("About", self.help_menu)
        }

        # Dodavanje elemenata na glavni prozor
        self._populate_main_window()
        

    def _populate_main_window(self):
        # populisanje menija
        self._populate_menus()
        # postavljanje widgeta na window
        self.setMenuBar(self.menubar)
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.statusbar)
        # postavljanje dock widgeta (mozemo ih imati proizvoljan broj)
        self.project_dock.setWidget(QtWidgets.QLabel("U izradi", self.project_dock))
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.project_dock)
        # uvezivanje akcija
        self._bind_actions()

    def _populate_menus(self):
        """
        Privatna metoda koja smesta menije u meni bar.
        """
        self.help_menu.addAction(self.menu_actions["about"])
        self.menubar.addMenu(self.help_menu)

    def _bind_actions(self):
        """
        Privatna metoda koja uvezuje reagovanje na dogadjaje.
        """
        self.menu_actions["about"].triggered.connect(self.about_action)

    def about_action(self):
        """
        Metoda koja prikazuje informacioni dijalog korisniku o aplikaciji.
        """
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "About Rukovalac dokumentima", 
                        "Autori: Studenti Univerziteta Singidunum, Centar Novi Sad.\nMentor: Aleksandra Mitrović\
                            \nPredmetni profesor: Branko Perišić", parent = self)
        msg.addButton(QtWidgets.QMessageBox.Ok)
        msg.exec_()