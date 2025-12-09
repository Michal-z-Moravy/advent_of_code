import requests


def get_input(year, day):
    try:
        f = open(f'{year}\\input_day{day}', 'r')
    except:
        session = open(f'{year}\\session', 'r').readline().replace('\n', '')
        resp = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={
                            'session': session})
        f = open(f'{year}\\input_day{day}', 'w')
        f.write(resp.text)
        f.close
        f = open(f'{year}\\input_day{day}', 'r')
    return f.readlines()
