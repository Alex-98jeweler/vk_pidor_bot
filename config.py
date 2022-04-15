GROUP_ID = "your group id. must be integer"

KEYBOARD = {}

TOKEN = "your token"

KEYBOARD = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "label": "Ищем пидра",
                "payload": "{\"button\": \"1\"}",
            },
            'color': 'positive'
        }, 
        {
            "action": {
                "type": "text",
                "label": "Ищем красавчика",
                "payload": "{\"button\": \"2\"}",
            },
            'color': 'negative'
        }
        ],
        [
        {
            "action": {
                "type": "text",
                "label": "Топ пидора",
                "payload": "{\"button\": \"3\"}",
            },
            'color': 'secondary'
        },
        {
            "action": {
                "type": "text",
                "label": "Топ красавчика",
                "payload": "{\"button\": \"4\"}",
            },
            'color': 'secondary'
        }
        ]
    ]
}



PIDOR_MESSAGES = ['Кто же тут долбиться в сраку?', 'Проверяю ширину очка каждого', 'Оу, да вам необходимо зашивать...', 'И сегодня пидор - @id{}({} {})']

PRETTY_MESSAGES = ['Красавчики всех стран объединяйтесь!', 'Анализирую красоту по размеру члена/глубине вагины', 'Красавчик сегодня - @id{}({} {})']

COMMAND_CHOICE = {
    '{"button":"1"}': (PIDOR_MESSAGES, 'last_call_pid', "Пидора", 'count_pid'), 
    '{"button":"2"}': (PRETTY_MESSAGES, 'last_call_pretty', "Красавчика", 'count_pretty'),
}

COMMAND_TOP = {
    '{"button":"3"}': ('Топ Пидора:\n', 4),
    '{"button":"4"}': ("Топ Красавчика:\n", 5)
}
