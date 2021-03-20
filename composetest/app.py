import time

import redis #memmory
from flask import Flask

app = Flask(__name__) 
cache = redis.Redis(host='redis', port=6379) 

def get_hit_count(): #จำจำนวนครั้งที่เข้ามา
    retries = 5
    while True: #พยายามเชื่อมต่อซำ้
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello Nichaporn! I have been seen {} times.\n'.format(count)