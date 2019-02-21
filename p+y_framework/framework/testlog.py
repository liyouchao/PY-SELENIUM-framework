from framework.logger import Logger

log = Logger(logger='log').getlog()
print(log.info('cesi'))

input_box = "id=>kw"
search_submit_bth = "xpath=>//*[@id='su']"
a = input_box.split('=>')[0]
b = input_box.split('=>')[1]
print(a)
print(b)