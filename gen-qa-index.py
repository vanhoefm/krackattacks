#!/usr/bin/env python2
from bs4 import BeautifulSoup

def main():
	soup = BeautifulSoup(open("index.html"), "html.parser")
	faq = soup.find("a", {"name": "faq"})
	faq_titles = faq.find_next_siblings("h3")
	faq_anchors = faq.find_next_siblings("a")
	assert len(faq_titles) == len(faq_anchors)

	print "<ul>"
	for title, anchor in zip(faq_titles, faq_anchors):
		print '\t<li><a href="#{anchor}">{title}</a></li>'.format(title=title.text, anchor=anchor["name"])
	print "</ul>"


if __name__ == "__main__":
	main()

