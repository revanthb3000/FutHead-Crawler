import BeautifulSoup
import mechanize

def main():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    browser.open("http://www.futhead.com/15/players/5/")
    print browser.response().read()

if __name__ == '__main__':
    main()