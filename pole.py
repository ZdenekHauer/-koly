skola = ["tužka", "pravítko", "guma", "propiska", "sešit", "úkoly"]
x = len(skola)
for x in skola :
    print(x)
skola.append("lavice")
skola.pop(2)
skola.sort()
skola.reverse()
print(skola)