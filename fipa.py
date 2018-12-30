from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage

class Sender(Agent):
    def __init__(self,aid):
        super(Sender, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Sender Initialized')

    def on_start(self):
        display_message(self.aid.localname, 'Sending Message to receiver')
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('receiver'))
        message.set_content('Hi')
        self.send(message)

    def react(self, message):
        display_message(self.aid.localname, 'Received Message: ' + message)

class Receiver(Agent):
    def __init__(self,aid):
        super(Receiver, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Receiver Initialized')

    def react(self, message):
        display_message(self.aid.localname, 'Received Message: ' + message)

if __name__ == '__main__':
    agent_r = Receiver(AID(name="receiver"))
    agent_s = Sender(AID(name="sender"))

    start_loop([agent_r, agent_s])

    