""" This is a checker for legality for a deck in the guEDHs format. """

import json
from pathlib import Path

DATABASE = Path("data/default-cards-20240924090726.json")
FAIR_COMMANDER_DATABASE = Path("data/fair_commander_database.json")
BANLIST = Path("ban_list.json")
DECK = Path("deck.json")

def check_database_exists() -> bool:
    pass

def open_card_database() -> set[str]:
    with open(FAIR_COMMANDER_DATABASE, mode="r", encoding="utf-8") as read_cards:
        card_database = json.load(read_cards)
        return set(card_database)

def open_banlist() -> set[str]:
    """Open banlist file."""
    with open(BANLIST, mode="r", encoding="utf-8") as banlist:
        _banlist = json.load(banlist)
        return set(_banlist)

def open_deck() -> set[str]:
    """TODO Open deck file."""
    with open(DECK, mode="r", encoding="utf-8") as deck:
        _deck = json.load(deck)
        return set(_deck)

def check_deck_validity() -> None:
    valid_deck = True

    database_set = open_card_database()
    deck = open_deck()
    banlist = open_banlist()

    print("Starting the search...")
  
    for card_deck in deck:
        if card_deck in banlist or card_deck not in database_set:
            print(card_deck, "is banned")
            valid_deck = False
            continue

    if valid_deck:
        print("Your deck is valid!")
    else:
        print("Your deck is not valid!")


def main() -> None:
    check_deck_validity()

if __name__ == "__main__":
    main()
