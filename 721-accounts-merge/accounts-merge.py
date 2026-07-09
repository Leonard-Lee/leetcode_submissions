class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node]) 

        return self.parents[node]

    def union(self, n1, n2) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        # connect all the emails under the same idx
        emailToIdx = {}
        for idx, account in enumerate(accounts):
            for i in range(1, len(account)):
                email = account[i]
                if email not in emailToIdx:
                    emailToIdx[email] = idx
                else:
                    uf.union(idx, emailToIdx[email])

        # grouping
        # root idx mapping to a list of emails
        groups = defaultdict(list)
        for email, idx in emailToIdx.items():
            rootIdx = uf.find(idx)
            groups[rootIdx].append(email)

        # populate the res
        res = []
        for idx, emails in groups.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res



        





        
