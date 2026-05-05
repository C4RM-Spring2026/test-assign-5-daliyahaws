import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = int(m * ppy)
    coupon = face * couponRate / ppy

    t = np.arange(1, periods + 1)

    pv = 1 / (1 + y / ppy) ** t

    cf = np.repeat(coupon, periods)
    cf[-1] = cf[-1] + face

    bondPrice = np.sum(cf * pv)

    return bondPrice


# Test values from Excel
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

# Annual (matches left table)
price_annual = getBondPrice(y, face, couponRate, m, ppy=1)

# Semi-annual (matches right table)
price_semi = getBondPrice(y, face, couponRate, m, ppy=2)

print(price_annual)
print(round(price_annual, 2))

print(price_semi)
print(round(price_semi, 2))
