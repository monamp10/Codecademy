import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# 1
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# 2
v_c = pd.merge(visits,cart,how='left')
print(v_c)

# 3
print(len(v_c))

# 4
print(len(v_c[v_c.cart_time.isnull()]))

# 5
v_c_percent = len(v_c[v_c.cart_time.isnull()]) * 100 / len(v_c)
print(float(v_c_percent))

# 6
c_ch = pd.merge(cart,checkout,how='left')
print(c_ch)
print(len(c_ch[c_ch.checkout_time.isnull()]))
c_ch_percent = len(c_ch[c_ch.checkout_time.isnull()])*100 /len(c_ch)
print(float(c_ch_percent))

# 7
all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())

# 8
ch_p = pd.merge(checkout,purchase,how='left')
ch_p_percent = len(ch_p[ch_p.purchase_time.isnull()])*100 / len(ch_p)
print(float(ch_p_percent))

# 10
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data)

# 11
print(all_data.time_to_purchase)

# 12
print(all_data.time_to_purchase.mean())