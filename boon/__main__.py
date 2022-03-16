from distutils.command.build import build
import sys
import requests
from colorama import Style, Fore
from concurrent.futures import ThreadPoolExecutor, as_completed

green = '\033[92m'
reset = Style.RESET_ALL
good = (Style.BRIGHT+ '['+'\033[1;32m+\033[0m'+Style.BRIGHT+']'+Style.RESET_ALL)
bad = (Style.BRIGHT + '['+ Fore.RED + '-' + Style.RESET_ALL + Style.BRIGHT + ']' + Style.RESET_ALL)
run = (Style.BRIGHT + '['+ Fore.BLUE + '*' + Style.RESET_ALL + Style.BRIGHT + ']' + Style.RESET_ALL)

print(Style.BRIGHT
+f"""
   ___               
  / _ )___  ___  ___ 
 / _  / _ \/ _ \/ _ \ 
/____/\___/\___/_//_/ v1.0

            ({green}\x1B[3mBy Nefcore\x1B[0m{reset})
""")

try:
    username = sys.argv[1]
except IndexError:
    print(bad, 'No Username specified!')
    quit()

URLs = ["Instagram-https://instagram.com/{injex}", "Facebook-https://facebook.com/{injex}", "YouTube-https://www.youtube.com/c/{injex}", 
        "Wordpress-https://{injex}.wordpress.com", "Pinterest-https://www.pinterest.com/{injex}", "GitHub-https://www.github.com/{injex}", 
        "Quora-https://www.quora.com/profile/{injex}", "Tumblr-https://{injex}.tumblr.com/", 
        "Flickr-https://www.flickr.com/people/{injex}", "Soundcloud-https://soundcloud.com/{injex}", "Disqus-https://disqus.com/{injex}", 
        "Medium-https://medium.com/@{injex}", 
        "Deviantart-https://{injex}.deviantart.com", "VK-https://vk.com/{injex}", "About.me-https://about.me/{injex}", 
        "SlideShare-https://www.slideshare.net/{injex}",  
        "Scribd-https://www.scribd.com/{injex}", "Badoo-https://badoo.com/{injex}", "Patreon-https://www.patreon.com/{injex}", 
        "Bitbucket-https://bitbucket.org/{injex}/", "Dailymotion-https://www.dailymotion.com/{injex}", "Etsy-https://www.etsy.com/shop/{injex}", 
        "Behance-https://www.behance.net/{injex}", "GoodReads-https://www.goodreads.com/{injex}", "Instructables-https://www.instructables.com/member/{injex}", 
        "Keybase-https://keybase.io/{injex}", "Kongregate-https://www.kongregate.com/accounts/{injex}", "Livejournal-https://{injex}.livejournal.com/", 
        "Last.fm-https://last.fm/user/{injex}", "Dribbble-https://dribbble.com/{injex}", 
        "Gravatar-https://en.gravatar.com/{injex}", "Pastebin-https://pastebin.com/u/{injex}", "Roblox-https://www.roblox.com/user.aspx?username={injex}", 
        "Gumroad-https://www.gumroad.com/{injex}", "Creativemarket-https://creativemarket.com/{injex}", "Trakt-https://www.trakt.tv/users/{injex}", 
        "Buzzfeed-https://www.buzzfeed.com/{injex}", "Hubpages-https://{injex}.hubpages.com", "Contently-https://{injex}.contently.com/", 
        "Houzz-https://www.houzz.com/user/{injex}", "Wikipedia-https://en.wikipedia.org/wiki/User:{injex}", "Ello-https://ello.co/{injex}", "https://vimeo.com/{injex}", "https://www.codementor.io/{injex}", "https://bandcamp.com/{injex}"]

session = requests.Session()

print(run, f'Finding {username} on {len(URLs)} platforms...'+'\n')

class scanner:
    def requester(url, username):
        parts = url.split('-')
        url = parts[1]
        platform = parts[0]
        build_url = url.replace('{injex}', username)
        request_get = session.get(build_url)
        status = request_get.status_code

        if status == 200:
            print(good, Style.BRIGHT + platform + ': ' + Style.RESET_ALL + build_url)
        else:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        for url in URLs:
            executor.submit(requester, url, username)

def main():
    scanner()

