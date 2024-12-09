from astropy.utils.console import human_time


class Human:
    def speak(self):
        pass

    def walk(self):
        pass

    def eat(self):
        pass

    def _kawayi(self):
        pass

class Girl(Human):
    def speak(self):
        print("你好，我是可爱的女孩子！")

    def walk(self):
        print("我是女孩子，我会走路")

    def eat(self):
        print("我是女孩子，我会吃饭")

class Boy(Human):
    def speak(self):
        print("你好，我是帅气的男孩子！")

    def walk(self):
        print("我是男孩子，我会走路")

    def eat(self):
        print("我是男孩子，我会吃")


def check_human(human:Human):
    human.speak()
    human.walk()
    human.eat()
    human._kawayi()



girl = Girl()
boy = Boy()
check_human(girl)

