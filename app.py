import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    response = requests.get('https://news.ycombinator.com/news')
    yc_news_page = response.text

    soup = BeautifulSoup(yc_news_page, 'html.parser')

    article_texts = []
    article_links = []
    for article in soup.find_all('span', class_='titleline'):
        title = article.text
        link = article.a.get('href')
        article_texts.append(title)
        article_links.append(link)

    article_points = [int(point.text.split()[0]) for point in soup.find_all('span', class_='score')]

    largest_point = max(article_points)
    index_of_largest = article_points.index(largest_point)

    print("The largest point is:", largest_point)
    print("The index of the largest point is:", index_of_largest)
    print("The article with the largest point is:", article_texts[index_of_largest])
    print("The link of the article with the largest point is:", article_links[index_of_largest])

def scrape_top_movies():
    URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
    response = requests.get(URL)
    movies_page = response.text

    soup = BeautifulSoup(movies_page, 'html.parser')

    titles_list = [title.getText() for title in soup.find_all('h3', class_='title')]
    reversed_titles_list = titles_list[::-1]

    with open('movies.txt', 'w', encoding="utf-8") as file:
        for title in reversed_titles_list:
            file.write(title + '\n')

if __name__ == "__main__":
    scrape_hacker_news()
    scrape_top_movies()
