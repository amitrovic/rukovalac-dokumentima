from PySide2.QtCore import QAbstractItemModel, QModelIndex, Qt

class DocumentModel(QAbstractItemModel):
    def __init__(self, document, parent=None):
        super().__init__(parent)
        self.document = document

    def index(self, row, column, parent=QModelIndex()):
        # vracamo indeks koji je indeks dokumenta (stranica na zadatom redu)
        # FIXME: dodati provere da li je validan indeks (red, kolona)
        return self.createIndex(row, column, self.document.pages[row])

    def parent(self, child):
        # FIXME: ukoliko je dublja hijerarhijska struktura generisati indeks preko createIndex metode
        # dodatno, potrebno je modifikovati model tako da bude laksi za snalazenje (na narednim vezbama demonstracija)
        # TODO: obavezno proveriti da li je indeks deteta validan child.isValid()
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return len(self.document.pages)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def data(self, index, role=Qt.DisplayRole):
        # FIXME: proveriti da li je indeks validan
        element = index.internalPointer()

        if index.column() == 0 and role == Qt.DisplayRole:
            return element.title
        elif index.column() == 1 and role == Qt.DisplayRole:
            return element.text
        elif index.column() == 2 and role == Qt.DisplayRole:
            return element.page_number
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if section == 0 and role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "Naslov"
        elif section == 1 and role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "Sadrzaj"
        elif section == 2 and role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "Broj strane"
        return None

    # Za editable model su potrebne i sledece dve metode
    def setData(self, index, data, role=Qt.EditRole):
        element = index.internalPointer() # page
        if index.column() == 0:
            # setovati naslov
            element.title = data
        elif index.column() == 1:
            # setovati sadrzaj
            element.text = data
        elif index.column() == 2:
            # setovati broj strane
            try:
                element.page_number = int(data)
            except ValueError:
                return False
        else:
            return False
        # emitovanje signala kako bi se naznacila promena u modelu
        self.dataChanged.emit(index, index, None)
        return True

    def flags(self, index):
        return super().flags(index) | Qt.ItemIsEditable # | - ili nad bitovima
