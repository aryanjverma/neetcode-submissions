class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailAccounts = {}
        for j in range(len(accounts)):
            account = accounts[j]
            for i in range(1, len(account)):
                email = account[i]
                if email not in emailAccounts:
                    emailAccounts[email] = []
                emailAccounts[email].append(j)
        visited = [False] * len(accounts)
        def dfs(i, answer):
            if not visited[i]:
                visited[i] = True
                for j in range(1, len(accounts[i])):
                    email = accounts[i][j]
                    if email not in answer:
                        answer.add(email)
                        for account in emailAccounts[email]:
                            dfs(account, answer)
        
        result = []
        for i in range(len(accounts)):
            if not visited[i]:
                answer = set()
                dfs(i, answer)
                result.append([accounts[i][0]] + sorted(list(answer)))
        return result