headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

import requests

def count_words(subreddit, word_list, after=None, count=None):
    if after is None:
        after = ""
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, params={'after': after}, allow_redirects=False, headers={'User-Agent': 'YourUserAgent'})

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for i, keyword in enumerate(word_list):
                keyword_count = title.count(keyword.lower())
                count[i] += keyword_count

        after = data['data']['after']
        if after is None:
            combined_counts = {}
            for word, c in zip(word_list, count):
                word = word.lower()
                if word not in combined_counts:
                    combined_counts[word] = c
                else:
                    combined_counts[word] += c

            sorted_counts = sorted(combined_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, c in sorted_counts:
                print(f"{word}: {c}")
        else:
            count_words(subreddit, word_list, after, count)

# Example usage
subreddit = "unpopular"
word_list = ["you", "unpopular", "vote", "down", "downvote", "her", "politics"]

count_words(subreddit, word_list)

