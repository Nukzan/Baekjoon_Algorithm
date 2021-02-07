# -*- coding: utf-8 -*-
"""day7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jWPgim4WPyMRPGk56PR15yk0FyqntVlT
"""

# 11654
#문제 : d알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때,
# 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 입력 : 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# A

# 출력 : 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
# 65

print(ord(input()))

# 11720
#문제 : N개의 숫자가 공백 없이 쓰여있다.
# 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오..

# 입력 : 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다.
# 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 5
# 54321

# 출력 : 입력으로 주어진 숫자 N개의 합을 출력한다.
# 15

n = int(input())
a = list(input())
li = []

for i in a:
  li.append(int(i))
print(sum(li))

# 10809
#문제 : 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 단어 S가 주어진다.
# 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# baekjoon

# 출력 : 각각의 알파벳에 대해서, a가 처음 등장하는 위치,
# b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

s = str(input())
li = []

for i in range(ord('a'),ord('z')+1):
  a = s.find(chr(i))
  li.append(a)

for i in li:
  print(i, end=" ")

# 2675
#문제 : 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는
# 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고,
# 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력 : 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
# 2
# 3 ABC
# 5 /HTP

# 출력 : 각 테스트 케이스에 대해 P를 출력한다.
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

n = int(input())

for i in range(n):
  a = input().split()
  li = ""
  for i in range(len(a[1])):
    string = a[1][i]*int(a[0])
    li += string
  print(li)

# 1157
#문제 : 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# Mississipi

# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# ?

n = str(input()).upper() # 단어 입력
li = []
x = []
cnt = 0

for i in range(len(n)):
  if n[i] not in li : # 중복 제거 단어 리스트 만들기
    li.append(n[i])

for j in li:
  a = n.count(j)  # 입력받은 단어의 알파벳 사용 횟수 카운트
  x.append(a) # x 리스트에 카운트 저장

for m in range(len(x)):
  if (max(x) == x[m]):
    cnt += 1  # 알파벳 사용 횟수의 max를 찾으면 cnt를 1 증가시킴
    k = m   # max가 해당하는 알파벳의 인덱스

if (cnt==1) :   # max 값을 가진 수가 1개면
  print(li[k])    # 중복제거 리스트에서 알파벳을 가져옴
else :
  print('?')