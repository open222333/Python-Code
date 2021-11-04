import re



test = "html5player.setVideoUrlLow('https://test.com/dadawwwwww/231231/2321d2e3')"

pattern_high = re.compile(r"html5player.setVideoUrlHigh\(.*'")
pattern_low = re.compile(r"html5player.setVideoUrlLow\(.*'")
pattern_img = re.compile(r"html5player.setThumbUrl169\(.*'")
# 取出http
pattern_http = r"[a-zA-Z]+://.*"

pattern_http2 = r"html5player.setVideoUrlLow\('(.*?)'\)"
print(re.findall(pattern_http2, test))