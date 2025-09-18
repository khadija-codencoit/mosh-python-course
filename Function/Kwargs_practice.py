def save_user(**user):
    print(user)


save_user(id=7, name="khadija")
#Example


def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)


fun(s1='Python', s2='is', s3='Awesome')
