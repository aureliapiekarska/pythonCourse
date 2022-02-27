# import this ....
s1 ='The Zen of Python, by Tim Peters Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases arent special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless youre Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, its a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- lets do more of those!'
print(s1)
#policz liczbe wystapien better
print(s1.count('better'))
#usun symbol gwiazdki
s1.split(',')
print(s1.replace('*', ' '))
#zamien jedno wystapeinie explain na understand
print(s1.replace('explain','understand', 1))
#usun spacje i polacz wszystkie slowa myslnikiem
print(s1.replace(' ' , '-'))
#podziel tekst na osobne zdania za pomoca kropki
print(s1.split('.'))



