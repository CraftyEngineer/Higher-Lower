import random
import game_data as gd
def compare_acc(acc_a, acc_b):
    if acc_a['follower_count']>acc_b['follower_count']:
        return acc_a 
    else:
        return acc_b

def get_random_account():
  """Get data from random account"""
  return random.choice(gd.data)