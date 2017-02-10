import requests, re, sys

read_file = requests.get(sys.argv[1]).text

if sys.argv[2].lower() == 'phone':
    PhoneRegex = re.compile(r'((\(\d\d\d\)|\d\d\d)(\s|-)(\d\d\d-\d\d\d\d))')
    results = PhoneRegex.findall(read_file)
    results = [results[i][0] for i in range(len(results))]
    # list comprehension to show the results of the first group only (the full number)
    # rather than showing the invidividual area code and first 3 digits groups 
    print(results)
elif sys.argv[2].lower() == 'email':
    EmailRegex = re.compile(r'''([a-zA-Z0-9_%-]+@[a-zA-Z0-9_%-]+\.[a-zA-Z]{2,4})''') # alphanum charset for user and doman
    results = EmailRegex.findall(read_file)
    print(results)
                            
                        
    
 
