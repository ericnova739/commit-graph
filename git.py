import os

with open("test.txt", "r") as f:
    dates = f.readlines()

for date in dates:
    date = date.strip()

    with open("file.txt", "a") as file:
        file.write(date + "\n")

    os.system("git add .")
    os.system(f'GIT_AUTHOR_DATE="{date}T12:00:00" GIT_COMMITTER_DATE="{date}T12:00:00" git commit -m "commit on {date}"')
