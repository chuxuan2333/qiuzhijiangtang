"""
在终端下执行此程序
python 示例-用户登录.py 1 -u root -p 123
python 示例-用户登录.py --help
"""
import argparse
parse = argparse.ArgumentParser(prog='Login',
                                usage='%(prog)s [options] usage',
                                description="模拟用户登录",
                                epilog='提示:root 123')

parse.add_argument('user type', type=int, help='用户类型')
parse.add_argument('-u', dest='user', type=str, help='user name')
parse.add_argument('-p', dest='pwd', type=str, help='password')

args = parse.parse_args()   # 获取参数
print(args)
if args.user=='root' and args.pwd=='123':
    print("Login successful")
else:
    print("Login failed")