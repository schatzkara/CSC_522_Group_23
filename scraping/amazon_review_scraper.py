import requests
from bs4 import BeautifulSoup
import pandas as pd


def make_page_urls(base_url, start_page, end_page):
	page_urls = []
	for i in range(start_page, end_page+1):
		page_urls.append(base_url + str(i))

	return page_urls


def get_proxy():
	proxy = None
	
	return proxy


def get_soup(url):
	r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
	soup = BeautifulSoup(r.text, 'html.parser')

	print(soup.title.text)
	# input()

	return soup


def get_reviews(soup):
	review_list = []
	reviews = soup.find_all('div', {'data-hook': 'review'})
	try:
		for item in reviews:
			review = {
						'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
						'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
						'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
						'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
					}
			review_list.append(review)
	except:
		pass

	return review_list


if __name__ == '__main__':
	base_urls = [
					"https://www.amazon.com/elago-Compatible-Protective-Shockproof-Anti-Scratch/product-reviews/B09D339LSQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/Cordking-iPhone-11-Shockproof-Anti-Scratch/product-reviews/B091T37BN9/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/OTOFLY-iPhone-Pro-Max-Case/product-reviews/B09B2PW3NJ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/DEENAKIN-iPhone-12-Pro-Shockproof/product-reviews/B0946RP7J5/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/JJGoo-Crystal-Compatible-Shockproof-Protective/product-reviews/B089NV5W1Z/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/JETech-iPhone-6-1-Inch-Shockproof-Anti-Scratch/product-reviews/B07QQZD49D/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/KKM-Yellowing-Shockproof-Protective-Anti-Scratch/product-reviews/B0B254VD5Z/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/Teageo-Compatible-iPhone-11-Love-Heart/product-reviews/B0B65CT662/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/BaHaHoues-S22-Kickstand-Shockproof-Protective/product-reviews/B0B11H5YXM/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/Hython-Full-body-Defender-Protective-Shockproof/product-reviews/B07KYC5847/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/MATEPROX-Anti-Yellow-Anti-Slippery-Anti-Scratches-Shockproof/product-reviews/B07H3K4V3P/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/OtterBox-Commuter-Case-iPhone-Pro/product-reviews/B08DY8GJN4/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/SPIDERCASE-Protector-Shockproof-Anti-Drop-Protective/product-reviews/B09DSVV1TC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/Caseative-Heart-Laser-Compatible-iPhone/product-reviews/B09HK8WJ4G/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					"https://www.amazon.com/LucBuy-Gameboy-Protective-Self-Powered-Shockproof/product-reviews/B07VCQKYN3/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
					# "https://www.amazon.com/KUMTZO-Compatible-Leopard-Fashion-Protective/product-reviews/B099F8YJ3R/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
				]
	my_base_url = base_urls[-1]

	page_urls = make_page_urls(my_base_url, 1, 10)

	all_reviews = []
	count = 0
	for url in page_urls:
		soup = get_soup(url)
		reviews = get_reviews(soup)
		all_reviews.extend(reviews)
		print(len(all_reviews))

		count += 1
		print(f'Scraped page {count}')

		if not soup.find('li', {'class': 'a-disabled a-last'}):
			pass
		else:
			break

	all_reviews_df = pd.DataFrame(all_reviews)
	all_reviews_df.to_excel(f'phone_case_reviews{len(base_urls)}.xlsx', index=False)
	print('Done!')

