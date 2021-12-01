fin = open('input.txt')
pub_key_card, pub_key_door, _ = fin.read().split('\n')
pub_key_card, pub_key_door = int(pub_key_card), int(pub_key_door)
res = 1
loops = 0
while res != pub_key_card:
    res = (res * 7) % 20201227
    #print(res)
    loops += 1
print(loops)
res = 1
for i in range(loops):
    #print(res)
    res = (res * pub_key_door) % 20201227
print(res)
