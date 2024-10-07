import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    new_warp = wrapper.wrap(text=string)
    return '\n'.join(new_warp) #from list you can directly join no need to loop
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)