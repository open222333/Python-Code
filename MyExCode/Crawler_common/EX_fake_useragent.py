from fake_useragent import FakeUserAgent


def get_chrome_useragent():
    '''虛構 user_agent'''
    user_agent = FakeUserAgent()
    # chrome
    return user_agent.google


def get_random_useragent():
    '''取得隨機 useragent'''
    user_agent = FakeUserAgent()
    return user_agent.random
