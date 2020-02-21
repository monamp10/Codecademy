import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# 1
print(ad_clicks.head())

# 2
utm_sources = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_sources)

# 3
ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

# 4
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

# 5
clicks_pivot = clicks_by_source.pivot(
                        columns = 'is_click',
                        index = 'utm_source',
                        values = 'user_id').reset_index()
print(click_pivot)

# 6
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])


# 7
experimental_group_count = ad_clicks.groupby('experimental_group').user_id.count()
print(experimental_group_count)

# 8
is_click_experimental = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

is_click_experimental_pivot = is_click_experimental.pivot(columns='is_click', index='experimental_group', values='user_id')

print(is_click_experimental_pivot)

is_click_experimental_pivot['percent_clicked']= \
	      is_click_experimental_pivot[True] /\
        (is_click_experimental_pivot[True] + 
        is_click_experimental_pivot[False])

print(is_click_experimental_pivot)

# 9
a_clicks = ad_clicks[ad_clicks.experimental_group
   == 'A']
b_clicks=ad_clicks[ad_clicks.experimental_group
   == 'B']

# 10
aclicks_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks_day= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

aclicks_pivot = aclicks_day.pivot(columns='is_click',index='day',values='user_id')
aclicks_pivot['percent_clicked'] = \
	aclicks_pivot[True] /\
  (aclicks_pivot[True] + 
  aclicks_pivot[False])
print aclicks_pivot
bclicks_pivot = bclicks_day.pivot(columns='is_click',index='day',values='user_id')
bclicks_pivot['percent_clicked'] = \
	bclicks_pivot[True] /\
  (bclicks_pivot[True] + 
  bclicks_pivot[False])
print bclicks_pivot

