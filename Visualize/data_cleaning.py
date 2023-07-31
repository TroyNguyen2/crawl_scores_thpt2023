from __future__ import annotations
import pandas as pd
import re

def main():
    
    # Optimize section
    pattern_dict = {
    "math_pattern" :r"\bToán:\s + (\d+\.\d+)\b",           #1 
    "literature_pattern":r"\bNgữ văn:\s + (\d+\.\d+)\b",   #2 
    "chemical_pattern":r"\bHóa học:\s + (\d+\.\d+)\b",     #3
    "physic_pattern" :r"\bVật lí:\s + (\d+\.\d+)\b",       #4
    "biology_pattern":r"\bSinh học:\s + (\d+\.\d+)\b",     #5
    "history_pattern":r"\bLịch sử:\s + (\d+\.\d+)\b",      #6
    "geo_pattern"   :r"\bĐịa lí:\s + (\d+\.\d+)\b",        #7
    "GDCD_pattern"  :r"\bGDCD:\s + (\d+\.\d+)\b",          #8
    "english_pattern":r"\bTiếng Anh:\s + (\d+\.\d+)\b",    #9
    "KHXH_pattern"  :r"\bKHXH:\s+(\d+\.\d+)\b",            #10   
    "KHTN_pattern"  :r"\bKHTN:\s+(\d+\.\d+)\b",            #11
    }

    df = pd.read_csv(r'.\crawl_data_thpt2023\thpt2023.csv')
    score_list = df['Score']
    id_list = df['ID']

    columns=['ID','Toán','Ngữ Văn','Hóa Học','Vật lí','Sinh học','Lịch sử','Địa lí','GDCD','Tiếng Anh','KHXH','KHTN']
    # Create 2 dataframes
    new_df = pd.DataFrame(columns=columns)
    add_value = pd.DataFrame(columns=columns)


    for i in range(1,df.shape[0]):
        add_value = [id_list[i]]

        for pattern in pattern_dict.values():
            try:
                score_value = re.findall(pattern,score_list[i])[0]
                add_value.append(score_value)
            except: add_value.append(0)
        new_df.loc[len(new_df.index)] = add_value
    # Output
    new_df.to_csv(r'crawl_data_thpt2023\Visualize\thpt_clean.csv', encoding='utf16',index=False)
if __name__ == "__main__":
    main()