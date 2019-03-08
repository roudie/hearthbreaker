import json
from hearthbreaker.serialization.serialization import serialize
class State():
    game = []
    def __init__(self, game):
        self.game = game

    def _save_object(self, o):
        return o.__to_json__()

    def export_state(self, fileName = "currentState.json"):
        txt = serialize(self.game)
        with open(fileName, "w") as text_file:
            text_file.write(txt)