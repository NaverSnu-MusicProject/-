# MTM API 명세

## 요약
* mtm은 네이버 뮤직으로 부터 제공받은 음악 데이터 및 재생 기록을 기반으로 하여 특정 장소에 알맞은 음악을 추천하는 서비스 입니다.
* 본 문서는 mtm을 HTTP요청으로 활용할 수 있는 REST API와 상세 설명을 포함합니다.

## 개발환경 구성
* REST API는 HTTP 요청을 보낼 수 있는 환경이라면 어디에서든 이용할 수 있습니다. 다음은 REST API를 활용할 수 있는 환경의 예입니다.
> 모바일/PC 웹 환경에서 Javascript를 활용
> 다양한 환경(Java, Ruby, Python 등)의 웹 서버에서 활용
> iOS, Android 등 다양한 모바일 환경에서 활용

## MTM API 상세기능
### MTM curation API
  * method :GET
  * 인증 : -
  * 요청 URL: "http://wlxyzlw.iptime.org:8008/"+[행정주소]+"/proposal"
  * 출력 포맷 : JSON/XML
  * 설명 : 요청한 장소에 어울리는 추천 음악리스트 및 태그, 아티스트 등을 가져옴
  * 요청 변수: place
  * 타입 : 다차원 배열(2차~3차)
  * 필수 여부 : Y
  * 기본값 : utf-8
  * 설명 : 검색할 주소의 동 단위 주소로, 띄어쓰기를 포함하지 않는다. ex) 서울특별시관악구신림동
  * 출력 결과 : 해당 행정주소에서의 추천 메타 정보를 가져온다.
> [ 상위 순위 태그, 상위 순위 음악, 관련 아티스트 랜덤, 관련 앨범 랜덤 ]
> 태그 = 태그 이름(string), size = 10
> 음악 = [ 음악 이름(string), 타이틀 곡 여부(bool), 수록 앨범 이름(string) ], size = 10
> 아티스트 = [ 아티스트 이름(string), 아티스트 성별(bool), 인기도(string)], size = 5
> 앨범 = 앨범 이름(string), size = 5

  * 에러 코드
>   __400__
>   __403__

* 예시 코드
> function API_example(){
>   var URL = "http://wlxyzlw.iptime.org:8008/address/서울특별시관악구신림동/proposal/";
>   var xmlhttp = new XMLHttpRequest();
>   xmlhttp.onreadystatechange = function(){
>     if(this.readyState == 4 && this.status == 200){
>       var obj = JSON.parse(this.responseText);>
>       /*Do Something*/
>     }
>   }
>   xmlhttp.open("GET", URL, true);
>   xmlhttp.send();
> }
