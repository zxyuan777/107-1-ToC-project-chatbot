from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "Your Webhook Verify Token"
machine = TocMachine(
    states=[
        'user',
        'pop',
        'poprock',
        'dancepop'
        'jazz',
        'edm',
        'house',
        'bigroom',
        'progressive',
        'future',
        'trace',
        'dubstep'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'pop',
            'conditions': 'is_going_to_pop'
        },
        {
            'trigger': 'advance',
            'source': 'pop',
            'dest': 'poprock',
            'conditions': 'is_going_to_poprock'
        },
        {
            'trigger': 'advance',
            'source': 'pop',
            'dest': 'dancepop',
            'conditions': 'is_going_to_dancepop'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'jazz',
            'conditions': 'is_going_to_jazz'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'edm',
            'conditions': 'is_going_to_edm'
        },
        {
            'trigger': 'advance',
            'source': 'edm',
            'dest': 'house',
            'conditions': 'is_going_to_house'
        },
        {
            'trigger': 'advance',
            'source': 'edm',
            'dest': 'trance',
            'conditions': 'is_going_to_trance'
        },
        {
            'trigger': 'advance',
            'source': 'edm',
            'dest': 'dubstep',
            'conditions': 'is_going_to_dubstep'
        },
        {
            'trigger': 'advance',
            'source': 'house',
            'dest': 'bigroom',
            'conditions': 'is_going_to_bigroom'
        },
        {
            'trigger': 'advance',
            'source': 'house',
            'dest': 'progressive',
            'conditions': 'is_going_to_progressive'
        },
        {
            'trigger': 'advance',
            'source': 'house',
            'dest': 'future',
            'conditions': 'is_going_to_future'
        },
        {
            'trigger': 'go_back',
            'source': [
                'bigroom',
                'progressive',
                'future'
            ]
            'dest': 'house'
        },
        {
            'trigger': 'go_back',
            'source': [
                'house',
                'trance',
                'dubstep'
            ]
            'dest': 'edm'
        },
        {
            'trigger': 'go_back',
            'source': [
                'poprick',
                'dancepop'
            ]
            'dest': 'pop'
        },
        {
            'trigger': 'go_back',
            'source': [
                'pop',
                'jazz',
                'edm'
            ]
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
