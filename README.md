# NewsAndMovies-Scraper

This project contains a Python-based web scraper that retrieves top news articles from Hacker News and a list of the best 100 movies from Empire Online. The scraper uses `BeautifulSoup` and `requests` to extract and process the data.

## Features

- **Hacker News Scraper**: 
  - Extracts article titles, links, and points from Hacker News.
  - Identifies the article with the highest points.

- **Empire Online Scraper**:
  - Extracts and saves the top 100 movies in reverse order from Empire Online's "Best Movies" list.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dipec001/NewsAndMovies-Scraper.git
   cd NewsAndMovies-Scraper
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage
- Run the script:
```bash
python app.py
```
-The script outputs:

The article with the highest points from Hacker News.
A text file movie.txt containing the top 100 movies.

### Project Structure
app.py: The main script that contains the scraping logic.
movie.txt: The output file containing the list of top 100 movies.
requirements.txt: Lists the dependencies required for the project.

### Dependencies
- requests
- beautifulsoup4

Install these dependencies
```bash
pip install -r requirements.txt
```
Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!
