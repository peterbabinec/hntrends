from hackernews import HackerNews

hn = HackerNews()

top_story_ids = hn.top_stories()
print(top_story_ids);