#stworz zmienna zadanie 1 z ostatniej grupy zadan

txt = "babababbabaa"
center_txt = len(txt) // 2
prev_center = center_txt - 1 #3
next_center = center_txt +1 #5

print(txt[prev_center:next_center + 1])