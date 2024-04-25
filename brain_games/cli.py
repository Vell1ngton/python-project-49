import prompt


def welcome_user():
    prompt.string('May I have your name? ')

#
# if random_number <= 1:
#     result = 'no'
#     for i in range(2, int(random_number ** 0.5) + 1):
#         if random_number % i == 0:
#             result = 'no'
#         else:
#             result = 'yes'