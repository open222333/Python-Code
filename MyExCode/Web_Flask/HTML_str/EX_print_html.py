'''網頁寫法範例'''


def li_sample():
    temp_id = 'sample'
    temp_name = 'li_sample'
    temp_role = 'presentation'

    lis = ''
    active = 'class="active"'

    lis += f'<li id="li_{temp_id}" role="{temp_role}" {active}>'
    lis += f'<a href="javascript:go_("{temp_name}");void(0);">'
    lis += '列表'
    lis += f'<span id="tab_{temp_name}" class="badge"></span></a></li>'
    return lis
