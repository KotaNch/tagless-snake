from snake import Snake

s = Snake(5,5)
print("start",s.body)

s.step()
print("after step:", s.body)

s.step(grow =True)
print("after grow:", s.body)

s.set_direction((0,1))
s.step()
print("after turn:",s.body)

s.set_direction((0,-1))
print("dir after reverce:",s.body)