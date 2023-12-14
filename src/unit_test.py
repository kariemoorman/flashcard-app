import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from flashcard_app import FlashcardApp

class TestFlashcardApp(unittest.TestCase):
    def setUp(self):
        self.test_flashcards = [
            ("Test Question 1", "Test Answer 1"),
            ("Test Question 2", "Test Answer 2")
        ]

        self.app = QApplication([])

    def test_initialization(self):
        flashcard_app = FlashcardApp(self.test_flashcards)

    def test_next_card(self):
        flashcard_app = FlashcardApp(self.test_flashcards)
        initial_card = flashcard_app.current_card

        QTest.mouseClick(flashcard_app.next_button, Qt.LeftButton)
        self.assertEqual(flashcard_app.current_card, initial_card + 1)

    def test_prev_card(self):
        flashcard_app = FlashcardApp(self.test_flashcards)
        flashcard_app.current_card = 1

        QTest.mouseClick(flashcard_app.prev_button, Qt.LeftButton)
        self.assertEqual(flashcard_app.current_card, 0)

    def test_reveal_answer(self):
        flashcard_app = FlashcardApp(self.test_flashcards)

        QTest.mouseClick(flashcard_app.reveal_button, Qt.LeftButton)
        self.assertIsNotNone(flashcard_app.answer_label.text())

    def test_show_flashcard(self):
        flashcard_app = FlashcardApp(self.test_flashcards)
        flashcard_app.current_card = 1

        flashcard_app.show_flashcard()
        self.assertEqual(flashcard_app.question_label.text(), self.test_flashcards[1][0])

if __name__ == '__main__':
    unittest.main()
