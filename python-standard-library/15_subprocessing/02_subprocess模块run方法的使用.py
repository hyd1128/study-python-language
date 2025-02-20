import subprocess

"""
    标准输入 标准输出 标准错误不同取值带来的效果:
    取值None:
        stdin: 子进程从父进程的标准输入（通常是终端）读取输入。
        stdout: 子进程的标准输出会直接打印到控制台。
        stderr: 子进程的错误信息会直接打印到控制台。
        
    取值PIPE:
        stdin: 可以使用 .communicate(input=...) 传递输入。
        stdout: 将结果储存到了CompletedProcess结果对象的stdout属性中
        stderr: 将结果储存到了CompletedProcess结果对象的stderr中
        
    取值指定文件对象
        stdin=open("input.txt", "r")：子进程从 input.txt 读取输入。
        stdout=open("output.txt", "w")：子进程的输出被写入 output.txt，不会显示在终端。
        stderr=open("error.txt", "w")：子进程的错误信息被写入 error.txt，不会显示在终端。
"""


f = open("./result.txt", "w")
result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True)

# 结果类型
print(type(result))

# text: 是否使用文本格式
print(result.stdout)



