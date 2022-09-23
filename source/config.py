# -*- coding: utf-8 -*-

TOKEN = 'TOKEN'
GROUP_ID = 'GROUP_ID'

START_ANSWER = 'Привет, чем я могу вам помочь?'

DEBUG_ANSWER = 'Простите я не знаю как вам помочь с этим, я могу ' \
               'предоставить вам наш католог товаров, если вам это интересно.' \
               'Просто скажите мне "Привет".'

END_ANSWER = 'Всего вам наилучшего!\n' \
             'Если я вам еще потребуюсь пишите!\n' \
             'Буду рад помочь!\n'

CONTACT_INFORMATION = 'Мы:    ООО "ПЛЮШКИ"   \n' \
                      'наш сайт:  example.com  \n' \
                      'ИНН:       0000000000000\n' \
                      'ОГРН:      0000000000000\n' \
                      '\n' \
                      'Телефон:+7(000)000-00-00\n'

START_EVENT = ['Каталог', 'Статус Заказа', 'Корзина', 'exit']
EXIT_EVENT = ['exit', 'end', 'by', 'Пока']
CATALOG_EVENT = ['Назад', 'Купить', 'Далее', 'Меню', 'Корзина']
REQUESTS = [
    {
        "name": "Каталог",
        "tokens": ("Купить", "купить", "Каталог", "каталог", "Заказ", "заказ"),
        "scenario": "catalog",
        "answer": None
    },
    {
        "name": "Корзина",
        "tokens": ("корзина", "Корзина"),
        "scenario": "shopping_basket",
        "answer": None
    },
    {
        "name": "Статус заказа",
        "tokens": ("Где мой з", "где мой з", "Где мой З", "где мой З", "Статус", "статус"),
        "scenario": "order_status",
        "answer": "Вы уверены что заказывали у нас что то?"
    },
    {
        "name": "Контакты",
        "tokens": ("Контакты", "контакты", "calls", "call",
                   "Справочник", "справочник", "инфо", "Инфо",
                   "телефон", "Телефон", "FAQ", "faq", "ИНН", "инн"),
        "scenario": None,
        "answer": CONTACT_INFORMATION
    },
    {
        "name": "Привет",
        "tokens": ("привет", "Привет", "Здарова", "хай", "start", "hi", "hello", "Hi", "Hello"),
        "scenario": None,
        "answer": START_ANSWER
    }
]
SCENARIOS = {
    "shopping_basket": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "",
                "err_val": "",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "",
                "err_val": "",
                "handler": "handle_email",
                "next_step": "step3"
            },
        }
    },

    "catalog": {
        "first_step": "catalog_menu",
        "steps": {
            "catalog_menu": {
                "text": "Выберите категорию",
                "err_val": "Я ничего не нашел, возможно добавим немного позже..",
                "table": "category_table",
                "line": 1
            },
            "step2": {
                "text": "",
                "err_val": "",
                "handler": "",
                "next_step": "step3"
            },
        }
    },

    "order_status": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "",
                "err_val": "",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "",
                "err_val": "",
                "handler": "",
                "next_step": "step3"
            },
        }
    }
}

#
# RW = {"catalog": {
#     "first_step": "catalog_menu", "steps": {
#         "catalog_menu": {
#             "text": "Выберите категорию",
#             "err_val": "Я ничего не нашел, возможно добавим немного позже..",
#             "keyboard": "catalog"
#         },
#         "step2": {
#             "text": "",
#             "err_val": "",
#             "handler": "",
#             "next_step": ""
#             },
#         }
#     },
# }
#
#
# scnr = RW['catalog']
# first_step = scnr['first_step']
# step = scnr['steps'][first_step]
#
# keyboard = step['keyboard']
# text_to_send = step['text']
# print(text_to_send, keyboard)
