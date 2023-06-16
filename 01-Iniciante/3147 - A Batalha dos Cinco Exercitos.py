humanos, elfos, anoes, orcs, wargs, aguias = map(int, input().split())
bem = humanos + elfos + anoes
mal = orcs + wargs

if bem > mal:
    print('Middle-earth is safe.')
else:
    bem += aguias
    if bem >= mal:
        print('Middle-earth is safe.')
    else:
        print('Sauron has returned.')
