from handler_base import MessageHandler
import os
import random

class Eightball(MessageHandler):     
    
    def __init__(self):         
        pass      
    
    def handle_message(self, raw_msg, user_email):
        if raw_msg == "eightball":
            predictions_file = os.path.join(os.path.dirname(__file__), 'text_files/eightball_predictions.txt')             
            return self.get_prediction(predictions_file)         
        return False

    def get_prediction(self, filename):
        with open(filename, "r") as file:
            predictions = file.read().splitlines()
            prediction = predictions[random.randint(0, len(predictions) - 1)]
            return prediction

    def help(self):
        return "eightball - Get a prediction"
