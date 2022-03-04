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
