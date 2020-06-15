from wordcloud import WordCloud
def freqGen(direct):
	f = open(direct)
	text = f.read()
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
	for letter in text:
		if letter in punctuations:
			text.replace(letter,"")
	freq = {}
	words = text.split(" ")
	for word in words:
		if word not in uninteresting_words:
			if word in freq:
				freq[word] += 1
			else:
				freq[word] = 1
	cloud = WordCloud()
	cloud.generate_from_frequencies(freq)
	cloud.to_file("wordCloud.jpg")
	return "File created at home directory with name \'wordCloud.jpg\'"