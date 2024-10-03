import json

with open(
    "data/default-cards-*.json", mode="r", encoding="utf-8"
) as read_cards:
    card_database = json.load(read_cards)

allowed_cards = []

with open("data/gueEDHs_database.json", "w") as outfile:
    for card_oracle in card_database:
        if card_oracle["reserved"]:
            continue
        if card_oracle["set_type"] == "expansion" or card_oracle["set_type"] == "core":
            allowed_cards.append(card_oracle["name"])

    json.dump(allowed_cards, outfile)
