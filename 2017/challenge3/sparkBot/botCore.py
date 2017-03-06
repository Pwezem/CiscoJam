import importlib

from spark2d2.bot import Bot

handler_modules = ['repeater.Repeater', 'futurama.Futurama', 'eightball.Eightball', 'shutdown.ShutDown',
                   'vote.Vote']


class botCore(Bot):

    def __init__(self, bot_token):
        self.len_handlers = len(handler_modules)
        self.bot_token = bot_token
        self.list_of_handlers = []
        self.responses = []
        self.response_string = " "

        for handler_name in handler_modules:
            handler = handler_name.split('.')
            handler_module = importlib.import_module('handlers.' + handler[0])
            handler_class = getattr(handler_module, handler[1])
            print('Registering handler %s' % format(str(handler_class)))
            self.list_of_handlers.append(handler_class())

        Bot.__init__(self, bot_token, encryption=True, events=True)

    def process_message(self, raw_msg, user_email=None):
        if "help" in raw_msg:
            for handler in self.list_of_handlers:
                self.responses.append(handler.help())
        else:
            for handler in self.list_of_handlers:
                self.responses.append(handler.handle_message(raw_msg, user_email))
        return_value = self.responses
        self.responses = []
        return return_value


