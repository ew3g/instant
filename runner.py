# -*- encoding: utf-8 -*-

from utils import Utils
import datetime
from collector import Collector
from follower import Follower
from unfollower import Unfollower
from poster import Poster


next_run_collector = 0
interval_run_collector = 1

next_run_follower = 0
interval_run_follower = 1

# next_run_unfollower = 0
# interval_run_unfollower = 5

next_run_poster = 0
interval_run_poster = 1



while True:
  now = Utils.current_time_milliseconds()

  if(now >= next_run_collector):
    print('\n\n\n******************')
    print('Executando o coletor')
    collector = Collector()
    collector.run()
    next_run_collector = (Utils.current_time_milliseconds() + (interval_run_collector * 3600000))
    print('Finalizado. Próxima execução: ' + str(datetime.datetime.fromtimestamp(next_run_collector / 1000.0)))
    print('**********************')

  if(now >= next_run_follower):
    print('\n\n\n******************')
    print('Executando o follower')
    follower = Follower()
    follower.run()
    next_run_follower = (Utils.current_time_milliseconds() + (interval_run_follower * 3600000))
    print('Finalizado. Próxima execução: ' + str(datetime.datetime.fromtimestamp(next_run_follower / 1000.0)))
    print('**********************')  

  if(now >= next_run_poster):
    print('\n\n\n******************')
    print('Executando o poster')
    poster = Poster()
    poster.run()
    next_run_poster = (Utils.current_time_milliseconds() + (interval_run_poster * 3600000))
    print('Finalizado. Próxima execução: ' + str(datetime.datetime.fromtimestamp(next_run_poster / 1000.0)))
    print('**********************')