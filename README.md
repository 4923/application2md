# 지원서 마크다운 변환

한국외국어대학교 글로벌캠퍼스 멋쟁이사자처럼 10기 지원서 관리를 위해 제작했습니다.

# requirements

```
python == 3.8
pandas == 1.4.1
```

## How to Use

1. 본 repository를 clone
2. dependency

```
pip install -r requirements.txt
```

3. repo 경로로 이동 후 `python main.py` 실행
4. 다운로드 받은 스프레드시트 절대경로를 입력
5. 포트폴리오가 있을 경우 포트폴리오를 받는 항목 질문을 입력

   - 예) 6. 그 외 포트폴리오가 있으시면 제출해주십시오. Github가 있으시면 Github링크 남겨주시고, 그 외 포트폴리오는 hufsglobal@likelion.org 메일로 보내주시기 바랍니다. (선택사항)

6. 학교별 개별 문항이 있다면 `yes` 입력 후 질문을 추가하세요. 중단하고 싶다면 `N` 을 입력하시면 됩니다.
