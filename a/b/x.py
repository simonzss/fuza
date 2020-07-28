# from a.b import y
# import y
# from a.b.y import *     # 无结果
from . import y  #报错


"""
在涉及到相对导入时，package所对应的文件夹必须正确的被python解释器视作package，而不是普通文件夹。
否则由于不被视作package，无法利用package之间的嵌套关系实现python中包的相对导入。
另外，练习中“from . import XXX”和“from .. import XXX”中的'.'和'..'，可以等同于linux里的shell中'.'和'..'的作用
表示当前工作目录的package和上一级的package，注意，(.)是package，是表示当前工作目录的package
表示当前工作目录的package和上一级的package
表示当前工作目录的package和上一级的package
重要的话说三遍~！！！
"""