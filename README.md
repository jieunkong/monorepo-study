# backend-monorepo

본 프로젝트는 FastAPI Web Frameworks를 기반으로 한 백앤드 Monorepo 입니다.

## 1. Backend Monorepo 폴더 구조
|폴더 구조|폴더 설명|
|---|---|
backend-monorepo
├─ common
│   ├─ base|공통으로 상속받아 사용하는 class 정의
│   ├─ const|공통으로 사용하는 const string이나 enum 정의
│   ├─ db|공통으로 사용하는 DB 정의
│   ├─ depends|공통으로 사용하는 FastAPI dependency 정의
│   ├─ mappers|Service와 Model을 연결하는 공통 Mapper 정의
│   ├─ middleware|공통으로 사용하는 Middleware 정의
│   ├─ models|공통으로 사용하는 Model 정의
│   ├─ schemas|공통으로 사용하는 Schema 정의
│   ├─ services|공통으로 사용하는 비즈니스 로직을 구현하는 Service 정의
│   ├─ tests|공통으로 사용하는 컴포넌트 테스트
│   └─ utils|공통으로 사용하는 유틸리티
├─ data|생성된 데이터를 저장 폴더
│   ├─ logs|log file 저장 폴더
│   ├─ files|upload된 file 저장 폴더
│   ├─ pgadmin|postgresql admin ui 데이터 폴더
│   ├─ pgdata|postgresql database 폴더
│   └─ vscode-server|remote-container에 설치된 vscode extenstion 폴더
├─ product
│   ├─ sample
│   │   ├─ app|app 이 최초 실행시 작업해야 할 내용을 정의
│   │   │   ├─ models|DB table
│   │   │   ├─ mappers|Service와 Model을 연결하는 Mapper
│   │   │   ├─ routers|request에서 데이터 처리
│   │   │   │   └─ v1|API 버전 관리
│   │   │   ├─ schemas|Data serialize
│   │   │   └─ services|비즈니스 로직을 처리
│   │   ├─ config|설정
│   │   ├─ core|제품별 사이트에 종속적이지 않은 데이터 정의
│   │   │   ├─ const|const string이나 enum 정의
│   │   │   ├─ depends|FastAPI dependency 정의
│   │   │   └─ middleware|FastAPI middleware 정의
│   │   ├─ docker|개발환경
│   │   ├─ etc|각종 추가적인 내용
│   │   │   ├─ database|db와 관련된 script
│   │   │   └─ pgconfig|postgresql 과 관련된 config 파일
│   │   ├─ templates|Jinja2 templates
│   │   ├─ tests
│   │   └─ main.py
├─ README.md
└─ requirements.txt|vuno-product에서 사용하는 모든 python library
