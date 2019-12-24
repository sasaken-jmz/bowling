import random

frame = []
for i in range(9):
    throw_1 = random.randint(0, 10)
    throw_2 = random.randint(0, (10-throw_1))
    pin = [throw_1, throw_2]
    frame.append(pin)

throw_1_frame_10 = random.randint(0, 10)
if throw_1_frame_10 == 10:
    throw_2_frame_10 = random.randint(0, 10)
    if throw_2_frame_10 == 10:
        throw_3_frame_10 = random.randint(0, 10)
    else:
        throw_3_frame_10 = random.randint(0, (10-throw_2_frame_10))
else:
    throw_2_frame_10 = random.randint(0, (10-throw_1_frame_10))
    if throw_1_frame_10 + throw_2_frame_10 == 10:
        throw_3_frame_10 = random.randint(0, 10)
    else:
        throw_3_frame_10 = 0
pin = [throw_1_frame_10, throw_2_frame_10, throw_3_frame_10]
frame.append(pin)
print(frame)


scorelist = []
score = 0
for j in range(0, len(frame)-2):
    # strike
    if frame[j][0] == 10 and frame[j+1][0] == 10:
        addi = sum(frame[j]) + sum(frame[j+1]) + frame[j+2][0]
    # strike * 2
    elif frame[j][0] == 10 and frame[j+1][0] != 10:
        addi = sum(frame[j]) + sum(frame[j+1])
    # spare
    elif sum(frame[j]) == 10:
        addi = sum(frame[j]) + frame[j+1][0]
    else:
        addi = sum(frame[j])
    score = score + addi
    scorelist.append(score)

if frame[8][0] == 10 and frame[9][0] == 10:  # strike1
        addi = sum(frame[8]) + frame[9][0] + frame[9][1]
elif sum(frame[j]) == 10:
        addi = sum(frame[j]) + frame[j+1][0]
else:
        addi = sum(frame[j])

score = score + addi
scorelist.append(score)

score = score + sum((frame[9]))
scorelist.append(score)

for j in range(0, len(frame)-1):
    # strike
    if frame[j][0] == 10 and frame[j+1][0] == 10:
        frame[j][0] = 'X'
    # strike * 2
    elif frame[j][0] != 'X' and frame[j][0] == 10 and frame[j+1][0] != 10:
        frame[j][0] = "X"
    # strike at frame9
    elif frame[j][0] != 'X' and\
            frame[j][0] == 10 and\
            frame[j+1][0] == 10 and\
            frame[j+1][1] == 10:
        frame[j][0] = "X"
    elif frame[j][0] != 'X' and sum(frame[j]) == 10:
        frame[j][1] = "/"

if frame[9][0] == 10:
    frame[9][0] = 'X'
    if frame[9][1] == 10:
        frame[9][1] = 'X'
    elif frame[9][1] != 'X' and frame[9][1] + frame[9][2] == 10:
        frame[9][2] = '/'
        if frame[9][2] == 10:
            frame[9][2] = 'X'
elif frame[9][0] != 'X' and\
        frame[9][1] != 'X' and\
        frame[9][0] + frame[9][1] == 10:
    frame[9][1] = '/'
    if frame[9][2] == 10:
        frame[9][2] = 'X'
print(scorelist)
print(frame)

framenew = []
for sublist in frame:
    for item in sublist:
        framenew.append(item)

f = open('score.html', 'w')
f.write('<table>')
f.write(
    '<table bgcolor = "#afeeee",\
    border = "1" cellpadding = "10" cellspacing = "0">'
    )

f.write("<tr>")
for i in range(9):
    f.write('<td colspan="2", align=center>{0}</td>'.format(i+1))
f.write('<td colspan="3", align=center>{0}</td>'.format(10))
f.write("</tr>")
f.write("<tr>")
for i in range(21):
    f.write('<td align=center>{0}</td>'.format(framenew[i]))
f.write("</tr>")
f.write("<tr>")
for i in range(9):
    f.write('<td colspan="2", align=center>{0}</td>'.format(scorelist[i]))
f.write('<td colspan="3", align=center>{0}</td>'.format(scorelist[9]))
f.write("</tr>")
f.write("</table>")
f.close()
