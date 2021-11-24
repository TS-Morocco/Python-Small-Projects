users = ['Adam', 'Ryan', 'Emily', 'Tarik']

for user in users:
    print(user)

looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break
