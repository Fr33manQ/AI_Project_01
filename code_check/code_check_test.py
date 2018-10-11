import sys
from code_check import CodeCheck
def main():
    # print(">>")
    code_checker = CodeCheck('/Users/Personal/Documents/GitHub/AI_Project_01/algorithm.py', 15)
    # print("?")
    if not code_checker.check_code():
        print(code_checker.errormsg)
    else:
        print('pass')

if __name__ == '__main__':
    main()