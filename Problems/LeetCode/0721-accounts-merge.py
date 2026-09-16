class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        idToName = {}
        E = defaultdict(list)

        for i, account in enumerate(accounts):
            name = account[0]
            idToName[i] = name

            for email in account[1:]:
                E[i].append(email)
                E[email].append(i)

        ans = []
        seen = set()

        for i in range(len(accounts)):
            emails = []
            if i in seen: continue
            dfs = [i]
            while dfs:
                curr = dfs.pop()
                if curr in seen: continue
                seen.add(curr)
                if type(curr) == str:
                    emails.append(curr)

                for edge in E[curr]:

                    if edge in seen: continue
                    dfs.append(edge)
            ans.append([idToName[i]] + sorted(emails))
        return ans