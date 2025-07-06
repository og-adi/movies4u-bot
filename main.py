import requests
from bs4 import BeautifulSoup
from seleniumbase import SB

def url_generator(query):
    query = query.replace(' ','+')
    query_url = f'https://www.movies4u.mov/?s={query}'
    resp = requests.get(query_url)
    soup = BeautifulSoup(resp.content,'html.parser')
    posts = soup.find('div',class_='container d-flex flex-wrap')
    posts_title = posts.findAll('h3',class_='entry-title')
    links = []
    if posts_title == []:
        return None
    elif len(posts_title) >= 2:
        print(f'{len(posts_title)} Results found !')
        print()
        for i in range(len(posts_title)):
            title = posts_title[i].text
            link = posts_title[i].find('a').get('href')
            links.append(link)
            print(f"{i+1}. {title} - {link}")
        print()
        choice = int(input('Enter no. of choice: '))
        url = links[choice-1]
        return url
    else:
        url = posts_title[0].find('a').get('href')
        if url == None:
            return None
        else:
            return url

def url_finder(html):    
    soup = BeautifulSoup(html,'html.parser')
    btns = soup.find('div',class_='download-links-div')
    a_ele = btns.find_all('a')
    for a_tag in a_ele:
        link = a_tag.get('href')
        if 'linkz.wiki' or 'linkz.mom' in link:
            return link
        else:
            return None

def bypass(url):
    try:
        with SB(uc = True) as sb:
            sb.driver.uc_open_with_reconnect(url,10)
            html = sb.driver.get_page_source()
            return html
    except:
        return None

query = input('Enter name to search: ')
url1 = url_generator(query)
if url1 == None:
    print('Results Not found!')
else:
    print("Generating link for :",url1)
    print()
    resp = requests.get(url1)
    html1 = resp.content
    wiz_link = url_finder(html1)
    if wiz_link == None:
        print('No links found!')
    else:
        print(f'Redirecting to {wiz_link}....')
        print()
        print('--------------------------------------------------------------------------------')
        wiz_html = bypass(wiz_link)
        if wiz_html == None:
            print('Driver Error')
        else:
            soup = BeautifulSoup(wiz_html,'html.parser')
            cont = soup.find('div',class_='download-links-div')
            headings = cont.findAll('h4')
            if headings == []:
                headings = cont.findAll('h5')
            btns = soup.findAll('div',class_='downloads-btns-div')

            try:
                for i in range(len(btns)):
                    print(headings[i].text)
                    a_ele = btns[i].find_all('a')
                    for link in a_ele:
                        print(link.get('href'))
                    print()
            except:
                print('')

