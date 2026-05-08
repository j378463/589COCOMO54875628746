import re
import json
import csv
from datetime import datetime
from typing import List, Dict
import unittest


class PalindromeChecker:
    """Main class responsible for palindrome checking and input processing."""

    def clean_input(self, text: str) -> str:
        """Clean input: remove non-alphanumeric characters and convert to lowercase."""
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return re.sub(r'[^a-zA-Z0-9]', '', text.lower())

    def is_palindrome(self, text: str) -> bool:
        """Check if the input is a palindrome after cleaning."""
        cleaned = self.clean_input(text)
        if not cleaned:
            raise ValueError("Input cannot be empty or contain only punctuation/spaces")
        return cleaned == cleaned[::-1]

    def get_category(self, text: str) -> str:
        """Determine category: Word, Sentence, or Number."""
        cleaned = self.clean_input(text)
        if cleaned.isdigit():
            return "Number"
        elif ' ' in text or any(c.isspace() for c in text):
            return "Sentence"
        else:
            return "Word" if len(cleaned) > 0 else "Unknown"


class SessionManager:
    """Manages session history, leaderboard, and exports."""

    def __init__(self):
        self.history: List[Dict] = []

    def add_result(self, input_text: str, is_pal: bool, category: str):
        """Add a result to session history."""
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": input_text,
            "is_palindrome": is_pal,
            "category": category,
            "length": len(input_text)
        })

    def show_leaderboard(self, top_n: int = 10):
        """Display leaderboard of longest palindromes."""
        if not self.history:
            print("No entries yet.")
            return

        palindromes = [entry for entry in self.history if entry["is_palindrome"]]
        sorted_pal = sorted(palindromes, key=lambda x: x["length"], reverse=True)

        print(f"\n--- Top {top_n} Palindromes Leaderboard ---")
        for i, entry in enumerate(sorted_pal[:top_n], 1):
            print(f"{i}. '{entry['input']}' (Length: {entry['length']})")

    def export_to_json(self, filename: str = "palindrome_session.json"):
        """Export session history to JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2)

    def export_to_csv(self, filename: str = "palindrome_session.csv"):
        """Export session history to CSV file."""
        if not self.history:
            return
        keys = self.history[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.history)


# ====================== AUTOMATED TESTS ======================
class TestPalindromeChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PalindromeChecker()

    def test_palindromes(self):
        self.assertTrue(self.checker.is_palindrome("radar"))
        self.assertTrue(self.checker.is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(self.checker.is_palindrome("12321"))
        self.assertTrue(self.checker.is_palindrome("Able was I ere I saw Elba"))

    def test_non_palindromes(self):
        self.assertFalse(self.checker.is_palindrome("hello"))
        self.assertFalse(self.checker.is_palindrome("A man a plan"))

    def test_validation(self):
        with self.assertRaises(ValueError):
            self.checker.is_palindrome("")
        with self.assertRaises(ValueError):
            self.checker.is_palindrome(123)  # Wrong type

    def test_category(self):
        self.assertEqual(self.checker.get_category("radar"), "Word")
        self.assertEqual(self.checker.get_category("A man a plan a canal Panama"), "Sentence")
        self.assertEqual(self.checker.get_category("12321"), "Number")
        self.assertEqual(self.checker.get_category("!@#$%^"), "Unknown")


def main():
    """Main application loop."""
    print("=== Palindrome Checker ===\n")
    print("Type 'quit' to exit anytime.\n")

    checker = PalindromeChecker()
    session = SessionManager()

    while True:
        user_input = input("Enter text: ").strip()
        if user_input.lower() == 'quit':
            break

        try:
            is_pal = checker.is_palindrome(user_input)
            category = checker.get_category(user_input)

            print(f"Cleaned : '{checker.clean_input(user_input)}'")
            print(f"Result  : {'✅ Palindrome' if is_pal else '❌ Not a palindrome'}")
            print(f"Category: {category}\n")

            session.add_result(user_input, is_pal, category)

        except ValueError as e:
            print(f"Error: {e}\n")

    # Final session summary
    if session.history:
        session.show_leaderboard()
        session.export_to_json()
        session.export_to_csv()
        print("\n✅ Session exported to 'palindrome_session.json' and 'palindrome_session.csv'")


if __name__ == "__main__":
    # Run tests first when executing directly (optional)
    print("Running automated tests...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=1)
    print("\n" + "="*50 + "\n")
    
    main()
