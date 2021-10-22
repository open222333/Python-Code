-- https://github.com/scrapy-plugins/scrapy-splash/issues/106
function process_one(splash)
    local get_dimensions = splash:jsfunc([[
    function () {
          var allA = document.getElementsByTagName('a');
    	  for(var i=0;i<allA.length;i++){
    		if(allA[i].innerHTML=="\u4e0b\u4e00\u9875"){
    			var rect = allA[i].getClientRects()[0];
    			return {"x": rect.left, "y": rect.top};
  		}
 	}
    }
    ]])
    splash:set_viewport_full()
    splash:wait(0.1)
    local dimensions = get_dimensions()
    splash:mouse_click(dimensions.x, dimensions.y)
    splash:wait(5)
    local content = splash:html()
    return content
end

function process_mul(splash)
    local res = {}
    for i = 1, 3, 1 do res[i] = process_one(splash) end
    return res
end

function main(splash)
    assert(splash:go("http://was.mot.gov.cn:8080/govsearch/gov_list.jsp"))
    return {res = process_mul(splash)}
end
