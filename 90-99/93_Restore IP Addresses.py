# -*- coding:utf-8 -*-
# https://leetcode.com/problems/restore-ip-addresses/description/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        
        def f(s, address):
            if not s or len(address) == 4:
                not s and len(address) == 4 and ret.append(''.join(address))
                return
            bg, ed = 1, 1 if s[0] == '0' else min(3, len(s))
            for i in xrange(bg, ed + 1):
                digit = s[:i]
                if 0 <= int(digit) <= 255:
                    if len(address) < 3:
                        address.append(digit + '.')
                    else:
                        address.append(digit)
                    f(s[i:], address)
                    address.pop()
                    
        f(s, [])
        
        return ret