def minWindow(s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_len = float('inf')
        f_t = {}
        for char in t:
            f_t[char] = f_t.get(char, 0) + 1

        l = 0
        res_l, res_r = 0, 0
        f_s = {}
        for r in range(len(s)):
            # add char to freq
            f_s[s[r]] = f_s.get(s[r], 0) + 1

            def is_valid(fs, ft):
                for key in ft:
                    if fs.get(key, 0) < ft[key]:
                        return False
                return True

            # remove chars 
            while is_valid(f_s, f_t) and l <= r:
                # update min sub before reducing
                curr_len = (r-l)+1 
                if curr_len < min_len:
                    min_len = curr_len
                    res_l, res_r = l, r
                
                f_s[s[l]] -= 1
                if f_s[s[l]] == 0:
                    del f_s[s[l]]
                
                l += 1

        return s[res_l : res_r + 1] if min_len != float('inf') else ""