import scrapy
from scrapy_splash import SplashRequest

# https://stackoverflow.com/questions/46925968/how-to-send-a-post-request-with-splashrequest-in-scrapy-splash
'''使用SplashRequest發送post請求'''


class SplashPostSpider(scrapy.Spider):
    name = "splash_post"
    http_proxy = 'http://proxy.example.com:1111' # 範例 無效的鏈結

    lua_script = """
    function main(splash, args)
      assert(splash:go{
        splash.args.url,
        http_method=splash.args.http_method,
        body=splash.args.body,
      })
      assert(splash:wait(0.5))
      return {
        html = splash:html(),
      }
    end
    """
    # has_proxy = {'wait': self.wait_sec, 'splash_headers': self.header}
    def start_requests(self):
        post_url = 'https://httpbin.org/post'
        post_data = 'foo=bar'
        yield SplashRequest(post_url, self.parse, endpoint='execute',
                            magic_response=True, meta={'handle_httpstatus_all': True},
                            args={'lua_source': self.lua_script, 'http_method': 'POST', 'body': post_data, 'proxy':self.http_proxy})

    def parse(self, response):
        with open('test.txt', 'a') as f:
            f.write(bytes(response.body).decode('utf-8'))
