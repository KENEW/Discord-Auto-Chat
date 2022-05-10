# Discord-Auto-Chat

<img src="https://img.shields.io/badge/Python-3.8-blue">


디스코드 서버에서 채팅을 자동으로 입력해줍니다.

## 주의 (Warning!)
- 디스코드 Auth Key와 같은 예민한 요소를 다룹니다. 사용할 시 필히 주의 바랍니다.
- 공개된 서버에서 과도한 사용(챗굴, 테러) 등을 금합니다.

## 주요 기능
- 미리 입력된 문자열을 채널 내에서 보내준다. (순서, 랜덤)
- (제작 예정) 제한된 문자 중 자연스럽게 문자를 만들어준다.
- (제작 예정) 채팅 딜레이 내에서 마지막으로 검색된 단어가 나오면 답장 기능과 함께 문자열을 보내준다

## 환경 설정
- 프로젝트 파일내에서 .env 생성 후 다음과 같이 입력

```
Discord_Auth_Token = ''
Chanel_End_Point = ''

Chat_Max_Time = 
Chat_Min_Time = 
```
