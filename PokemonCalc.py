Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #charizard vs feraligatr
>>> charizard = 90
>>> feraligatr = 95
>>> modifier = round((1 * 1 * 1 * 2 * 0.85 * 1.5 * 0.25 ),2)
>>> damage = round(((((((2*90)/5)+2)*110*(205/188))/50)+2),2)
>>> tdamage = round ((damage * modifier),2)
>>> print('Damage Dealt: ', tdamage)
Damage Dealt:  59.62
>>> 