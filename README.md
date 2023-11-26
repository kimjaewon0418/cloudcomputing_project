## Cloud_Computing_Term_Project : Image Face Analyst

---
#### A.	프로젝트 명
  AWS Rekognition을 이용한 이미지 속 얼굴 분석
  
---
#### B.	프로젝트 멤버 이름 및 멤버 별로 담당한 파트에 대한 소개
  * 정의정 (20181725) : 자료조사, 보고서 작성, PPT
  * 김재원 (20195135) : 자료조사, 보고서 작성, 코드 작성, 발표

---
#### C.	프로젝트 소개 및 개발 내용 소개
  * 프로젝트 소개 : AWS S3 bucket을 생성하고 이미지를 저장해 Rekognition을 이용해 해당 이미지 속 얼굴을 분석한다. 
  * 개발 내용 소개 : AWS S3 bucket을 생성한다. 이미지 객체를 저장한다. Python boto3를 이용해 Rekognition detects_face를 작동시킨다. 출력된 분석 결과를 해석한다. 
  
---
#### D.	프로젝트 개발 결과물 소개 (+ 다이어그램)
  AWS S3 bucket을 생성한다. 이미지 객체를 저장한다. Python boto3를 이용해 Rekognition detects_face를 작동시킨다. 출력된 분석 결과를 해석한다.\
  <img src="https://user-images.githubusercontent.com/94631526/144223539-6e163c12-0e2b-4a44-95d2-26fce7814b85.png" width=500 height=300>

---
#### E.	개발 결과물을 사용하는 방법 소개 (+ 프로그램 구동 화면 스크린 샷 첨부)
  1. s3 버킷을 생성한다. \
    <img src="https://user-images.githubusercontent.com/94631526/144223542-f1913b5d-becc-493c-aa42-86c8593d0045.png" width=400 height=300>
  2. 생성한 버킷 안에 다운받은 이미지를 업로드 한다. 이미지는 각각 업로드 한다. \
    <img src="https://user-images.githubusercontent.com/94631526/144223537-4c3f6ea9-af65-4267-8711-0681c1715602.png" width=400 height=300>
  3. 다음과 같이 보이는 코드는 aws recognition 서비스 안에 있는 소스 코드를 가져와 수정한 것이다. 여러종류의 소스 코드들이 있었지만 python을 이용했다. Rekogniton을 사용하기 위해 boto3모듈을 가져오고  모듈과 Main 함수 부분에서 photo부분에 이름을 버킷안에 업로드한 이미지 이름으로 바꾸고 bucket은 s3 버킷에 생성한 이름을 적어준다. 그리고 이 프로그램을 실행시키기 위해선 이미지 파일 형식이 png 또는 jpg로 사용해야한다. \
     <img src="https://user-images.githubusercontent.com/94631526/144223534-be934709-c72c-4b37-b46e-2a953a14096c.PNG" width=500 height=600>
  4. 아래는 출력 결과이다. \
    <img src="https://user-images.githubusercontent.com/94631526/144223531-7762eca4-0fec-4d62-b82e-1d01d34d3348.png" width=300 height=600>
    <img src="https://user-images.githubusercontent.com/94631526/144223528-3b444eed-b6dd-40d5-a7bc-e5a25a3f9246.png" width=300 height=120>\
    <img src="https://user-images.githubusercontent.com/94631526/144223527-6806d521-8095-47f9-a90b-a183ab3dffeb.png" width=300 height=600>
    <img src="https://user-images.githubusercontent.com/94631526/144223545-a69c3667-4693-40b8-b21a-2862872040db.png" width=300 height=120>

---
#### F.	개발 결과물의 필요성 및 활용방안
  1. 사진 출력 서비스 : 원하는 분위기의 또는 가장 잘 나온 사진을 추천
  2. 온라인 데이팅 서비스 : 이상형에 가까운 얼굴 추천
  3. 리테일 비지니스 : 고객의 움직임, 손님의 기분등을 인식하여 비지니스에 활용
  4. 디지털 광고 : 개인화된 광고 제공
  5. 심리 검사 및 실험: 얼굴 분석을 통해 심리를 추측
