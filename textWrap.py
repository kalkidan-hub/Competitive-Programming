import textwrap

def wrap(string, max_width):
    
    s, e = 0, max_width
    while e < len(string):
        print(string[s:e])
        s, e = e, e + max_width
    return string[s:]

def wrap2(string, max_width):
    res = ''
    wrapper = textwrap.TextWrapper(max_width)
    words = wrapper.wrap(string)
    for i in words:
        res += i + '\n'

        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)