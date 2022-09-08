states = ["O'zbekiston",'Misr','Rossiya','Usa','Turkiya']
print(len(states))
print(sorted(states))
print(sorted(states,reverse=True))
print(states)


states.reverse()
print(states)
print(states.sort())
print(states.sort(reverse=True))


numbers = list(range(120,1200,2))
print(sum(numbers))
print(max(numbers) - min(numbers))
print(len(numbers))
print(numbers[:20])
print(numbers[-20:])
print(numbers[530:550])


dishes = ['somsa','manti','norin','kabob','osh']
breakfast = dishes[:]
breakfast.remove('norin')
breakfast.remove('kabob')
breakfast.remove('manti')
breakfast.append('kasha')
breakfast.append('tuhum va sasiska')
print(dishes)
print(breakfast)

