# MOVIES4U BOT
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/og-adi/movies4u-bot)

This is a command-line utility built with Python to automate the process of finding and extracting download links for movies and TV shows from `movies4u.mov`.

## Features
- Search for content by name.
- Handles multiple search results by presenting a choice to the user.
- Automates navigation through intermediate link protector pages.
- Uses SeleniumBase to bypass bot detection and retrieve final download links.
- Extracts and displays categorized download links directly in the terminal.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `seleniumbase`

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/og-adi/movies4u-bot.git
    ```

2.  Navigate into the project directory:
    ```sh
    cd movies4u-bot
    ```

3.  Install the required Python packages:
    ```sh
    pip install requests beautifulsoup4 seleniumbase
    ```

## Usage

1.  Run the script from your terminal:
    ```sh
    python main.py
    ```

2.  When prompted, enter the name of the movie or show you want to search for.
    ```
    Enter name to search: Interstellar
    ```

3.  If multiple results are found, a list will be displayed. Enter the number corresponding to your choice.
    ```
    2 Results found !

    1. Interstellar (2014) Full Movie [English DD5.1] 1080p 10bit HEVC BluRay ... - https://www.movies4u.mov/interstellar-2014-full-movie/
    2. Interstellar (2014) Dual Audio [Hindi+English] BluRay ... - https://www.movies4u.mov/interstellar-2014-dual-audio-hindienglish/

    Enter no. of choice: 1
    ```

4.  The script will then process the links and display the final download URLs.

## How It Works

1.  **Search:** The script takes a user query, constructs a search URL for `movies4u.mov`, and scrapes the results page using `requests` and `BeautifulSoup`.
2.  **Selection:** It displays the titles and links of the found content, allowing the user to select the correct one.
3.  **Link Extraction:** The script visits the selected movie's page and parses it to find the initial download link, which typically points to a `linkz.wiki` or `linkz.mom` page.
4.  **Bypass:** To access the final links, the script launches a browser instance using `SeleniumBase` with undetected-chromedriver (`uc=True`). this allows it to bypass JavaScript challenges and bot detection mechanisms.
5.  **Final Output:** Once on the final page, the script parses the HTML one last time to extract and print all available download links, which are often grouped by video quality.

## Disclaimer
This tool is intended for educational purposes only. The user is solely responsible for their actions and for complying with all applicable copyright laws. The developers of this tool do not condone piracy and are not responsible for any misuse of this software.
