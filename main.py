import requests

class bot:
    def __init__(self):
        self.username = input("1:")
        self.csrf = input('open inspect element > network tab > delete comment > click on delete comment event > go to payload > fetch the csrftoken')
        self.main()
    def main(self):
        while True: #it should crash print "[]" when done
            headers = {
                'sec-ch-ua-platform': '"Windows"',
                'Referer': f'https://www.reddit.com/user/{self.username}/comments/?sort=top',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'accept': 'text/vnd.reddit.partial+html, text/html;q=0.9',
                'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-ch-ua-mobile': '?0',
            }

            params = {
                'sort': 'top',
                't': 'ALL',
                'name': self.username,
                'feedLength': '58',
                'distance': '50',
            }

            response = requests.get(
                'https://www.reddit.com/svc/shreddit/profiles/profile_comments-more-posts/top/',
                params=params,
                headers=headers,
            )
            comments = []
            def extract(rawData):
                global comments
                import regex
                for line in rawData.split('\n'):
                    if len(line.split('comment-id='))>=2:
                        extractedComment = line.split('comment-id=')[1].replace('"','')
                        if extractedComment not in comments:
                            comments.append(extractedComment)
                    
            extract(response.text)
            print(comments)

            import requests

            cookies = {} # replace with the cookies you get from same spot ass other thing

            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://www.reddit.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }

            for comment in comments:
                json_data = {
                    'operation': 'DeleteComment',
                    'variables': {
                        'input': {
                            'commentId': comment,
                        },
                    },
                    'csrf_token': self.csrf,
                }

                response = requests.post('https://www.reddit.com/svc/shreddit/graphql', cookies=cookies, headers=headers, json=json_data)
                print(response.json())

bot()
