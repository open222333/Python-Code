import scrapy
from scrapy_splash import SplashRequest

# https://stackoverflow.com/questions/46925968/how-to-send-a-post-request-with-splashrequest-in-scrapy-splash
'''使用SplashRequest發送post請求'''


class SplashPostSpider(scrapy.Spider):
    name = "splash_post"

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

    def start_requests(self):
        post_url = 'https://httpbin.org/post'
        post_data = 'foo=bar'
        yield SplashRequest(post_url, self.parse, endpoint='execute',
                            magic_response=True, meta={'handle_httpstatus_all': True},
                            args={'lua_source': self.lua_script, 'http_method': 'POST', 'body': post_data})

    def parse(self, response):
        print(response.body)
