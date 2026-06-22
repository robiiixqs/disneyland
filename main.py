"""Add continuous menu and input validation"""

from pathlib import Path

import process
import tui

DATA_FILE = Path(__file__).with_name("disneyland_reviews.csv")


def run():
    """Load the dataset and keep displaying the menu until exit."""
    tui.display_title()

    try:
        reviews = process.load_data(DATA_FILE)
    except (FileNotFoundError, OSError) as error:
        tui.display_error(f"Unable to load dataset: {error}")
        return

    tui.display_data_loaded(len(reviews))

    while True:
        choice = tui.get_main_menu_choice()

        if choice == "A":
            tui.display_message("you have chosen option A - View Data")
            tui.get_view_data_choice()
        elif choice == "B":
            tui.display_message("yu have chosen option B - Visualise Data")
            tui.get_visualise_data_choice()
        elif choice == "X":
            tui.display_message("thank you for using the program.")
            break
        else:
            tui.display_error("Please enter A, B or X.")


if __name__ == "__main__":
    run()