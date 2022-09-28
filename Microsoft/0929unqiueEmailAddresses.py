ex = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def numUniqueEmails(emails):
    res = set()
    for email in emails:

        name, domain = email.split('@')
        local = name.split('+')[0].replace('.','')
        res.add(local + '@' + domain)

    return len(res)

print(numUniqueEmails(ex))