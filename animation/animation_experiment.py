"""experiments with terminal"""
import time

animation = "|/-\\"
idx = 0
while True:
    print (animation[idx % len(animation)] + "\r",)
    idx += 1
    time.sleep(0.1)

# import time
# for i in range(10):
#     print(animation[i], end='')
#
#     time.sleep(1)
#     print('\r', end='')
# print()
