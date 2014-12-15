import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())
C = int(raw_input())
budgets = []
for i in xrange(N):
    budgets.append(int(raw_input()))
    
sorted_budgets = sorted(budgets)
participants = len(budgets)
gift_remain = C

distribution = []

for i in xrange(N):
    share = gift_remain / participants
    if share <= sorted_budgets[i]:
        distribution.append(share)
        gift_remain -= share
    else:
        distribution.append(sorted_budgets[i])
        gift_remain -= sorted_budgets[i]
    participants -= 1

if gift_remain > 0:
    print "IMPOSSIBLE"
else:
    for share in distribution:
        print share

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
