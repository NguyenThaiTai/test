#QHBoxLayout: Bố cục ngang tuyến tính
#QVBoxLayout: Bố cục dọc tuyến tính
#QGridLayout: Bố cục dạng lưới
#QStackedLayout: Bố cục dạng chồng lên nhau

#Container: để chứa các widget
#Các thành phần trong container bao gồm:
#QGroupBox: chứa các widget có liên quan với nhau
#QScrollArea: Một vùng cuộn (Có thể lăn chuột được) chứa các widget
#QStackWidget: Một cửa sổ chứa các widget có thể chồng lên nhau
#QTabWidget: Một cửa sổ chứa các widget được chia thành các tab

#Các container trong QTdesigner đã có áp dụng bố cục cho các thành phần khi đặt bên trong nó
#Tuy nhiên một số thành phần container chưa áp dụng bố cục như: QWidget, QFrame

#Các bước áp dụng bố cục cho container bằng kéo thả:
#1. Kéo các thành phần giao diện vào container
#2. Nhấn chuột phải vào container
#3. Chọn layout -> Chọn các bố cục muốn áp dụng cho container

#Ngoài ra có thể kéo thả layout trong QTDesigner để có các container đã áp dụng sẵn bố cục

#Các bước áp dụng bố cục cho container bằng lập trình
import sys
from PyQt6.QtWidgets import (
    QMainWindow,QApplication,QPushButton,
    QCheckBox, QComboBox, QDateEdit, QFontComboBox,
    QLineEdit, QRadioButton, QSlider, QGridLayout,
    QSpinBox, QVBoxLayout, QWidget, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.layout = QHBoxLayout()
        self.widgets = [QCheckBox,
                        QComboBox,
                        QDateEdit,
                        QFontComboBox,
                        QLineEdit,
                        QPushButton,
                        QRadioButton,
                        QSlider,
                        QSpinBox]
        
        for w in self.widgets:
            self.layout.addWidget(w()) #Phương thức thêm widget vào layout đã tạo

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout) #Phương thức gán layout cho container đã tạo
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())