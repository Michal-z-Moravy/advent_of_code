import requests


def get_input(day):
    try:
        f = open('2025\\input_day'+str(day), 'r')
    except:
        session = open('2025\\session', 'r').readline().replace('\n', '')
        resp = requests.get('https://adventofcode.com/2025/day/'+str(day)+'/input', cookies={
                            'session': session})
        f = open('2025\\input_day'+str(day), 'w')
        f.write(resp.text)
        f.close
        f = open('2025\\input_day'+str(day), 'r')
    return f.readlines()
