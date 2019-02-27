# проверка безопасности пароля
# Вариант с регекспами:
import re


def check_psw(psw):
    return len(psw) >= 8 and
    bool(re.match("^.*[A-Z]+.*$", psw)
             and re.match("^.*[a-z]+.*$", psw)
         and re.match("^.*[0-9]+.*$", psw))


# или


def check_psw(psw):
    return bool(re.match("((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8})", psw))


# или


def check_psw(psw):
    if len(psw) < 8:
        return False
    for r in ('[a-z]', '[A-Z]', '\d'):
        if re.search(r, psw) is None:
            return False
    return True


# стрип-функция
def strip_custom(x=" ", text):
    return re.search(' *[{s}]*(.*?)[{s}]* *$'.format(s=x), text).group(1)


split_custom('abc', ' aaabtestbcaa ')
