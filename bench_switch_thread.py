import util
import math

NUM_TESTS = 10


def startBench(coroutines) -> int:
    return int(util.run_loom('loom/BenchSwitchThread.java', coroutines)[7])

print('--Start thread bench--')

switchesPerSecond = [startBench('100') for i in range(NUM_TESTS)]

mean, std = util.stdev(switchesPerSecond)

print('Result: {} +/- {}'.format(mean, std))
