
import HW4 as Cls

PROB = 0.4
TIME_STEPS = 20
Realization_times= 1000

myGame = Cls.Games(realization_times=Realization_times, prob=PROB)

# simulate
myGame.simulate(TIME_STEPS)

# print
print(myGame.get_ave_exp_cost())
print(myGame.get_total_time())




