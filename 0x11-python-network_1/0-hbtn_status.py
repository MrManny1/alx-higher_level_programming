#!/usr/bin/python3
"""Python script that 
- fetches https://alx-intranet.hbtn.io/status
- use the package urllib
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

if __name__ == "__main__":

if __name__ == '__main__':
    import urllib.request
    

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
