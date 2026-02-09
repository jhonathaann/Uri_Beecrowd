B = int(input())
T = int(input())

areaRetangulo = 160 * 70

areaFelix = (T + B)*70/2
areaMarzia = areaRetangulo - areaFelix

if areaFelix > (areaRetangulo / 2):
    print(1)

elif areaMarzia > (areaRetangulo / 2):
    print(2)
else:
    print(0)