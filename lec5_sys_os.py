import sys, os

print(os.getcwd())

os.system("echo hi!")
# os.system("python3 /workspaces/math_modeling/lec5_sys_os.py ")
print("Python version is:", sys.path)
print(sys.path)
print(sys.platform)

print(dir(sys))
print(dir(os))