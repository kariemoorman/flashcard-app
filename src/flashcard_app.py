import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import argparse


class FlashcardApp(QWidget):
    def __init__(self, flashcards):
        super().__init__()

        self.flashcards = flashcards
        self.current_card = 0

        self.setWindowTitle("Flashcards")
        self.setGeometry(100, 100, 600, 400)

        question_font = QFont("Helvetica", 18)
        answer_font = QFont("Helvetica", 16)

        self.question_label = QLabel(self)
        self.question_label.setFont(question_font)

        self.answer_label = QLabel(self)
        self.answer_label.setFont(answer_font)

        self.next_button = QPushButton("Next", self)
        self.prev_button = QPushButton("Previous", self)
        self.reveal_button = QPushButton("Reveal", self)

        self.next_button.clicked.connect(self.next_card)
        self.prev_button.clicked.connect(self.prev_card)
        self.reveal_button.clicked.connect(self.reveal_answer)

        layout = QVBoxLayout(self)
        
        self.question_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setWordWrap(True)

        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_label)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.prev_button, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.next_button, alignment=Qt.AlignCenter)

        layout.addLayout(button_layout)
        layout.addWidget(self.reveal_button, alignment=Qt.AlignCenter)
        
        self.show_flashcard()

    def next_card(self):
        self.current_card += 1
        if self.current_card < len(self.flashcards):
            self.show_flashcard()
        else:
            QMessageBox.information(self, "Flashcards", "No more flashcards!")

    def prev_card(self):
        self.current_card -= 1
        if self.current_card >= 0:
            self.show_flashcard()

    def show_flashcard(self):
        self.question_label.setText(self.flashcards[self.current_card][0])
        self.answer_label.clear()

    def reveal_answer(self):
        self.answer_label.setText(self.flashcards[self.current_card][1])

def main(flashcards_file):
    try:
        with open(flashcards_file, "r") as file:
            flashcard_lines = file.readlines()
            flashcards = [line.strip().split(', ', 1) for line in flashcard_lines]
            flashcards = [(question.strip('"'), answer.strip('"')) for question, answer in flashcards]
    except FileNotFoundError:
        print(f"Flashcards file '{flashcards_file}' not found.")

    app = QApplication(sys.argv)
    flashcard_app = FlashcardApp(flashcards)
    flashcard_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flashcard App")
    parser.add_argument("-f", "--flashcards", type=str, help="Path to the flashcards file.")
    args = parser.parse_args()
    main(args.flashcards)
