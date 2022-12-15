import httpx

def get_url_with_http2(url):
    # 連接池保持連線與最大連線數
    limits = httpx.Limits(max_keepalive_connections=50, max_connections=100)
    # 重試次數
    transport = httpx.HTTPTransport(retries=3)
    httpx_client = httpx.Client(http2=True, limits=limits, transport=transport)
    r = httpx_client.get(url,timeout=1, headers={'Connection': 'close'})
    return r.http_version
