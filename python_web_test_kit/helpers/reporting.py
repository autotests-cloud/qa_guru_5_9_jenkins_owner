from allure import step as allure_step


def step(title):
    def decorator(fn):
        return allure_step(title)(fn)()

    return decorator
