import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QComboBox, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QMessageBox)
import pythonbible as bible
from main import get_random_verse, get_points, find_dist_away, BOOK_ABBREVIATIONS, total_verses_in_bible


class BibleGuessrGame(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize game state
        self.total_points = 0
        self.current_round = 1
        self.guesses = []  # List to store guessed verses and actual verses
        self.max_rounds = 5

        self.setup_ui()

        # Start a new round
        self.start_new_round()

    def setup_ui(self):
        """Setup the initial UI components."""
        layout = QVBoxLayout()

        # Display random verse text
        self.random_verse_label = QLabel("Verse: ")
        layout.addWidget(self.random_verse_label)

        # Display round and total points
        self.round_label = QLabel(f"Round: {self.current_round}/{self.max_rounds}")
        layout.addWidget(self.round_label)

        self.points_label = QLabel(f"Total Points: {self.total_points}")
        layout.addWidget(self.points_label)

        # Create dropdowns for book, chapter, and verse
        self.book_dropdown = QComboBox()
        self.book_dropdown.addItems(BOOK_ABBREVIATIONS.keys())
        self.book_dropdown.currentIndexChanged.connect(self.update_chapter_menu)
        layout.addWidget(self.book_dropdown)

        self.chapter_dropdown = QComboBox()
        self.chapter_dropdown.currentIndexChanged.connect(self.update_verse_menu)
        layout.addWidget(self.chapter_dropdown)

        self.verse_dropdown = QComboBox()
        layout.addWidget(self.verse_dropdown)

        # Add submit button
        self.submit_button = QPushButton("Submit Guess")
        self.submit_button.clicked.connect(self.submit_guess)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("Bible Guessr Game")
        self.update_chapter_menu()  # To populate initial chapter/verse dropdowns

    def start_new_round(self):
        """Start a new round by selecting a new random verse."""
        self.random_verse_id = get_random_verse()
        self.random_verse_text = bible.get_verse_text(self.random_verse_id, version=bible.Version("KJV"))
        self.random_verse_label.setText(f"Verse: {self.random_verse_text}")

    def update_chapter_menu(self):
        """Update the chapter dropdown based on the selected book."""
        selected_book = self.book_dropdown.currentText().upper()
        if selected_book in BOOK_ABBREVIATIONS:
            book = BOOK_ABBREVIATIONS[selected_book]
            total_chapters = bible.get_number_of_chapters(book)
            self.chapter_dropdown.clear()
            self.chapter_dropdown.addItems([str(i) for i in range(1, total_chapters + 1)])
            self.update_verse_menu()

    def update_verse_menu(self):
        """Update the verse dropdown based on the selected chapter."""
        selected_book = self.book_dropdown.currentText().upper()
        selected_chapter = int(self.chapter_dropdown.currentText()) if self.chapter_dropdown.currentText() else 1
        if selected_book in BOOK_ABBREVIATIONS:
            book = BOOK_ABBREVIATIONS[selected_book]
            total_verses = bible.get_number_of_verses(book, selected_chapter)
            self.verse_dropdown.clear()
            self.verse_dropdown.addItems([str(i) for i in range(1, total_verses + 1)])

    def submit_guess(self):
        """Submit the guess, calculate points, and advance the game."""
        # Get the selected book, chapter, and verse
        selected_book = self.book_dropdown.currentText().upper()
        selected_chapter = int(self.chapter_dropdown.currentText())
        selected_verse = int(self.verse_dropdown.currentText())

        if selected_book in BOOK_ABBREVIATIONS:
            book = BOOK_ABBREVIATIONS[selected_book]
            guessed_verse_id = bible.get_verse_id(book, selected_chapter, selected_verse)

            # Calculate distance between the guessed verse and the real verse
            distance = find_dist_away(self.random_verse_id, guessed_verse_id)

            # Get the maximum distance (total verses in the Bible)
            max_dist = total_verses_in_bible()

            # Calculate points and update the total
            points = get_points(distance, max_dist)
            self.total_points += points

            # Store the guess and the real verse for later display
            real_book, real_chapter, real_verse = bible.get_book_chapter_verse(self.random_verse_id)
            guessed_book, guessed_chapter, guessed_verse = bible.get_book_chapter_verse(guessed_verse_id)
            self.guesses.append({
                "real_verse": f"{real_book.name} {real_chapter}:{real_verse}",
                "guessed_verse": f"{guessed_book.name} {guessed_chapter}:{guessed_verse}",
                "points": points
            })

            # Show the real verse and guessed verse
            QMessageBox.information(self, "Round Result",
                                    f"Real verse: {real_book.name} {real_chapter}:{real_verse}\n"
                                    f"Your guess: {guessed_book.name} {guessed_chapter}:{guessed_verse}\n"
                                    f"You scored {points:.0f} points in this round.")

            # Update the display labels
            self.points_label.setText(f"Total Points: {self.total_points:.0f}")

            # Update round
            if self.current_round < self.max_rounds:
                self.current_round += 1
                self.round_label.setText(f"Round: {self.current_round}/{self.max_rounds}")
                self.start_new_round()
            else:
                # Game over, show all results and give option to play again
                self.show_final_results()

    def show_final_results(self):
        """Show all the guessed verses, real verses, and points, and offer to play again."""
        result_text = "\n".join([f"Round {i+1}: Real verse: {g['real_verse']} | Your guess: {g['guessed_verse']} | Points: {g['points']:.0f}"
                                 for i, g in enumerate(self.guesses)])
        QMessageBox.information(self, "Game Over", f"Final Results:\n\n{result_text}\n\nTotal Points: {self.total_points:.0f}")

        # Ask if the user wants to play again
        play_again = QMessageBox.question(self, "Play Again?", "Do you want to play another game?",
                                          QMessageBox.Yes | QMessageBox.No)

        if play_again == QMessageBox.Yes:
            self.reset_game()
        else:
            self.close()

    def reset_game(self):
        """Reset the game state and start a new game."""
        self.total_points = 0
        self.current_round = 1
        self.guesses = []

        self.points_label.setText(f"Total Points: {self.total_points}")
        self.round_label.setText(f"Round: {self.current_round}/{self.max_rounds}")
        self.submit_button.setEnabled(True)

        self.start_new_round()


# Main function to run the game
def main():
    app = QApplication(sys.argv)
    game = BibleGuessrGame()
    game.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
