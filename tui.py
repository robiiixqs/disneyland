"Add menus and text user interface"""

def display_title():
    """Display the program title with matching dashed lines."""
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))


def display_data_loaded(row_count):
    """Confirm that the dataset has been loaded."""
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
    """Display the View Data submenu and receive a choice."""
    print("Please enter one of the following options:")
    print("\t[A] View Reviews by Park")
    print("\t[B] Number of Reviews by Park and Reviewer Location")
    print("\t[C] Average Score per year by Park")
    print("\t[D] Average Score per Park by Reviewer Location")
    return input("> ").strip().upper()


def get_visualise_data_choice():
    """Display the Visualise Data submenu and receive a choice."""
    print("Please enter one of the following options:")
    print("\t[A] Most Reviewed Parks")
    print("\t[B] Park Ranking by Nationality")
    print("\t[C] Most Popular Month by Park")
    return input("> ").strip().upper()


def display_message(message):
    """Display a normal program message."""
    print(f"\n{message}\n")


def display_error(message):
    """Display an error message."""
    print(f"\nError: {message}\n")
