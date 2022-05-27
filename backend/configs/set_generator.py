import json
import requests

class SetGenerator():

    def __init__(self):
        self.response = None
        self.encounters = []
        self.agendas = []
        self.acts = []
        self.locations = []
        self.title = ''
        self.game_type = ''
        self.set_name = ''

    def parse_cards(self):
        for card in self.response:
            print(card.get("code"),card.get("name"), card.get("type_code"))
            if card.get('type_code') == 'encounter':
                self.encounters.append(card)

            if card.get('type_code') == 'agenda':
                self.agendas.append(card)

            if card.get('type_code') == 'location':
                self.locations.append(card)
        
            if card.get('type_code') == 'act':
                self.acts.append(card)

            # if card.get('type_code') == '':
            #     self.encounters.append(card.get('code'))

    def write_config(self):
        self.parse_cards()
        config = {
            "title": self.title,
            "type": self.game_type,
            "locations": self.locations,
            "encounters": self.encounters,
            "agenda": self.agendas,
            "acts": self.acts
        }

        with open(f"{self.set_name}.json") as j:
            j.write(json.dumps(config))
    
    def generate_config(self):
        self.parse_cards()
        config = {
            "title": self.title,
            "type": self.game_type,
            "locations": self.locations,
            "encounters": self.encounters,
            "agenda": self.agendas,
            "acts": self.acts
        }
 
        return config