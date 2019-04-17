#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = ''

    if intent_message.intent.intent_name == 'hi':
        print('hi sir')
        sentence += 'hi sir'
    elif intent_message.intent.intent_name == 'bye':
        print('bye master')
        sentence += 'bye master'
    else:
        return

    hi_slot = intent_message.slots.hi.first()
    bye_slot = intent_message.slots.bye.first()
    

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
