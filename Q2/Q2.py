rowsCount = input()

msg = []

#Get input from user
for __ in range(int(rowsCount)):
    msg.append(input().split(' '))


allValid = True
errCodes = []
for i in range(int(rowsCount)):

    if(msg[i][1] == 'false'):
        rowValid = False
    else:
        rowValid = True

    if(allValid and not rowValid):
        allValid = False
    
    if not rowValid:
        errCodes.append(msg[i][2])

if allValid:
    print('Yes')
else:
    print('No')
    print(' '.join(errCodes))