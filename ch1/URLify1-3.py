
def urlify(url):
	return "%20".join(url.split())


if __name__ == '__main__':
	assert urlify("Mr John Smith") == "Mr%20John%20Smith"

