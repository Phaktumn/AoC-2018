import time

file = open('input.txt', "r")
lines = [line.rstrip('\n') for line in file]

DEBUG = 1

res_frequency = 0
first_repeated_frequency = -1
last_frequency = 0

repeated_found = False
frequencies = set()

times_repeated = 0
freq_count = 0

start = time.time()

frequencies.add(0)
while repeated_found is False:
    times_repeated += 1
    for line in lines:
        frequency = int(line[1:])
        last_frequency = res_frequency
        res_frequency += (frequency if line[0] == "+" else -frequency)
        if DEBUG is 1:
            print('prev [{}] {} [{}] resulting in [{}]'.format(last_frequency, line[0], frequency, res_frequency))
        if res_frequency in frequencies:
            first_repeated_frequency = res_frequency
            repeated_found = True
            freq_count = len(frequencies)
            break
        frequencies.add(res_frequency)

end = time.time()
elapsed = end-start

print('Frequencies Result = {}'.format(res_frequency))
print('Repeated Frequency = {}'.format(first_repeated_frequency))
print('Retries - {}    Frequencies Length - {}'.format(times_repeated, freq_count))
print('Took {} seconds to compute'.format(elapsed))
