class Page:
    def __init__(self, title="", text="", page_number=1):
        self.title = title
        self.text = text
        self.page_number = page_number

    def add_text(self, text):
        self.text += text