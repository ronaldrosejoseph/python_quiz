import time
import threading
import schedule

# cache is stored in a dictionary where key can be a combination of country code and other unique values
# values of the dictionary are stored in a list where v[0] is the value, v[1] is the position and v[2] is the time
cache = {}

# size of the cache be 4
size = 4

# time to retain a cache be 30 seconds
expiry = 30


# key, value pair is added to the cache, when adding same key the position changes to 1
# if a new element is added and the size if full then LRU item is deleted, all other elements position + 1
def add_cache(key, value):
    try:
        if cache[key]:
            for k, v in cache.items():
                if v[1] < cache[key][1]:
                    v[1] += 1
                else:
                    pass
            cache[key] = [value, 1, time.time()]

    except KeyError:
        temp = None
        for k, v in cache.items():
            if v[1] != size:
                v[1] += 1
            else:
                temp = k
        if temp:
            del cache[temp]
        cache[key] = [value, 1, time.time()]
    return cache


# adding caches with a delay of 10 seconds
print(add_cache('ca', 55))
time.sleep(10)
print(add_cache('in', 1))
time.sleep(10)
print(add_cache('us', 70))
time.sleep(10)
print(add_cache('uk', 110))
time.sleep(10)
print(add_cache('au', 50))
time.sleep(10)
print(add_cache('ca', 55))
time.sleep(10)


# return cache when cache has the key else return False
def get_cache(key):
    try:
        if cache[key]:
            for k, v in cache.items():
                if v[1] < cache[key][1]:
                    v[1] += 1
                else:
                    pass
            cache[key][1] = 1
            cache[key][2] = time.time()
            return cache[key]
    except KeyError:
        return False


# Get the cache of us and print cache
print("\nThe cache of us : ", get_cache('us'))
print(cache)


# clear the cache when it is expired
# TODO: Location based cache clearing
def cache_clearing():
    temp = []
    for k, v in cache.items():
        if (time.time() - v[2]) > expiry:
            temp.append(k)
    if temp:
        print("\n")
        for i in temp:
            print("Time expired for: ", i, cache[i])
            del cache[i]
        print("New cache: ", cache)


# schedule cache clearing every 6th second
# TODO: change scheduled interval to be that of LRU cache expiry time
def scheduler():
    schedule.every(0.1).minutes.do(cache_clearing)
    while True:
        schedule.run_pending()
        time.sleep(1)


# starting a thread of scheduler
t1 = threading.Thread(target=scheduler)
t1.start()
