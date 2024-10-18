# Fair Commander
This is an alternative format of commander, with rulings looking to fair play.

# How to Run
1. Install `python` in your system.
2. Edit the `deck.json` file with your deck

Be sure to follow the format of ```["card 1", "card 2"]```

3. Install `poetry` in your system
```
python3 -m pip install pipx
python3 -m pipx install poetry
```

4. Run the program
```
poetry run python -m fair_commander
```

# How to Create the database:
1. Download the "Default Cards" database from [Scryfall.com](https://scryfall.com/docs/api/bulk-data) and place it in the `data` directory.
2. Change the name in line 4 of `generate_database.py` according to the downloaded file.
3. Run `python3 generate_database.py`
