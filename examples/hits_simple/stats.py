import conjoiners
import gevent

class Conjoiner(object):
    pass

def main():
    dev = 0
    avg = 0
    prev_cnt = 0
    c = Conjoiner()
    conjoiners.implant(c, "./conf.json", "stats")
    while True:
        gevent.sleep(1)
        dev += 1
        cnt = c.count
        avg = float(avg + (cnt - prev_cnt)) / dev
        print "hits: %s, %s hits/s avg" % (cnt, avg)
        prev_cnt = cnt

        if dev == 2:
            dev = 1

if __name__ == '__main__':
    main()
