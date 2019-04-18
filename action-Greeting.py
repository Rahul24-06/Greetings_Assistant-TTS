#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

hi_choice = ['hello', 'howdy', 'hi', 'greetings']
bye_choice = ['bye', 'see you later', 'good bye', 'bye now']

def intent_received(hermes, intent_message):
        sentence = ''
        if intent_message.intent.intent_name == 'SirBuildsALot7:hello':
                say = random.choice(hi_choice)
                print(say)
        elif intent_message.intent.intent_name == 'SirBuildsALot7:bye':
                say = random.choice(bye_choice)
                print(say)
        else:
                return
        sentence += say + " Rahul"
#sentence += 'Rahul'
        hermes.publish_end_session(intent_message.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
        h.subscribe_intents(intent_received).start()
