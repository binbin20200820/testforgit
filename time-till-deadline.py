import datetime

user_input = input("enter your goal with a deadLine separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
dateline = input_list[1]

deadline_date = datetime.datetime.strptime(dateline, "%H.%d.%m.%Y")
# print(input_list)
# calculate how many days from now till deadline
today_date = datetime.datetime.today()
# print(datetime.datetime.today())
# Distance college entrance examination :9.07.06.2022
# learn python:9.07.06.2022
print('today:', today_date)
print(goal, ':', (deadline_date - today_date))
