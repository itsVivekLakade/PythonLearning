from requests import get

response = get('https://git.elektrobitautomotive.com/api/v3/repos/EB-EST-COS-A-4/COS_DEVOPS_SANDBOX/pulls', auth=('vila274183', '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'))
print (response.text)
