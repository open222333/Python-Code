from fake_useragent import FakeUserAgent


'''虛構 user_agent'''
user_agent = FakeUserAgent()
# chrome
print(user_agent.google)
