import urllib.request as request

def get_word():
	word = None
	try:
		req_obj = request.urlopen('Paste your URL here')
		word = req_obj.read().decode("UTF-8")
		word = word.strip()
	except Exception as e:
		print("Exception getting Random word", str(e))
	return word

if __name__ == '__main__':
	print(get_word())
