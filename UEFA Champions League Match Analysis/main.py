import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("champions_league_matches.csv")
# print(df.to_string())

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# ------------------------------
# 1.Total number of teams
#-------------------------------

teams = pd.concat([df['home_team'], df['away_team']])
print("Total teams:", teams.nunique())

#-------------------------------
# 2.Total number of matches
#-------------------------------

total_matches = df.shape[0]
print("Total number of matches : ",total_matches)

#--------------------------------
# 3.The venue which hosted matches
#--------------------------------

host = df["venue"].unique()
print("Total number of hosts : ",len(host))
for i in host:
    print("Match hosted at : ",i)

#--------------------------------
# 4.Removing the missing values
#--------------------------------

missing = df.dropna(how='all')
print(missing.head())

#-------------------------------
# 5.How many home wins
#-------------------------------

home_win = (df["result"] =="Home Win").sum()
away_win = (df["result"] =="Away Win").sum()
draw = (df["result"]=="Draw").sum()

print("Home Wins:", home_win)
print("Away Wins:", away_win)
print("Draws:", draw)

#------------------------------
# 6.Does higher possession lead to winning
#------------------------------

df["higher_possession_team"] = np.where(
    df["home_possession"] > df["away_possession"], "home",
    np.where(df["away_possession"] > df["home_possession"], "away", "equal")
)

home_higher = df[df["higher_possession_team"] == "home"]
away_higher = df[df["higher_possession_team"] == "away"]

home_wins = (home_higher["winner"] == home_higher["home_team"]).sum()
away_wins = (away_higher["winner"] == away_higher["away_team"]).sum()

total_cases = len(home_higher) + len(away_higher)
wins_with_higher_possession = home_wins + away_wins

percentage = (wins_with_higher_possession / total_cases) * 100
home_pct = (home_wins / total_matches) * 100
away_pct = (away_wins / total_matches) * 100
draw_pct = (draw / total_matches) * 100

print("Home Win %:", home_pct)
print("Away Win %:", away_pct)
print("Draw %:", draw_pct)
print("Winning percentage with higher possession:", percentage)


#------------------------------------
# 7.Shooting Efficiency Analysis
#------------------------------------

home_shots = df.groupby("home_team")["home_shots_on_target"].sum()
away_shots = df.groupby("away_team")["away_shots_on_target"].sum()

total_shots = home_shots.add(away_shots, fill_value=0)

top_teams = total_shots.sort_values(ascending=False)

print("The top 10 teams are")
print(top_teams.head(10))

df["higher_accuracy_team"] = np.where(
    df["home_shots_on_target_pct"] > df["away_shots_on_target_pct"], "home",
    np.where(df["away_shots_on_target_pct"] > df["home_shots_on_target_pct"], "away", "equal")
)
home_accuracy = df[df["higher_accuracy_team"] == "home"]
away_accuracy = df[df["higher_accuracy_team"] == "away"]

home_accuracy_wins = (home_accuracy["winner"] == home_accuracy["home_team"]).sum()
away_accuracy_wins = (away_accuracy["winner"] == away_accuracy["away_team"]).sum()

total_cases = len(home_accuracy) + len(away_accuracy)
wins = home_accuracy_wins + away_accuracy_wins

accuracy_win_percentage = (wins / total_cases) * 100

print("Win percentage when team had higher shot accuracy:", accuracy_win_percentage)


#-----------------------------
# 8.Goalkeeper Performance
#-----------------------------

# Which teams have the best goalkeeping performance?
# Average save percentage in matches

home_save = df[df["home_saves"] > df["away_saves"]]
away_save = df[df["away_saves"] > df["home_saves"]]

best_performance_home = (home_save["winner"] == home_save["home_team"]).sum()
best_performance_away = (away_save["winner"] == away_save["away_team"]).sum()

total_cases = len(home_save) + len(away_save)
win = best_performance_home + best_performance_away

if total_cases > 0:
    save = (win / total_cases) * 100
    print("Win percentage when team made more saves:", save)
else:
    print("No matches to analyze for saves.")


#-----------------------------
# 9.Referee Analysis
#-----------------------------

# Which referees officiated most matches?
referee_matches = df["referee"].value_counts()
print(referee_matches)

# Top five reference
print(referee_matches.head(5))


#-----------------------------
# 10. Winning Team Analysis
#-----------------------------

# Which teams won the most matches?
team_won = df["winner"].value_counts()
print("Most team won by the team :-",team_won)

# Top 5 most successful teams
team_won = df[df["winner"] != "Draw"]["winner"].value_counts()

print("Top 5 most successful teams:")
print(team_won.head(5))


#-----------------------------
# 10. Visualizations
#-----------------------------

plt.figure(figsize=(12,8))

# Pie chart - Match results distribution
plt.subplot(2,2,1)
result_count = df["result"].value_counts()
plt.pie(result_count.values, labels=result_count.index, autopct='%1.1f%%')
plt.title("Match Results Distribution")

# Bar chart - Top 5 Teams with most wins
plt.subplot(2,2,2)
plt.bar(team_won.head(5).index, team_won.head(5).values)
plt.title("Top 5 Teams With Most Wins")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)

# Histogram - Possession distribution
plt.subplot(2,2,3)
plt.hist(df["home_possession"].dropna(), bins=10, alpha=0.5, label="Home")
plt.hist(df["away_possession"].dropna(), bins=10, alpha=0.5, label="Away")
plt.title("Possession Distribution")
plt.xlabel("Possession %")
plt.ylabel("Number of Matches")
plt.legend()

# Bar chart → Shots on target by team
plt.subplot(2,2,4)
plt.bar(home_shots.head(5).index, home_shots.head(5).values)

plt.title("Top Teams by Shots on Target")
plt.xlabel("Teams")
plt.ylabel("Shots on Target")
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
