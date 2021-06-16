from allure import step as Step


def step(title):
    def decorator(fn):
        fn_with_logging_to_allure = Step(fn)
        fn_with_logging_to_allure()
    return decorator