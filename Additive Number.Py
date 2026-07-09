class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                # Skip numbers with leading zeros
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue

                a = int(first)
                b = int(second)
                k = j

                while k < n:
                    s = str(a + b)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    a, b = b, a + b

                if k == n:
                    return True

        return False
