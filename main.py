""" This is a checker for legality for a deck in the guEDHs format. """

import json
from pathlib import Path

DATABASE = Path("data/default-cards-20240924090726.json")
GUEDHS_DATABASE = Path("data/fair_commander_database.json")
BANLIST = Path("data/banlist.json")
DECK = Path("deck.json")


def check_database_exists():
    pass

def open_card_database():
    with open("data/fair_commander_database.json", mode="r", encoding="utf-8") as read_cards:
        card_database = json.load(read_cards)
        return set(card_database)

def open_banlist() -> str:
    """TODO Open banlist file."""
    with open("deck.json", mode="r", encoding="utf-8") as deck:
        my_deck = json.load(deck)
        return set(my_deck)

def open_deck() -> str:
    """TODO Open deck file."""
    with open("deck.json", mode="r", encoding="utf-8") as deck:
        my_deck = json.load(deck)
        return set(my_deck)


def check_deck_validity() -> None:
    valid_deck = True

    database_set = open_card_database()
    deck = open_deck()
    banlist = open_banlist()

    print("Your deck: ")
    print(deck)
    print("Starting the search...")
    for card_deck in deck:
        if card_deck in banlist:
            print(card_deck, "is banned")
            valid_deck = False
            continue

        if card_deck in database_set:
            print(card_deck, "is valid")
        else:
            print(card_deck, "is banned")
            valid_deck = False

    if valid_deck:
        print("Your deck is valid!")
    else:
        print("Your deck is not valid!")


def main():
    check_deck_validity()


if __name__ == "__main__":
    main()
