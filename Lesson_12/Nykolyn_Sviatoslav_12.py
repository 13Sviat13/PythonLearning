import re

# task1
def text_match(text):
    pattern = '^[a-zA-Z0-9_]*$'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched'


print(text_match("Baby aweraf awrwff 1."))
print(text_match('ab Cdbs'))
print(text_match("1 2 32"))
print(text_match("afd_a_sfa21312AFSFA_"))
print(text_match("_ _"))

# task2


def find_urls(text):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return urls

print(f"Your web site is {find_urls('https://www.debuggex.com/')}")


# task3
def replace(text):
    print(re.sub(r'\(.*?\)', '', text))


replace("example (.com)")
replace("github (.com)")
replace("stackoverflow (.com)")


# task4
def replace2(text):
    print(re.sub(r'([A-Z)])', r' \1', text))

replace2("AwadAkedawAra")