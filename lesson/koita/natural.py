# import time
#
# start = time.time()
#
# with open("/Users/ryoichinakai/WorkSpace/AtCorder/lesson/koita/test") as f:
#     for line in f:
#
#         flag = True
#
#         if int(line) < 2:
#             print(line + "is composite number.\n")
#             flag = False
#
#         for i in range(2, int(line)):
#             if int(line) % i == 0:
#                 print(line + "is composite number.\n")
#                 flag = False
#                 break
#
#         if flag:
#             print(line + "is natural number.\n")
#
# elapsed_time = time.time() - start
# print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

import sys
import os

flag = True

if len(sys.argv) != 2:
    print('Usage: %s MAXIMUM' % (os.path.basename(sys.argv[0])))
    sys.exit(1)

if int(sys.argv[1]) < 2:
    print(sys.argv[1] + "is composite number.\n")
    flag = False

for i in range(2, int(sys.argv[1])):
    if int(sys.argv[1]) % i == 0:
        print(sys.argv[1] + "is composite number.\n")
        flag = False
        break

if flag:
    print(sys.argv[1] + "is natural number.\n")

