from snake import Snake

s2 = Snake(2,0)
print("start:", s2.body, "wall?", s2.hits_wall(10,10))

s2.set_direction((0,-1))
s2.step()
print("after up:", s2.body, "wall?", s2.hits_wall(10,10))


s = Snake(5,5)
print("start",s.body)


for _ in range(3):    
    s.step(grow =True)

s.set_direction((0, 1))
s.step(grow=True)
s.set_direction((-1, 0))
s.step(grow=True)
s.set_direction((0, -1))
s.step(grow=True)
print("body:", s.body, "self?", s.hits_self())
