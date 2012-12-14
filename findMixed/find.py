import requests
import re
custom_sites = [
  'www.nytimes.com',
  'www.bankofamerica.com',
  'www.yahoo.com',
  'www.baidu.com',
  'www.wikipedia.org',
  'www.live.com',
  'www.amazon.com',
  'www.twitter.com',
  'www.blogspot.com',
  'www.linkedin.com',
  'www.facebook.com',
  'www.ebay.com',
  'www.msn.com',
  'www.cnn.com',
  'www.tumblr.com',
  'www.pinterest.com',
  'www.paypal.com',
  'www.blogger.com',
  'www.craigslist.com',
  'www.bbc.co.uk',
  'www.ask.com',
  'www.flickr.com'
    ]

def get_bank_sites():
  ret = []
  f = open('banksites', 'r')
  regex = r'<a href="(.*?)"'
  matches = re.findall(regex, f.read())
  for match in matches:
    site = make_https(match)
    ret.append(site)

  f.close()
  return ret

def get_tops(file_name):
  ret = []
  f = open(file_name, 'r')
  for line in f.readlines():
    site = make_https(line)
    ret.append(site)
  f.close()
  return ret

def make_https(site):
  parts = site.split('://')
  if len(parts) > 1:
    return parts[1]
  return site

def check_mixed(sites):
  for site in sites:
    site = 'https://www.' + site.strip()
    print 'Checking', site
      #res = requests.get(site, timeout=3, allow_redirects=False)
    try:
      res = requests.get(site, timeout=3, verify=False)
      if res.url.startswith('https'):
          regex = r'src=[\'"](http://.*?)[\'"]'
          matches = re.findall(regex, res.content)
          print len(matches), 'pieces of mixed content!'
          for match in matches:
            print match
      else:
        print 'redirection happened; not https anymore'
    except Exception:
      print 'Problem with request'

 
#check_mixed(get_bank_sites())
#check_mixed(custom_sites)
#check_mixed(get_tops('top500'))
check_mixed(get_tops('top10k.out'))
