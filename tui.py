"""Display information and receive input from the user."""


def display_title():
    """Display the program title."""
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))


def display_data_loaded(row_count):
    """Confirm that the dataset has loaded."""
    print("\nDataset loaded successfully.")
    print(f"The dataset contains {row_count:,} rows.\n")


def get_main_menu_choice():
    """Display the main menu and return the user's choice."""
    print(
        "Please enter the letter which corresponds with your "
        "desired menu choice:"
    )
    print("\t[A] View Data")
    print("\t[B] Visualise Data")
    print("\t[X] Exit")

    return input("> ").strip().upper()


def get_view_data_choice():
    """Display the View Data submenu."""
    print("\nPlease enter one of the following options:")
    print("\t[A] View Reviews by Park")
    print(
        "\t[B] Number of Reviews by Park and Reviewer Location"
    )
    print("\t[C] Average Score per year by Park")
    print("\t[D] Average Score per Park by Reviewer Location")
    print("\t[X] Return to Main Menu")

    return input("> ").strip().upper()


def get_visualise_data_choice():
    """Display the Visualise Data submenu."""
    print("\nPlease enter one of the following options:")
    print("\t[A] Most Reviewed Parks")
    print("\t[B] Park Ranking by Nationality")
    print("\t[C] Most Popular Month by Park")

    return input("> ").strip().upper()


def get_park(parks):
    """Display the parks and ask the user to select one."""
    print("\nAvailable parks:")

    for park in parks:
        print(f"\t{park}")

    return input("Enter a park: ")


def get_location():
    """Ask the user for a reviewer location."""
    return input("Enter a reviewer location: ").strip()


def get_year():
    """Ask for and validate a four-digit year."""
    while True:
        year = input("Enter a four-digit year: ").strip()

        if year.isdigit() and len(year) == 4:
            return int(year)

        display_error("Please enter a valid four-digit year.")


def display_reviews(reviews):
    """Display reviews for a selected park."""
    if not reviews:
        display_message("No reviews were found.")
        return

    print(f"\n{len(reviews):,} reviews found:")
    print("Review ID   Rating   Date      Reviewer Location")
    print("-" * 65)

    for review in reviews:
        print(
            f"{review['Review_ID']:<11} "
            f"{review['Rating']:<8} "
            f"{review['Year_Month']:<9} "
            f"{review['Reviewer_Location']}"
        )


def display_review_count(park, location, count):
    """Display the number of matching reviews."""
    display_message(
        f"{park} received {count:,} reviews from {location}."
    )


def display_average_rating(park, year, average):
    """Display the average rating."""
    if average is None:
        display_message(
            f"No reviews were found for {park} in {year}."
        )
    else:
        display_message(
            f"The average rating for {park} in {year} was "
            f"{average:.2f} out of 5."
        )


def display_message(message):
    """Display a normal message."""
    print(f"\n{message}\n")


def display_error(message):
    """Display an error message."""
    print(f"\nError: {message}\n")