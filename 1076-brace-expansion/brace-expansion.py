class Solution:
    def expand(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        cur = []
        def dfs(idx: int, isBrace: bool, tmp: List[int]) -> None:
            if idx == len(s):
                res.append("".join(cur))
                return

            if s[idx] == "{":
                dfs(idx + 1, True, tmp)
            elif isBrace and "a" <= s[idx] <= "z":
                tmp.append(s[idx])
                dfs(idx + 1, isBrace, tmp)
            elif isBrace and s[idx] == "}":
                print(tmp)
                for c in tmp:
                    cur.append(c)
                    dfs(idx + 1, not isBrace, [])
                    cur.pop()
            elif "a" <= s[idx] <= "z":
                # print(s[idx])
                cur.append(s[idx])
                dfs(idx + 1, isBrace, tmp)
                cur.pop()
            elif s[idx] == ",":
                dfs(idx + 1, isBrace, tmp)

        dfs(0, False, [])
        return sorted(res)