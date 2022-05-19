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
                self.encounters.append(card.get('code'))

            if card.get('type_code') == 'agenda':
                self.agendas.append(card.get('code'))

            if card.get('type_code') == 'location':
                self.locations.append(card.get('code'))
        
            if card.get('type_code') == 'act':
                self.acts.append(card.get('code'))

            # if card.get('type_code') == '':
            #     self.encounters.append(card.get('code'))

    def parse_encouters(self):
        pass

    def parse_agendas(self):
        pass

    def parse_acts(self):
        pass

    def parse_locations(self):
        pass

    def generate_config(self):
        config = {
            "title": self.title,
            "type": self.game_type,
            "locations": self.locations,
            "encounters": self.encounters,
            "agenda": self.agenda,
            "acts": self.acts
        }

        with open(f"{self.set_name}.json") as j:
            j.write(json.dumps(config))
