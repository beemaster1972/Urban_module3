import re
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.ru|\.net|\.com)$"
    condition = [re.match(pattern,recipient),re.match(pattern,sender)]
    if not all(condition):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return False
    elif recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
        return False
    elif sender is send_email.__defaults__[0]:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return True
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return True


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
