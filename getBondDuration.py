import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = int(m * ppy)
    coupon = face * couponRate / ppy

    t = np.arange(1, periods + 1)

    pv = 1 / (1 + y / ppy) ** t

    cf = np.repeat(coupon, periods)
    cf[-1] = cf[-1] + face

    pvcf = cf * pv

    bondPrice = np.sum(pvcf)

    duration = np.sum(t * pvcf) / bondPrice / ppy

    return duration


# Test values from Excel
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

duration = getBondDuration(y, face, couponRate, m, ppy)

print(duration)
print(round(duration, 2))
