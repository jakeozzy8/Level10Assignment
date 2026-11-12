import pandas as pd

football_data = pd.read_csv("cfb.csv")

select_season = int(input("Enter a season to analyze: "))

matches = football_data["Season"] == select_season
season_data = football_data[matches]

if len(season_data) == 0:
    print(f"Sorry, no data was found for the {select_season} season.")
else:
    win_categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    for index, row in season_data.iterrows():
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

    print(f"College Football Results for {select_season}")
    print("-" * 34)

    for category, teams in win_categories.items():
        print()
        print(f"{category}:")
        for team in teams:
            print(team)
