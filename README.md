# MyNike (nike_clone)

나이키 공식사이트 클론 <br>
Flask 서버에서 페이지 이동, 검색, 장바구니 만드는 것을 목표로 시작한 프로젝트

- 제작기간 : 2020.10.31 ~ 2020.11.01

<br>

## 소개

![나이키1](https://user-images.githubusercontent.com/72585287/116178973-6c886600-a751-11eb-977e-d6a0603ae188.png)
![나이키2](https://user-images.githubusercontent.com/72585287/116178980-701bed00-a751-11eb-9377-2395b5c5ced4.png)
(사이트에 이용한 사진 출처 - 나이키 공식홈페이지)

<br>


## 📖 API 설계
| 목적 | API주소 (요청방법) | 서버 |클라이언트|
|:----------:|:----------:|:----------:|:---------:|
| 상품 불러오기 | `/api/home`<br>(GET)| 전체 collection에서 상품 리스트를 불러온다 | 상품들로 카드를 만든다 |
| 카트 불러오기 | `/api/cart`<br>(GET) | 카트 collection에서 상품 리스트를 불러온다 | 상품들로 카드를 만든다 |
| 카트에 저장하기 | `/api/cart`<br>(POST) | 해당 상품을 카트 collection에 저장한다 | 장바구니 버튼 눌린 상품의 이름을 전달한다 |
| 카트에서 삭제하기 | `/api/cart/del`<br>(POST) | 해당 상품을 카트 collection에서 삭제한다 | 삭제 버튼 눌린 상품의 이름을 전달한다 |
| 검색하기 | `/api/search`<br>(POST) | 전달된 검색어가 포함된 상품을 전체 collection에서 찾아 검색결과 collection에 저장한다  | 검색창에 입력한 값을 전달한다 |
| 검색결과 보여주기 | `/api/search`<br>(GET) | 검색결과 collection에서 상품 리스트를 불러온다 | 상품들로 카드를 만든다 |
