"""Control the program flow for the Disneyland Review Analyser."""

from pathlib import Path

import process
import tui


DATA_FILE = (
    Path(__file__).parent
    / "data"
    / "disneyland_reviews.csv"
)

def request_park(reviews):
    """Ask for a park and validate it against the dataset."""
    parks = process.get_parks(reviews)
    entered_park = tui.get_park(parks)
    park = process.match_park(reviews, entered_park)

    if park is None:
        tui.display_error("That park was not found in the dataset.")

    return park


def handle_view_data(reviews):
    """Run the View Data submenu."""
    while True:
        choice = tui.get_view_data_choice()

        if choice == "X":
            return

        if choice == "A":
            park = request_park(reviews)

            if park:
                matching_reviews = process.get_reviews_by_park(
                    reviews, park
                )
                tui.display_reviews(matching_reviews)

        elif choice == "B":
            park = request_park(reviews)

            if park:
                location = tui.get_location()
                count = process.count_reviews_by_park_and_location(
                    reviews, park, location
                )
                tui.display_review_count(park, location, count)

        elif choice == "C":
            park = request_park(reviews)

            if park:
                year = tui.get_year()
                average = process.calculate_average_by_park_and_year(
                    reviews, park, year
                )
                tui.display_average_rating(park, year, average)

        elif choice == "D":
            tui.display_message(
                "This option belongs to Section D and is not implemented."
            )

        else:
            tui.display_error("Please enter A, B, C, D or X.")


def run():
    """Load the dataset and display the menus."""
    tui.display_title()

    try:
        reviews = process.load_data(DATA_FILE)
    except (FileNotFoundError, OSError) as error:
        tui.display_error(f"Unable to load the dataset: {error}")
        return

    tui.display_data_loaded(len(reviews))

    while True:
        choice = tui.get_main_menu_choice()

        if choice == "A":
            tui.display_message("You have chosen option A - View Data")
            handle_view_data(reviews)

        elif choice == "B":
            tui.display_message(
                "You have chosen option B - Visualise Data"
            )
            tui.get_visualise_data_choice()

        elif choice == "X":
            tui.display_message("Thank you for using the program.")
            break

        else:
            tui.display_error("Please enter A, B or X.")


if __name__ == "__main__":
    run()