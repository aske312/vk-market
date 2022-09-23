# -*- coding: utf-8 -*-

import vk_api
import platform
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from source.config import *
from source.sql_db import * # select, conn
from logs.change import log, config_logging


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
        self.user_session = dict()
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        log.info(f'Running VkBot by: {platform.system()} in date: {datetime.now()}')

    def buttons(self, item_list, line=5, loc=False, vk_pay=False):
        # print('buttons')

        def generate(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i+n]

        keyboard = VkKeyboard(one_time=True)
        check = 0
        for items in generate(item_list, line):
            for item in items:
                if item == 'exit':
                    keyboard.add_button(str(item), color=VkKeyboardColor.NEGATIVE)
                else:
                    keyboard.add_button(str(item), color=VkKeyboardColor.SECONDARY)
                    check = check + 1
            if len(item_list) != check:
                keyboard.add_line()
        if loc:
            keyboard.add_location_button()
        if vk_pay:
            keyboard.add_vkpay_button(hash="#")
        log.info(f'Activates button keyboard with {len(item_list)} positionsin')
        return keyboard.get_keyboard()

    def send_messages(self, message):
        # print('send_msg')
        if message['keyboard']:
            self.vk.messages.send(
                keyboard=self.buttons(message['keyboard'], message['line']),
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
        log.info(f'Sends message is user')

    def on_event(self, event):
        if event.type != VkBotEventType.MESSAGE_NEW:
            return
        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        log.info(f'NEW MESSAGE BY USER: {user_id}')
        send_by_user = {
            'keyboard': None,
            'message': None,
            'user_id': user_id
        }
        if user_id in self.user_session:
            print('user_id array')
            # send_by_user = 'error'  # continue_session
            send_by_user['message'] = 'error'
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

    # def continue_session(self, user_id, text):
    #     session = self.user_session[user_id]
    #     steps = SCENARIOS[session.scenario_name]['steps']
    #     step = steps[session.step_name]
    #     # handler = getattr(hand_func, step['handler'])
    #     # if handler(text=text, context=state.context):
    #     #     next_step = steps[step['next_step']]
    #     #     text_to_send = next_step['text'].format(**state.context)
    #     #     if next_step['next_step']:
    #     #         state.step_name = step['next_step']
    #     #     else:
    #     #         self.user_states.pop(user_id)
    #     #         log.info('Зарегистрирован: {name}: {email}.'.format(**state.context))
    #     # else:
    #     #     text_to_send = step['failure_text'].format(**state.context)
    #     # return text_to_send

    def start_session(self, user_id, scenario):
        log.info(f'Used by {scenario} scenario, active.')
        text_to_send = {}
        scenario = SCENARIOS[scenario]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        if step['table']:
            key = select(table=str(step['table']))
            mras = []
            for item in key:
                mras.append(item[1])
            text_to_send['line'] = step['line']
            text_to_send['keyboard'] = mras
        text_to_send['user_id'] = user_id
        text_to_send['message'] = step['text']
        self.user_session[user_id] = UserSession(scenario=scenario, step=first_step)
        return text_to_send

    def run(self):
        for event in self.longpoll.listen():
            try:
                self.on_event(event)
            except Exception as err:
                print(f'Error value {err}')


if __name__ == '__main__':
    config_logging()
    bot = VkBot(token=TOKEN, group=GROUP_ID)
    bot.run()
    conn.close()
