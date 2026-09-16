# any() and all() are usefull while checking the conditionals
scores = [80, 90, 75, 60]
print(any(score < 50 for score in scores))

# any()->at lest 1 is true
# all() everything is true
print(all(score >= 50 for score in scores))