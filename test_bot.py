# -*- coding: utf-8 -*-

import os
import unittest
from bot import VkBot
import vk_api.bot_longpoll
from unittest import TestCase
from unittest.mock import patch, Mock, ANY


def base_check():
    try:
        os.path.isfile('base.db')
    except Exception as err:
        print("ERROR SQL:", err)


class TestBotCase(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {
            'message': {'date': 1636595114, 'from_id': 517870328, 'id': 175, 'out': 0, 'peer_id': 517870328,
                        'text': 'adas', 'attachments': [], 'conversation_message_id': 173, 'fwd_messages': [],
                        'important': False, 'is_hidden': False, 'random_id': 0},
            'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link',
                                               'callback', 'intent_subscribe', 'intent_unsubscribe'],
                            'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}
        },
        'group_id': 188414199,
        'event_id': 'f0080c97909467dc1576bba2f3407b2d75932855'}

    def run_test(self):
        pass


if __name__ == '__main__':
    base_check()
