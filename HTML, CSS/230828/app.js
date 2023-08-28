console.log("connect")
const BASEURL = 'http://test.api.weniv.co.kr/'

const mainContainer = document.getElementById("main");

function createProductCard(imgUrl, productName, price, onClick) {
	const $productCard = document.createElement('div');
	const $productName = document.createElement('strong');
	const $price = document.createElement('span');
	const $thumbnailImg = document.createElement('img');

	$productName.innerText = productName;
	$price.innerText = price + '원';
	$thumbnailImg.src = imgUrl;
	$productCard.append($productName, $price);
	$productCard.addEventListener("click", onClick);

	return $productCard;
}

function createProductDetail(imgUrl) {
	const $productDetail = document.createElement("img");
	$productDetail.src = imgUrl;
	return $productDetail;
}

async function main() {
	const productsContainer = document.createElement("div");
	productsContainer.id = "products";
	const detailContainer = document.createElement("div");
	detailContainer.id = "detail";
	mainContainer.appendChild(productsContainer);
	mainContainer.appendChild(detailContainer);
	

	const res = await fetch(BASEURL + "mall")
	const json = await res.json();
			
	console.log(json);
	json.forEach(data => {
		const productId = data.id;
		const productImgUrl = BASEURL + data.thumbnailImg;
		const productName = data.productName;
		const price = data.price;
		const onClick = async (e) => {
			detailContainer.innerHTML = "";
			const res = await fetch(BASEURL + "mall/" + productId);
			const json = await res.json();
			json.detailInfoImage.forEach(imgUrl => {
				const detailImgUrl = BASEURL + imgUrl;
				const $productDetail = createProductDetail(detailImgUrl);
				detailContainer.appendChild($productDetail);
			})
		}
		const $productCard = createProductCard(productImgUrl, productName, price, onClick)
		productsContainer.appendChild($productCard);
	})
};

main();
