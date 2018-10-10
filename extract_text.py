from goose3 import Goose

g = Goose()
def get_text_from_url(news_url):
		text = ' '
		try:
			article = g.extract(url=news_url)
			return article.cleaned_text
		except Exception:
			text = ''
			title = ''
			publish_date = ''
			meta_Description = ''
			title = ''
		return title, text, publish_date, meta_Description