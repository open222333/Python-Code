import scrapy
from scrapy_splash import SplashRequest

# https://stackoverflow.com/questions/46925968/how-to-send-a-post-request-with-splashrequest-in-scrapy-splash
'''使用SplashRequest發送post請求
使用說明'''


class SplashPostSpider(scrapy.Spider):
    name = "splash_post"
    proxy = {
        'http': 'http://proxy.example.com:1111',
        'https': 'http://proxy.example.com:1111'
    }  # 範例 無效的鏈結

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

    args = {
        # lua腳本
        'lua_source': lua_script,
        'http_method': 'POST',
        # 使用proxy
        'proxy': proxy,
        # 設置最長等待時間 預設60
        'timeout': 3600,
        # 超時後中止資源加載
        'resource_timeout': 20
    }
    # has_proxy = {'wait': self.wait_sec, 'splash_headers': self.header}

    def start_requests(self):
        post_url = 'https://httpbin.org/post'
        self.args['body'] = 'foo=bar'
        yield SplashRequest(
            post_url,
            self.parse,
            endpoint='execute',
            magic_response=True,
            meta={'handle_httpstatus_all': True},
            args=self.args
        )

    def parse(self, response):
        with open('test.txt', 'a') as f:
            f.write(bytes(response.body).decode('utf-8'))


Ｆ
