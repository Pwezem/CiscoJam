# -*- coding: utf-8 -*-
import json
from handler_base import MessageHandler


class Vote(MessageHandler):
    def __init__(self, path_to_file="handlers/data_files/votes.json"):
        # load the json votes.
        self.path = path_to_file
        with open(self.path) as json_votes:
            self.data = json.load(json_votes)

    def handle_message(self, raw_msg, user_email, username):

        if "start_vote" in raw_msg.lower():
            # Starts a vote
            raw_msg = raw_msg.lower().replace("start_vote", "", 1)
            return self.start_vote(raw_msg)
        if "end_vote" in raw_msg.lower():
            return self.end_vote()
        if "vote" in raw_msg.lower():
            raw_msg = raw_msg.lower().replace("vote", "", 1)
            return self.vote(raw_msg, user_email)
        return False

    def help(self):
        return "**Vote** - the voting command:<br>" \
               "1. start_vote - Defaulted to \"yes\" or \"no\", adding choices, \"maybe, hell no, ok\".<br>" \
               "2. vote <choice> - vote for your choice, can only vot once.<br>" \
               "3. end_vote - tallies the votes and retruns the results."

    def write_json(self):
        with open(self.path, 'w') as output:
            json.dump(self.data, output)

    def start_vote(self, options):
        response = "**Starting Vote, options:**<br>"

        # Check there is no vote in progress
        if len(self.data["options"]) is not 0:
            return "Vote currently in progress!"
        # start a vote, check the options
        if len(options) == 0:
            # No options, go with default options
            # yes or no
            self.data["options"] = ["yes", "no"]
            self.write_json()
            return response + "Yes or No"

        opts = options.split(",")

        if len(opts) == 1:
            return "**Cancelling vote:**<br>There was only one option: %s" % options.strip()

        for option in opts:
            self.data["options"].append(option.strip())
            response += option.strip() + ", "

        self.write_json()
        return response[:-2]

    def vote(self, vote, user_email):
        vote = vote.strip()

        if vote is None or vote is "":
            return "**No Vote**<br>Please cast a vote!"
        if len(self.data["options"]) is 0:
            return "No vote in progress. Use start_vote to begin a vote"
        vote = str(vote)
        response = "Not a valid vote: \"%s\"" % vote
        if user_email in self.data:
            return "You have already voted."

        for opt in self.data["options"]:
            if opt.lower() == vote.lower().strip():
                self.data[user_email] = opt
                response = "Your vote has been logged."
                self.write_json()
                break

        return response

    def end_vote(self):
        response = "**Votes are in!**<br>"
        options = {}
        for opt in self.data["options"]:
            options[opt] = 0

        del self.data["options"]

        if not self.data:
            return "**No Votes Cast**<br>Ending vote."
        else:
            for name in self.data:
                for opt in options:
                    if self.data[name] == opt:
                        options[opt] += 1

            max = 0
            vote = ""
            for opt in options:
                response += "%s: %d<br>" % (opt, options[opt])
                if options[opt] > max:
                    max = options[opt]
                    vote = opt

            response += "**The winner is**<br>%s" % vote

        self.data = {"options": []}
        self.write_json()

        return response
