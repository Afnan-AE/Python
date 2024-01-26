class ain:

    alive = True

    def eat(self):
        print("HEY I AM EATING!")

    def walk(self):
        print("Lemme talk a walk.")

    def sleep(self):
        print("Sleeping don't disturb.")


class ra(ain):
    def run(self):
        print("As a rabbit, I am running")

class ba(ain):
    def fly(self):
        print("As a bat, I am flying")

class fi(ain):
    def swim(self):
        print("As a fish, I as swimming")


r = ra()
b = ba()
f = fi()

print(r.alive + b.alive +f.alive)
r.walk()
r.run()
b.eat()
b.fly()
f.sleep()
f.swim()