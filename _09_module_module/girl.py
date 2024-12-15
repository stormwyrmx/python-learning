
count=0


def print_girl(name):
    print(name)

def count_girl():
    print(count)

if __name__ == '__main__':
    count_girl()


"""
__all__ is a list in a Python module that defines the public interface of the module. 
It specifies which names should be imported when from module import * is used. 
If __all__ is not defined, the import * statement will import all names that do not start with an underscore (_).
"""
__all__=['count_girl','print_girl']