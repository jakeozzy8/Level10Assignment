import pandas as pd

# Load the college football data from the CSV file
football_data = pd.read_csv("cfb.csv")

# Ask the user which season to analyze
select_season = int(input("Enter a season to analyze: "))

# Keep only the rows for the chosen season
matches = football_data["Season"] == select_season
season_data = football_data[matches]

# Let the user know if the season isn't in the file
if len(season_data) == 0:
    print(f"Sorry, no data was found for the {select_season} season.")
else:
    # Dictionary holding a list of teams for each win category
    win_categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    # Sort each team into a category based on its number of wins
    for index, row in season_data.iterrows():
        # Remove the conference from the name, e.g. "Alabama (SEC)" -> "Alabama"
        team = row["Team"].rsplit(" (", 1)[0]
        wins = row["Win"]

        if wins >= 10:
            win_categories["10 or more wins"].append(team)
        elif wins >= 8:
            win_categories["8-9 wins"].append(team)
        elif wins >= 6:
            win_categories["6-7 wins"].append(team)
        else:
            win_categories["Fewer than 6 wins"].append(team)

    # Display the results, one category at a time
    print(f"College Football Results for {select_season}")
    print("-" * 34)

    for category, teams in win_categories.items():
        print()
        print(f"{category}:")
        for team in teams:
            print(team)
