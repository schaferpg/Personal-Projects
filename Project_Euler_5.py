num_Holder = []
for i in range(1,21):
    num_Holder.append(i)

def test_Function(num):
    for i in range(len(num_Holder)):
        if num % num_Holder[i] != 0:
            return False
    return True


number = 20
while True:
    if test_Function(number):
        break
    number += 20
print(number)
