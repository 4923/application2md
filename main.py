# -*- coding: utf-8 -*-
# %%

from converter import check_questions, df_to_md, load_data

# %%


def main():
    # csv/excel 로드 -> glob로 그냥 알아서 경로 찾도록 하는게 나을듯
    PATH: str = input("csv 파일이 위치한 경로를 입력하세요: ")
    df = load_data(PATH)
    print(type(df))
    # 질문 확인
    questions, total_question_number = check_questions()

    # markdown 변환
    df_to_md(df, questions, total_question_number)


# %%
if __name__ == "__main__":
    main()


# /Users/a4923/Desktop/repositories/application2md/10기 선발 스프레드 시트 - 지원서 현황.csv
# 6. 그 외 포트폴리오가 있으시면 제출해주십시오. Github가 있으시면 Github링크 남겨주시고, 그 외 포트폴리오는 hufsglobal@likelion.org 메일로 보내주시기 바랍니다. (선택사항)
# 5. 본인이 사용했던 웹서비스 중 좋았던 것과 아니었던 것을 적고 그 이유를 적으시오.(500자 이내)
