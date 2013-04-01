import conjoiners
import gevent

class Conjoiner(object):
    pass

def main():
    div = 1
    avg = 0
    prev_cnt = 0
    maxa = 0
    mina = 10000000
    c = Conjoiner()
    conjoiners.implant(c, "./conf.json", "stats")
    while True:
        gevent.sleep(1)
        cnt = c.count
        diff = cnt - prev_cnt
        if div > 1:
            if diff > maxa:
                maxa = diff

            if diff < mina:
                mina = diff

            avg = (avg + diff) / div
            print "hits: %s, %s hits/s avg, max %s hits/s, min %s hits/s" % (cnt, avg, maxa, mina)
        div = 2
        prev_cnt = cnt
        

if __name__ == '__main__':
    main()
