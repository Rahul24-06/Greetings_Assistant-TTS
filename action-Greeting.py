#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import random

# say = ['bye', 'see you later', 'good bye', 'bye now']
# result_sentence = random.choice(say)
# current_session_id = intentMessage.session_id
# hermes.publish_end_session(current_session_id, result_sentence)

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = ''

    if intent_message.intent.intent_name == 'SirBuildsALot7:hello':
        print('hi sir')
        sentence += 'hi sir'
    elif intent_message.intent.intent_name == 'SirBuildsALot7:bye':
        print('bye master')
        sentence += 'bye master'
    else:
        return

    hi_slot = intent_message.slots.hello.first()
    bye_slot = intent_message.slots.bye.first()
    

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
