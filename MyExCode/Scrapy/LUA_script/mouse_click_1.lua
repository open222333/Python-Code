function main(splash)
    -- .element 是css選擇器 可以用右鍵 Copy selector 複製下來
    local element = splash:select_all('.div.big-button.play')
    local bounds = element:bounds()
    assert(element)
    -- assert(element:mouse_click{x = bounds.width / 3, y = bounds.height / 3})
    -- ...
end

function main(splash)
    -- ...
    local element = splash:select('.element')
    local bounds = element:bounds()
    assert(element:mouse_click{x = bounds.width / 3, y = bounds.height / 3})
    -- ...
end

function main(splash)
    local element = splash:select_all('.div.big-button.play')
    return element
end

function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(2))
    return {
      a = splash:select("div").node.outerHTML,
      html = splash:html(),
      png = splash:png(),
      har = splash:har(),
    }
  end
