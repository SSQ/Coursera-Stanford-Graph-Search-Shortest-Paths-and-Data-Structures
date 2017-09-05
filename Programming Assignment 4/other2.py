def sums(nums):
    seen = {}
    nums = sorted(nums)
    nindex = {n: i for i, n in enumerate(nums)}
    MIN = nums[0]
    MAX = nums[-1]
    total = 0
    for i in nums:
        a, b = sorted([(10000 - i), (-10000 - i)])
        print min(MAX, b)
        print max(MIN, a)
        print
        raise SystemError()
    '''
        for n in range(max(MIN, a), min(MAX, b) + 1):
            assert -10000 <= i + n <= 10000
            if n != i and n in nindex:
                if ((i, n) in seen) or ((n, i) in seen): continue
                seen[(i, n)] = True
                seen[(n, i)] = True
                total += 1
    '''
    return total


if __name__ == '__main__':

    input = [-10001, 1, 2, -10001]
    # assert sums(input) == 3

    input = [-10001, 1, 2, -10001, 9999]
    # assert sums(input) == 5

    input = [int(i.rstrip()) for i in open('2sum.txt')]
    print sums(input)
