class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        out = []
        for email in emails:
            host, domain = email.split("@")
            host = host.split("+")[0]
            host = host.replace(".","")
            out.append(host+"@"+domain)
        return len(set(out))