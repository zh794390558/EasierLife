#coding=utf8
import sys, os
import requests, json

try:
    with open('tuling.json') as f: key = json.loads(f.read())['key']
except:
    key = '' # if key is '', get_response will return None
    # raise Exception('There is something wrong with the format of you plugin/config/tuling.json')

def get_response(msg, storageClass = None, userName = None, userid = 'ItChat'):
    url = 'http://www.tuling123.com/openapi/api'
    if isinstance(msg, str):
        msg = msg.decode('utf-8')
        print(type(msg))

    payloads = {
        'key': key,
        'info': msg,
        'userid': userid,
    }
    try:
        #r = requests.post(url, data = json.dumps(payloads)).json()
        r = requests.post(url, data = payloads).json()
    except:
        return

    print(type(r))

    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000): return
    if r['code'] == 100000: # tuling.py

        #return '\n'.join([r['text'].replace('<br>','\n')])
        return r.get('text').encode('utf-8')

    elif r['code'] == 200000: # tuling.py
        return '\n'.join([r['text'].replace('<br>','\n'), r['url']])
    elif r['code'] == 302000: # tuling.py
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['article'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 308000: # tuling.py
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['name'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 313000: # tuling.py
        return '\n'.join([r['text'].replace('<br>','\n')])
    elif r['code'] == 314000: # tuling.py
        return '\n'.join([r['text'].replace('<br>','\n')])

if __name__ == '__main__':
    try:
        ipt = raw_input
        #ipt = lambda: raw_input('>').decode(sys.stdin.encoding)
    except:
        ipt = lambda: input('>')
    while True:
        a = ipt()
        print(a)
        print(type(a))
        print(get_response(a, 'ItChat'))
