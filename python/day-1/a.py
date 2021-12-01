def find_product(nums):
    for n1 in nums:
        for n2 in nums:
            if n1 + n2 == 2020:
                return n1 * n2

def main():
    nums = [int(s) for s in open('input.txt').read().split()]
    print(find_product(nums))

main()