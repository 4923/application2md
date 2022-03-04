# -*- coding: utf-8 -*-
# %%

import os
import glob
from converter import check_questions, df_to_md, load_data

# %%


def main():
    # Getting the current working directory.
    PATH_list: list = glob.glob(os.getcwd() + "/*.csv")

    # Loading the data from the csv file.
    applications = load_data(PATH_list)

    # 질문 확인
    questions, total_question_number = check_questions()

    # markdown 변환
    df_to_md(applications, questions, total_question_number)


# %%
if __name__ == "__main__":
    main()
