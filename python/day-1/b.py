def find_product(nums):
    for n1 in nums:
        for n2 in nums:
            for n3 in nums:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3

nums = [int(s) for s in open('input.txt').read().split()]
print(find_product(nums))