# -*- coding: utf-8 -*-

TOKEN = 'c7465075b375a18026d0a4092b380a376f271ed121af807548ee0690a456f2d819a49a7e003c601723481'
GROUP_ID = '188414199'

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
EXIT_EVENT_ANSWER = ['exit', 'end', 'by', 'Пока']
REQUESTS = [
    {
        "name": "Каталог",
        "tokens": ("Купить", "купить", "Каталог", "каталог", "Заказ", "заказ"),
        "scenario": None,
        "answer": None
    },
    {
        "name": "Корзина",
        "tokens": ("корзина", "Корзина"),
        "scenario": "shopping_basket",
        "answer": "Вы ничего не выбрали :с"
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
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "",
                "err_val": "",
                "handler": "",
                "next_step": "step2"
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
