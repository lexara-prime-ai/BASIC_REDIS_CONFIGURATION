import redis

REDIS_URL = '<region>-redis.<provider>.com'

# ---------
# Alternatively, you can connect via docker:
# docker run --name some-redis -p 6379:6379 -d redis redis-server --save 60 1 --loglevel warning
# REDIS_URL = 'localhost'
#-----------

REDIS_INSTANCE = redis.Redis(host=REDIS_URL, username='red-user-xxxXXXxxxXXX', password='red-pwd-xxxXXXxxxXXX', db=0, ssl=True)

#-------------
# When working with the docker instance.
# REDIS_INSTANCE = redis.Redis(host=REDIS_URL)
#------------



def store_data():
    try:
        REDIS_INSTANCE.set('foo', 'bar')
    except Exception as e:
        print("ERROR: ", e)


def retrieve_data():
    try:
        print(REDIS_INSTANCE.get('foo'))
    except Exception as e:
        print("ERROR: ", e)


# Usage examples:
# store_data()
# retrieve_data()
