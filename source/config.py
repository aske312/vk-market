# -*- coding: utf-8 -*-

from source.sql_db import *     # select, conn

TOKEN = 'TOKEN' # token del
GROUP_ID = 'GROUP_ID'

START_ANSWER = 'Привет, чем я могу вам помочь?'
DEBUG_ANSWER = 'Я не смог разобать что вы сказали, вот что я умею:'

CONTACT_INFORMATION = 'Мы:    ООО "ПЛЮШКИ"   \n' \
                      'наш сайт:  example.com  \n' \
                      'ИНН:       0000000000000\n' \
                      'ОГРН:      0000000000000\n' \
                      '\n' \
                      'Телефон:+7(000)000-00-00\n'

START_EVENT = ['Каталог Товаров', 'Статус Заказа', 'Корзина', 'Контакты']
CATALOG_EVENT = ['Назад', 'Купить', 'Далее', 'Меню', 'Корзина']

REQUESTS = [
    {
        "name": "Каталог",
        "tokens": ("Купить", "купить", "Каталог", "каталог"),
        "scenario": "catalog_menu",
        "answer": None
    },
    {
        "name": "Корзина",
        "tokens": ("корзина", "Корзина"),
        "scenario": "basket",
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
        "scenario": "main_menu",
        "answer": START_ANSWER
    }
]
QUEST_SHOP = [
    # {
    #     "name": "Купить",
    #     "tokens": "Купить",
    #     "scenario": "by",
    #     "answer": None
    # },
    {
        "name": "Назад",
        "tokens": "Назад",
        "scenario": "back",
        "answer": None
    },
    {
        "name": "Далее",
        "tokens": "Далее",
        "scenario": "farther",
        "answer": None
    },
    {
        "name": "Меню",
        "tokens": "Меню",
        "scenario": "catalog_menu",
        "answer": None
    },
    # {
    #     "name": "Корзина",
    #     "tokens": "Корзина",
    #     "scenario": "basket",
    #     "answer": None
    # }
]

SCENARIOS = {
    "main_menu": {
        "text": START_ANSWER,
        "err_val": "Я ничего не нашел, возможно добавим немного позже..",
        "name": "main_menu",
        "sql_table": None,
        "sql_line": None,
        "table": START_EVENT,
        "line": 1,
        "step": 0
    },
    "basket": {},
    "catalog_menu": {
        "text": "Выберите категорию",
        "err_val": "Я ничего не нашел, возможно добавим немного позже..",
        "name": "catalog_menu",
        "sql_table": "category_table",
        "sql_line": "name",
        "table": None,
        "line": 1,
        "step": 1,
        "navigation": {
            "name": "navigation",
            "back": {
                "name": 'back',
                "step": -1
            },
            "farther": {
                "name": 'farther',
                "step": +1
            },
            "catalog_menu": {
                "name": 'catalog',
                "step": 0
            },
        },
    },
    "status": {},

}
