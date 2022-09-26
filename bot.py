# -*- coding: utf-8 -*-

import vk_api
import platform
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from source.config import *
from logs.change import log, config_logging


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
        self.shop_basket = dict()
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        log.info(f'Running VkBot by: {platform.system()} in date: {datetime.now()}')

    def buttons(self, item_list, line=5, loc=False, vk_pay=False):
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

    def keyboard_panel(self, scenario):
        response = {}
        if scenario['table']:
            response['keyboard'] = scenario['table']
        else:
            result = []
            for point in select(table=scenario['sql_table'],
                                line=scenario['sql_line']):
                result.append(point[0])
            response['keyboard'] = result
        response['line'] = scenario['line']
        return response

    def scenario(self, user_id, request):
        result = {}
        if request['scenario']:
            scenario = SCENARIOS[request['scenario']]
            result['message'] = scenario['text']
            result.update(self.keyboard_panel(scenario))
            # self.user_session[user_id] = {}
            self.user_session[user_id] = {
                "step": 0,
                "index": [],
                "scenario": scenario,
                "next_step": True
            }
        else:
            result['message'] = request['answer']
        return result

    def shoping_function(self, user_id, request):
        result = {}
        session = self.user_session[user_id]
        print(self.user_session[user_id]['next_step'])
        if self.user_session[user_id]['next_step'] == 'GOTO_MENU':
            self.user_session[user_id]['next_step'] = True
            response = self.keyboard_panel(SCENARIOS['catalog_menu'])
            result['message'] = SCENARIOS['catalog_menu']['text']
            result['keyboard'] = response['keyboard']
            result['line'] = response['line']
            return result
        if self.user_session[user_id]['next_step']:
            items = select(sql=f"SELECT * FROM category_table,items_table "
                               f"WHERE category_table.id = category_id "
                               f"AND category_table.name = '{request}'")
            context = [item for item in items]
            session['step'] = 0
            session["index"] = context
        message = session['index'][session['step']]
        result['message'] = f'{message[3]}\n\n {message[4]}\n\n Цена за порцию: {message[5]}р.'
        self.user_session[user_id].update(session)
        return result

    def navigation(self, text, session, user_id):
        step = 0
        for request in QUEST_SHOP:
            if any(token in text for token in request['tokens']):
                if request['name'] == 'Меню':
                    self.user_session[user_id]['next_step'] = 'GOTO_MENU'
                    break
                if request['name'] == text:
                    self.user_session[user_id]['next_step'] = None
                    scence = session['scenario']['navigation']
                    move = request['scenario']
                    step = scence[move]['step']
                    break
        index = self.user_session[user_id]['index']
        if step < 0:
            new_step = self.user_session[user_id]['step'] - step
            self.user_session[user_id]['step'] = new_step
        else:
            self.user_session[user_id]['step'] = self.user_session[user_id]['step'] + step
        if self.user_session[user_id]['step'] >= len(index):
            self.user_session[user_id]['step'] = 0

    def new_event(self, event):
        if event.type != VkBotEventType.MESSAGE_NEW:
            return
        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        response_to_user = {
            'user_id': user_id,
            'keyboard': None,
            'message': None,
            'line': 1
        }
        log.info(f'new event by user: {user_id} say: {text}')
        response_to_user['keyboard'] = START_EVENT
        if user_id in self.user_session:
            if len(self.user_session[user_id]['index']) > 0:
                session = self.user_session[user_id]
                self.navigation(text, session, user_id)
            response_to_user['line'] = 3
            response_to_user['keyboard'] = CATALOG_EVENT
            response_to_user.update(self.shoping_function(user_id, text))
        else:
            for request in REQUESTS:
                if any(token in text for token in request['tokens']):
                    response_to_user.update(self.scenario(user_id, request))
                    break
            else:
                response_to_user['message'] = DEBUG_ANSWER
        self.send_messages(response_to_user)

    def run(self):
        for event in self.longpoll.listen():
            try:
                self.new_event(event)
            except Exception as err:
                print(f'Error value {err}')


if __name__ == '__main__':
    config_logging()
    bot = VkBot(token=TOKEN, group=GROUP_ID)
    bot.run()
    conn.close()
