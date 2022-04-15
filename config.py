GROUP_ID = 212216280

KEYBOARD = {}

TOKEN = "67551833ab9353f9013192edf4394ade976f874adddfc5a3a0a87b08005df6ea3235b09390c2714f26fdd"

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

PRETTY_MESSAGES = ['Красавчики всех стран объединяйтесь!', 'Анализирую красоту по размеру члену/глубине вагины', 'Красавчик сегодня - @id{}({} {})']

COMMAND = {
    '{"button":"1"}': (PIDOR_MESSAGES, 'last_call_pid'), 
    '{"button":"2"}': (PRETTY_MESSAGES, 'last_call_pretty'),
    '{"button":"3"}': None,
    '{"button":"4"}': None
}
