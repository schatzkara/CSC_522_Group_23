import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


def make_page_urls(base_url, start_page, end_page):
	page_urls = []
	for i in range(start_page, end_page+1):
		page_urls.append(base_url + "&pageNumber=" + str(i))

	return page_urls


def get_soup(url):
	r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
	soup = BeautifulSoup(r.text, 'html.parser')

	return soup


def get_reviews(soup):
	review_list = []
	reviews = soup.find_all('div', {'data-hook': 'review'})
	try:
		for item in reviews:
			review = {
						'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').replace("Amazon.com: Customer reviews:", "").strip(),
						'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
						'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
						'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
					}
			review_list.append(review)
	except:
		pass

	return review_list


def last_page_of_reviews(soup):
	return soup.find('li', {'class': 'a-disabled a-last'}) or soup.find('h3', string="From other countries")


if __name__ == '__main__':
	base_urls = {
					1 : "https://www.amazon.com/elago-Compatible-Protective-Shockproof-Anti-Scratch/product-reviews/B09D339LSQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					2 : "https://www.amazon.com/Cordking-iPhone-11-Shockproof-Anti-Scratch/product-reviews/B091T37BN9/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					3 : "https://www.amazon.com/OTOFLY-iPhone-Pro-Max-Case/product-reviews/B09B2PW3NJ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					4 : "https://www.amazon.com/DEENAKIN-12-Pro-Max-Shockproof/product-reviews/B08T1DKXVT/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					5 : "https://www.amazon.com/JJGoo-Crystal-Compatible-Shockproof-Protective/product-reviews/B089NV5W1Z/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					6 : "https://www.amazon.com/JETech-Silky-Soft-Protective-Shockproof-Microfiber/product-reviews/B07QQZFZKJ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					7 : "https://www.amazon.com/KKM-Yellowing-Shockproof-Protective-Anti-Scratch/product-reviews/B0B254VD5Z/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					8 : "https://www.amazon.com/Teageo-iPhone-12-Pro-Max/product-reviews/B09MCJF7RT/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					9 : "https://www.amazon.com/BaHaHoues-S22-Kickstand-Shockproof-Protective/product-reviews/B0B11H5YXM/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					10 : "https://www.amazon.com/Hython-Full-body-Defender-Protective-Shockproof/product-reviews/B07KYC5847/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					11 : "https://www.amazon.com/MATEPROX-Glitter-Sparkle-Protective-Gradient/product-reviews/B075M9M7SS/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					12 : "https://www.amazon.com/OtterBox-Commuter-Case-iPhone-Pro/product-reviews/B08DY8GJN4/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					13 : "https://www.amazon.com/SPIDERCASE-Protector-Shockproof-Anti-Drop-Protective/product-reviews/B09DSVV1TC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					14 : "https://www.amazon.com/Caseative-Heart-Laser-Compatible-iPhone/product-reviews/B09HK8WJ4G/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					15 : "https://www.amazon.com/LucBuy-Gameboy-Protective-Self-Powered-Shockproof/product-reviews/B07VCQKYN3/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&all_reviews",
					16 : "https://www.amazon.com/Diverbox-Shockproof-Dropproof-Dust-Proof-Protection/product-reviews/B09M6VBTVF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					17 : "https://www.amazon.com/ZTOFERA-Pattern-Silicone-Lightweight-Protective/product-reviews/B08X4LVSZ1/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					18 : "https://www.amazon.com/AOTESIER-Compatible-Anti-Fingerprint-Full-Body-Protective/product-reviews/B08HQG7RBM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					19 : "https://www.amazon.com/TEAUGHT-Adjustable-Anti-Scratch-Shockproof-Protective/product-reviews/B096ZTMTZ9/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					20 : "https://www.amazon.com/MZELQ-Compatible-Strawberry-Protector-Protective/product-reviews/B0B87PYJFY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					21 : "https://www.amazon.com/LOVE-3000-Compatible-Anti-Scratch-Microfiber/product-reviews/B09MHMW4W7/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					22 : "https://www.amazon.com/MOZOTER-iPhone-13-Case-Anti-Yellowing/product-reviews/B0BLMG629Z/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&all_reviews",
					23 : "https://www.amazon.com/COOLQO-Compatible-Protector-Protective-Shockproof/product-reviews/B07YJMJ2VB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&all_reviews",
					24 : "https://www.amazon.com/Ownest-Compatible-Protective-Shockproof-11-Purple/product-reviews/B08CR3Y7ZF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&all_reviews",
					25 : "https://www.amazon.com/IceSword-iPhone-11-Silicone-Microfiber/product-reviews/B07XKY9H27/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					26 : "https://www.amazon.com/iPhone-MOSNOVO-Shockproof-Protective-Tulips/product-reviews/B0B1MXVZFY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					27 : "https://www.amazon.com/KUMTZO-Compatible-Leopard-Fashion-Protective/product-reviews/B099F8YJ3R/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&all_reviews",	
					28 : "https://www.amazon.com/ESR-iPhone-11-Shock-Absorbing-Scratch-Resistant/product-reviews/B07VK3Y6F8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					29 : "https://www.amazon.com/iCoverCase-Kickstand-Blocking-Embossed-Shockproof/product-reviews/B096S1P1NB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					30 : "https://www.amazon.com/CASEKOO-iPhone-13-Pro-Max/product-reviews/B0967K9PRZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",	
					31 : "https://www.amazon.com/ORNARTO-Compatible-Silicone-Covered-inch-Chalk/product-reviews/B09F3MNSTP/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					32 : "https://www.amazon.com/Chirano-iPhone-Corners-Shockproof-Protection/product-reviews/B07YSBNDBF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					33 : "https://www.amazon.com/SUBESKING-Pattern-Silicone-Shockproof-Protective/product-reviews/B08CBC99CZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					34 : "https://www.amazon.com/Idocolors-Ultra-Thin-Shockproof-Anti-Fall-Protective/product-reviews/B091SXMW4V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					35 : "https://www.amazon.com/Qokey-Compatible-Kickstand-Shockproof-Butterfly/product-reviews/B08XB6YPV6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					36 : "https://www.amazon.com/XUNQIAN-Compatible-Leopard-Tempered-Protective/product-reviews/B08ZMR2RTC/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					37 : "https://www.amazon.com/TORRAS-iPhone-14-Plus-Non-Yellowing/product-reviews/B0B5LJT8BR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					38 : "https://www.amazon.com/UniqueMe-iPhone-11-Shockproof-Protective/product-reviews/B09Y8VSYRD/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					39 : "https://www.amazon.com/Folosu-Compatible-360%C2%B0Rotation-Protective-Shockproof/product-reviews/B0B2W913BY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					40 : "https://www.amazon.com/FireNova-iPhone-14-Protection-Anti-Scratch/product-reviews/B0BGJ91959/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					41 : "https://www.amazon.com/Miracase-Silicone-Compatible-Protection-Shockproof/product-reviews/B07WRCDQJM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					42 : "https://www.amazon.com/Humixx-Ultra-Samsung-Galaxy-S23/product-reviews/B0BN5TPXWQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					43 : "https://www.amazon.com/Mkeke-iPhone-14-Yellowing-Shockproof/product-reviews/B0BB5HBHGN/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					44: "https://www.amazon.com/SUPCASE-Unicorn-Full-Body-Protector-Kickstand/product-reviews/B0B7MC26MS/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					45 : "https://www.amazon.com/Compatible-iPhone-12-Mini-Case/product-reviews/B08L931SLD/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					46 : "https://www.amazon.com/Military-Dropproof-Protector-Full-Body-Shockproof/product-reviews/B0B2J6GHM3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					47 : "https://www.amazon.com/TAURI-iPhone-Pro-Max-Non-Yellowing/product-reviews/B09N6VSP1F/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					48 : "https://www.amazon.com/TOMOTO-Compatible-Protection-Microfiber-Shockproof/product-reviews/B08J6D6V54/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					49 : "https://www.amazon.com/seacosmo-Shockproof-Protector-Lightweight-Protective/product-reviews/B09NPNNKN3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					50 : "https://www.amazon.com/Mgnaooi-Compatible-Translucent-Anti-Fingerprint-Anti-Scratch/product-reviews/B0B6VXF379/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					51 : "https://www.amazon.com/TAURI-Pro-Max-Not-Yellowing-Military-Grade/product-reviews/B0B5V19W21/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					52 : "https://www.amazon.com/Elando-Compatible-Non-Yellowing-Shockproof-Protective/product-reviews/B08RNNJN4P/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					53 : "https://www.amazon.com/Temdan-iPhone-14-Pro-Waterproof/product-reviews/B0B5TF9DPF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					54 : "https://www.amazon.com/Apple-Silicone-Case-MagSafe-iPhone/product-reviews/B08L5NS72V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
					55 : "https://www.amazon.com/ULAK-iPhone-11-Transparent-Anti-Scratch/product-reviews/B07X48BD6J/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
				}

	for i in base_urls.keys():
		my_base_url = base_urls[i]
		page_urls = make_page_urls(my_base_url, 1, 100)

		all_reviews = []
		count = 0
		for url in page_urls:
			my_soup = get_soup(url)
			reviews = get_reviews(my_soup)
			all_reviews.extend(reviews)
			count += 1
			# print(f'Scraped page {count} for {star} star reviews - {len(all_reviews)} total reviews for this product.')

			if last_page_of_reviews(my_soup):
				print(f'Last page of reviews: {count}.')
				break

		print(f'Scraped {len(all_reviews)} reviews over {count} pages for product {i}.')

		all_reviews_df = pd.DataFrame(all_reviews)
		all_reviews_df.to_excel(f'phone_case_reviews{i}_all_reviews.xlsx', index=False)
