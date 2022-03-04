# %%
# Convert spread sheet (csv or excel) into markdown

import pandas as pd
import re


# %%

def load_data(PATH_list: list) -> pd.DataFrame:
    df = pd.DataFrame()
    for PATH in PATH_list:
        df = pd.concat([df, pd.read_csv(PATH)])

    print(f"총 {len(df)} 명의 지원자가 지원했습니다.")
    return df

# %%

# 파일명에 / 포함되어 파일 생성 에러 생기는 것 방지


def clean_text(text: str):
    special = re.compile(r'[^A-Za-z0-9가-힣+]')
    result = special.sub('', text)
    return result

# %%


def check_questions():
    # 공통문항 변경하여 사용 시 하단 dictionary 수정
    questions: dict = {
        'q_name': '지원자 성함을 입력해 주세요.',
        'q_major': '지원자의 소속 학과를 입력해 주세요.',
        'q_track': '2. 멋쟁이사자처럼 대학 10기부터 기초 개발 스터디는 동일하게 진행되지만 이후에 기획/디자인 파트와 개발 파트 중 선택하여 진행하게 됩니다. 어느 파트에 지원하시나요? ① 기획/디자인 파트② 개발 파트(프론트엔드, 백엔드)',

        'q_no1': '1. 다양한 IT동아리 중에서 멋쟁이사자처럼 대학 10기를 선택하고 지원하시게 된 이유를 작성해주세요. (500자 이내)',
        'q_no2': '2-1. 위의 파트를 선택한 이유와 관련 경험을 해본 적이 있는지, 그리고 이 파트를 통해 어떠한 성장을 희망하시는지 작성해주세요. (500자 이내)',
        'q_no3': '3. 멋쟁이사자처럼 대학은 협업과 팀워크를 중요한 가치로 생각하는 공동체입니다. 지원자 본인이 협업과 팀워크를 진행해보았던 경험과, 그 경험을 멋쟁이 사자처럼 대학에서 어떻게 적용시킬 수 있을지 작성해주세요. (500자 이내)',
        'q_no4': '4. 멋쟁이사자처럼 대학은 최소 주 2회 모임 & 10시간 이상의 시간 투자를 권장합니다. 활동 기간동안 얼마나 열정적으로, 매주 얼만큼의 시간을 할애하실 수 있는지 작성해주세요. (500자 이내)'
    }

    print(f"""다음은 공통 문항입니다. 잘못 기입된 항목이 있다면 변경해주세요. (./converter.py)
    지원자 성명 : {questions['q_name']}
    지원자 전공 : {questions['q_major']}
    지원 트랙 : {questions['q_track']}

    1번 문항 : {questions['q_no1']}
    2번 문항 : {questions['q_no2']}
    3번 문항 : {questions['q_no3']}
    4번 문항 : {questions['q_no4']}
    \n""")

    # 포트폴리오 확인
    is_portfolio = input("포트폴리오를 받는 항목이 있다면 질문을 입력해주세요. 없다면 N을 입력하세요: ")
    if is_portfolio != 'N':
        questions['portfolio'] = is_portfolio

    # 그 외 학교 개별문항 추가
    is_more = input("학교별 개별 문항이 있다면 yes 없다면 N를 입력하세요: ")
    idx_more = 0
    while is_more == 'yes':
        idx_more += 1
        question_more = input(f"{4+idx_more}번 문항을 입력하세요 (중단: N): ")
        if question_more != 'N':
            questions[f"q_no{4+idx_more}"] = question_more
        else:
            is_more = "N"
            print("학교별 개별문항 입력을 종료합니다.")

    # 총 문항 개수
    total_question_number: int = 4 + idx_more
    return questions, total_question_number

# %%


def df_to_md(df: pd.DataFrame, questions: dict, total_question_number):
    for idx in range(len(df)):
        # 지원서
        candidate: pd.DataFrame = df.loc[idx]

        # 주요 항목
        name = clean_text(candidate[questions['q_name']])
        major = clean_text(candidate[questions['q_major']])
        track = clean_text(candidate[questions['q_track']])

        # 포트폴리오 항목이 없을경우 예외처리
        try:
            portfolio = candidate[questions['portfolio']]
        except:
            portfolio = ''

        timestamp, email, phone,  = candidate[0], candidate[1], candidate[3]
        file_name = f"{name}_{major}_{track}"

        # markdown 파일 생성
        f = open(f'./application/{track}/{file_name}.md', 'w+')   # 파일명
        f.write(f"# {file_name}\n\n")     # h1
        # 지원자 정보
        f.write(
            f"|email|phone|portfolio|timestamp\n|:-|:-|:-|:-|\n|{email}|{phone}|{portfolio}|{timestamp}|\n\n")

        # 문항 및 답변
        f.write("---\n")
        for q_no in range(1, total_question_number):
            f.write(
                f"## {questions[f'q_no{q_no}']}\n{candidate[questions[f'q_no{q_no}']]}\n\n")
        print(f"[Success] {file_name}.md 생성 완료")
        f.close()

    return
