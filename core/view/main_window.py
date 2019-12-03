from PySide2 import QtWidgets, QtCore, QtGui
from ..model.document_model import DocumentModel
from ..model.document import Document
from ..model.page import Page
from os.path import abspath


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
        self.central_widget = QtWidgets.QTabWidget(self)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.project_dock = QtWidgets.QDockWidget(self)

        # Akcije menija
        # TODO: Dodati i ostale akcije
        self.menu_actions = {
            "about": QtWidgets.QAction("About", self.help_menu)
        }

        # Dodavanje elemenata na glavni prozor
        self._populate_main_window()

    def _dummy_document(self):
        """
        Kreiranje jednog dokumenta za testiranje modela i view-a.
        """
        document = Document("test", "Aleksandra")
        page1 = Page("Modeli podataka", "Kreiranje modela na osnovu QAbstractItemModel-a")
        page2 = Page("State obrazac", "Primer i primena state obrasca", 2)
        document.add_child(page1)
        document.add_child(page2)

        document_model = DocumentModel(document)
        return document_model
        

    def _populate_main_window(self):
        # populisanje menija
        self._populate_menus()
        # postavljanje widgeta na window
        self.setMenuBar(self.menubar)
        self.addToolBar(self.toolbar)
        # populisanje tabova u centralnom widgetu
        self._populate_tab_widget()
        # postavljanje dock widgeta (mozemo ih imati proizvoljan broj)
        self._populate_project_dock()
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.statusbar)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.project_dock)
        # uvezivanje akcija
        self._bind_actions()

    def _populate_project_dock(self):
        self.project_dock.setWidget(QtWidgets.QTreeView(self.project_dock))
        # TODO: Primer za file system sadrzaj
        # model = QtWidgets.QFileSystemModel()
        # model.setRootPath(QtCore.QDir.currentPath())
        # self.project_dock.widget().setModel(model)
        # self.project_dock.widget().setRootIndex(model.index(QtCore.QDir.currentPath()))

        # primer dokument modela
        self.project_dock.widget().setModel(self.central_widget.widget(0).model())

    def _populate_tab_widget(self):
        """
            Populisati prilikom ucitavanja konteksta, kreirati sve tabove koji su bili otvoreni
            sa widgetima. Podesiti modele za svaki ucitani widget.

        """
        # dodavanje ponasanja
        self.central_widget.setTabsClosable(True)
        # populisanje
        # na osnovu liste modela se moze kreirati broj tabova
        data_table = QtWidgets.QTableView(self.central_widget)
        self.central_widget.addTab(data_table, QtGui.QIcon("resources/icons/icons8-grid-2-64.png"),
            "Document data table1")
        data_table = QtWidgets.QTableView(self.central_widget)
        self.central_widget.addTab(data_table, QtGui.QIcon("resources/icons/icons8-grid-2-64.png"),
            "Document data table2")
        data_table = QtWidgets.QTableView(self.central_widget)
        self.central_widget.addTab(data_table, QtGui.QIcon("resources/icons/icons8-grid-2-64.png"),
            "Document data table3")

        # postavljanje modela u widget-e iz tabova
        self._set_models([self._dummy_document(), self._dummy_document(), self._dummy_document()])

        self.central_widget.tabCloseRequested.connect(lambda i: self.central_widget.removeTab(i))

    def _populate_menus(self):
        """
        Privatna metoda koja smesta menije u meni bar.
        """
        self.help_menu.addAction(self.menu_actions["about"])
        self.menubar.addMenu(self.help_menu)

    def _set_models(self, models=[]):
        """
            Populise modele u tabove redom.
        """
        print(self.central_widget.count())
        for i in range(self.central_widget.count()):
            widget = self.central_widget.widget(i)
            widget.setModel(models[i])

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