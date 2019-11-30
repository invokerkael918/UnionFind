import collections


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def accountsMerge(self, accounts):
        # write your code here
        self.father = {}
        if not accounts:
            return []
        # initialize self.father{} by emails
        for account in accounts:
            if not account or len(account) < 2:
                continue
            for email in account[1:]:
                self.father[email] = email
        # union
        for account in accounts:
            if not account or len(account) < 2:
                continue
            for email in range(2, len(account)):
                self.union(account[email - 1], account[email])

        email_set = collections.defaultdict(set)
        email_to_acct = {}
        for account in accounts:
            if not account:
                continue
            name = account[0]
            for email in account[1:]:
                root_email = self.find(email)
                email_set[root_email].add(email)
                if root_email not in email_to_acct:
                    email_to_acct[root_email] = name

        results = []
        for root_email in email_set:
            temp = [email_to_acct[root_email]] + sorted(list(email_set[root_email]))
            results.append(temp)
        return results

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        self.father[rootA] = rootB

    def find(self, user_id):
        path = []

        while user_id != self.father[user_id]:
            path.append(user_id)
            user_id = self.father[user_id]

        for n in path:
            self.father[n] = user_id
        return user_id
