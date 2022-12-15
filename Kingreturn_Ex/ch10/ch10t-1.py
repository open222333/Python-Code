string = '''Silicon Stone Education is an unbiased organization, concentrated on bridging the gap between academic and the working world in order to benefit society as a whole. We have carefully crafted our online certification system and test content databases. The content for each topic is created by experts and is all carefully designed with a comprehensive knowledge to greatly benefit all candidates who participate.'''
string = string.lower()
for ch in string:
    if ch in '.,':
        string = string.replace(ch, '')
string_list = string.split()
string_set = set(string_list)
print(string_set)
