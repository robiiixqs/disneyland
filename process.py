"""Read and process the Disneyland review dataset."""

import csv


def load_data(file_path):
    """Read the CSV file and return its rows in a list."""
    with open(
        file_path, "r", encoding="utf-8-sig", newline=""
    ) as csv_file:
        return list(csv.DictReader(csv_file))


def get_parks(dataset):
    """Return the park names found in the dataset."""
    return sorted({review["Branch"] for review in dataset})


def match_park(dataset, user_entry):
    """Match the user's entry to a park in the dataset."""
    cleaned_entry = user_entry.strip().replace(" ", "_").lower()

    for park in get_parks(dataset):
        if park.lower() == cleaned_entry:
            return park

    return None


def get_reviews_by_park(dataset, park):
    """Return all reviews for the selected park."""
    matching_reviews = []

    for review in dataset:
        if review["Branch"] == park:
            matching_reviews.append(review)

    return matching_reviews


def count_reviews_by_park_and_location(
    dataset, park, location
):
    """Count reviews for a park from a reviewer location."""
    count = 0

    for review in dataset:
        park_matches = review["Branch"] == park
        location_matches = (
            review["Reviewer_Location"].lower()
            == location.strip().lower()
        )

        if park_matches and location_matches:
            count += 1

    return count


def calculate_average_by_park_and_year(
    dataset, park, year
):
    """Calculate the average park rating for a year."""
    ratings = []

    for review in dataset:
        review_year = review["Year_Month"].split("-")[0]

        if review["Branch"] == park and review_year == str(year):
            ratings.append(int(review["Rating"]))

    if len(ratings) == 0:
        return None

    return sum(ratings) / len(ratings)