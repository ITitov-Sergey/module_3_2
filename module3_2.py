def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" in recipient and recipient.endswith((".com", ".ru", ".net")) and
            "@" in sender and sender.endswith((".com", ".ru", ".net"))):
        if recipient != sender:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        else:
            print("Нельзя отправить письмо самому себе!")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email("Это сообщение для проверки связи", "sergey.student@gmail.net")
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")
