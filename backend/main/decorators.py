
def check_auth(func):
    # Аннотирует все необходимые поля
    def check_field(*arg, **kwargs):
        current_user = arg[1].context.user
        print(current_user.is_authenticated)
        if current_user.is_authenticated:
            return func(*arg, **kwargs)
        else:
            Exception("You are not auth")
    return check_field

