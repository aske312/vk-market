# -*- coding: utf-8 -*-

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from source.config import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class UserSession:
    def __init__(self, scenario, step, context=None):
        self.scenario = scenario
        self.step = step
        self.context = context or {}


class VkBot:
    """
    """
    def __init__(self, group, token):
        """
        :param group: group id vk club
        :param token: token by bot vk_api
        """
        self.group_id = group
        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        self.user_session = dict()

    def _event_buttons(self, scenario, loc=False, vk_pay=False):
        keyboard = VkKeyboard(one_time=True)
        new_line = 1
        for even in scenario:
            if even == 'exit':
                keyboard.add_button(even, color=VkKeyboardColor.NEGATIVE)
            else:
                keyboard.add_button(even, color=VkKeyboardColor.SECONDARY)
            if int((scenario.index(even) + 1) // vk_api.keyboard.MAX_BUTTONS_ON_LINE + 1) > new_line:
                keyboard.add_line()
                new_line = new_line + 1
        if loc:
            keyboard.add_location_button()
        if vk_pay:
            keyboard.add_vkpay_button(hash="#")
        return keyboard.get_keyboard()

    def send_messages(self, message):
        if message['keyboard']:
            self.vk.messages.send(
                keyboard=str(message['keyboard']),
                peer_id=int(message['user_id']),
                message=str(message['message']),
                random_id=0
            )
        else:
            self.vk.messages.send(
                peer_id=int(message['user_id']),
                message=str(message['message']),
                random_id=0
            )

    def on_event(self, event):
        if event.type != VkBotEventType.MESSAGE_NEW:
            print('INT: NEW_EVENT')
            return
        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        send_by_user = {
            'keyboard': None,
            'message': None,
            'user_id': user_id
        }
        if user_id in self.user_session:
            send_by_user = ''  # continue_session
        else:
            for req in REQUESTS:
                if any(token in text for token in req['tokens']):
                    if req['answer']:
                        send_by_user['message'] = req['answer']
                    else:
                        send_by_user = self.start_session(user_id, req['scenario'])
                    break
            else:
                send_by_user['message'] = DEBUG_ANSWER
        self.send_messages(send_by_user)

    def continue_session(self):
        pass

    def start_session(self, user_id, scenario):
        scenario = SCENARIOS[scenario]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_session[user_id] = UserSession(scenario=scenario, step=first_step)
        return text_to_send

    def run(self):
        for event in self.longpoll.listen():
            try:
                self.on_event(event)
            except Exception as err:
                print(f'Error value {err}')


if __name__ == '__main__':
    bot = VkBot(token=TOKEN, group=GROUP_ID)
    bot.run()
