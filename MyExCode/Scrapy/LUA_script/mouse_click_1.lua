function main(splash)
    -- ...
    local element = splash:select('.element')
    local bounds = element:bounds()
    assert(element:mouse_click{x = bounds.width / 3, y = bounds.height / 3})
    -- ...
end
