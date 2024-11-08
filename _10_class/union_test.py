from typing import Union

"""
以下两种联合类型语法都可以
"""
girls: list[Union[str, int]] = ['Alice', 'Bob', 'Cathy', 1, 2, 3]
boys: list[int | str] = ['Alice', 'Bob', 'Cathy', 1, 2, 3]

# name可以是str类型或者int（默认值为1）类型
def fuck(name: str | int = 1) -> str| int:
    return name


print(fuck("husiqi"))
print(fuck())

