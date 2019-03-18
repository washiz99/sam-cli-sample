
class RingCommand:

    def __init__(self, config):
        self.status = int(config['status'])
        self.commands = config['commands']

    def turn_next(self):
        if self.status == len(self.commands):
            self.status = 1
        else:
            self.status = self.status + 1
        return self.status

    def turn_prev(self):
        if self.status == 1:
            self.status = len(self.commands)
        else:
            self.status = self.status - 1
        return self.status

    def get_command(self):
        return self.commands[self.status - 1]['lambda']

    def to_json(self):
        config_json = {
                'status': self.status,
                'commands': self.commands
                }
        return config_json
