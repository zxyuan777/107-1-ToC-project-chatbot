from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_pop(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to pop'
        return False

    def is_going_to_jazz(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to jazz'
        return False
    
    def is_going_to_edm(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to edm'
        return False

    def is_going_to_poprock(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to pop rock'
        return False

    def is_going_to_dancepop(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to dance pop'
        return False
    
    def is_going_to_house(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to house'
        return False

    def is_going_to_trance(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to trance'
        return False

    def is_going_to_dubstep(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to dubstep'
        return False

    def is_going_to_bigroom(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to bigroom'
        return False

    def is_going_to_progressive(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to progressive'
        return False

    def is_going_to_future(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to future'
        return False









    def on_enter_pop(self, event):
        print("I'm entering pop")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering pop")
        self.go_back()

    def on_exit_pop(self):
        print('Leaving pop')

    def on_enter_jazz(self, event):
        print("I'm entering jazz")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering jazz")
        self.go_back()

    def on_exit_jazz(self):
        print('Leaving jazz')

    def on_enter_edm(self, event):
        print("I'm entering edm")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering edm")
        self.go_back()

    def on_exit_edm(self):
        print('Leaving edm')

    def on_enter_poprock(self, event):
        print("I'm entering poprock")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering poprock")
        self.go_back()

    def on_exit_poprock(self):
        print('Leaving poprock')

    def on_enter_dancepop(self, event):
        print("I'm entering dancepop")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering dancepop")
        self.go_back()

    def on_exit_dancepop(self):
        print('Leaving dancepop')

    def on_enter_house(self, event):
        print("I'm entering house")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering house")
        self.go_back()

    def on_exit_house(self):
        print('Leaving house')

    def on_enter_trance(self, event):
        print("I'm entering trance")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering trance")
        self.go_back()

    def on_exit_trance(self):
        print('Leaving trance')

    def on_enter_dubstep(self, event):
        print("I'm entering dubstep")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering dubstep")
        self.go_back()

    def on_exit_dubstep(self):
        print('Leaving dubstep')

    def on_enter_bigroom(self, event):
        print("I'm entering bigroom")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering bigroom")
        self.go_back()

    def on_exit_bigroom(self):
        print('Leaving bigroom')

    def on_enter_progressive(self, event):
        print("I'm entering progressive")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering progressive")
        self.go_back()

    def on_exit_progressive(self):
        print('Leaving progressive')

    def on_enter_future(self, event):
        print("I'm entering future")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering future")
        self.go_back()

    def on_exit_future(self):
        print('Leaving future')
