require 'conjoiners'

class Conjoiner
  attr_accessor :count
end

div = 1
avg = 0
prev_cnt = 0
maxa = 0
mina = 10000000
c = Conjoiner.new
Conjoiners::implant(c, "./conf.json", "stats_ruby")
sleep 1
while true
  sleep(1)
  cnt = c.count
  diff = cnt - prev_cnt
  if div > 1
    if diff > maxa
      maxa = diff
    end
    if diff < mina
      mina = diff
    end
    avg = (avg + diff) / div
    puts "hits: %s, %s hits/s avg, max %s hits/s, min %s hits/s" % [cnt, avg, maxa, mina]
  end
  div = 2
  prev_cnt = cnt
end
