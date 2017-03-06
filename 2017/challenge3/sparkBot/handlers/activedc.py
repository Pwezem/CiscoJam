from handler_base import MessageHandler
import urllib2
import ast

class ActiveDC(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg):
        if raw_msg == "dcs":
            return self.get_active_dcs()
        return False

    def help(self):
        return "dcs - Return ative and inactive DCs"

    @staticmethod
    def get_active_dcs():
        response = ast.literal_eval(urllib2.urlopen(" http://teamgold.cisco.com/datacenter/dclist").read())
        if response:
            response_string = "Active Production = " + response['active-production-dc'] \
                            + "<br>Active Integration = " + response['active-integration-dc'] \
                            + "<br>Standby Production = " + response['standby-production-dc'] \
                            + "<br>Standby Integration = " + response['standby-integration-dc'] \
                            + "<br>Active EU Production = " + response['active-eu-production-dc']
        else:
            response_string = "Error getting DCs, probably a problem with the Auto Infra API"
        return response_string

