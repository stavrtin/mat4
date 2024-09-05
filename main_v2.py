import datetime

import pandas as pd
import numpy as np

def calc():
    # Use a breakpoint in the code line below to debug your script.

    # In[1155]:

    df_genius = pd.read_csv('./data_files/EventList.csv', delimiter=',')
    df_radar = pd.read_csv('./data_files/Live-Calendar.csv', delimiter=';', encoding='cp1251')
    df_raning = pd.read_excel('./data_files/rf.xls')
    # df_rts = pd.read_excel('RTS.xls')

    # In[1156]:

    print(f'{df_genius.shape=}')
    print(f'{df_radar.shape=}')
    print(f'{df_raning.shape=}')

    # print(f'{df_rts.shape=}')

    # In[1157]:

    def age_u_xx(df_, u_xx):
        df_.loc[
            (df_['com1'].str.contains(u_xx) == True)
            , 'liga'] = u_xx
        df_.loc[
            (df_['com1'].str.contains(u_xx) == True)
            , 'com1'] = df_['com1'].str.split(u_xx).str[0]

        df_.loc[
            (df_['com2'].str.contains(u_xx) == True)
            , 'com2'] = df_['com2'].str.split(u_xx).str[0]
        return df_

    # In[1158]:

    def woman_(df_):
        df_.loc[
            (df_['com1'].str.contains('women') == True)
            , 'liga'] = df_['liga'] + '-' + 'women'
        df_.loc[
            (df_['com1'].str.contains('women') == True)
            , 'com1'] = df_['com1'].str.replace('women', '')

        df_.loc[
            (df_['com2'].str.contains('women') == True)
            , 'com2'] = df_['com2'].str.replace('women', '')
        return df_

    # In[ ]:

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>готовлю генус

    # In[1159]:

    df_genius['liga'] = ''

    # In[1160]:

    df_genius = df_genius[['Competition',
                           # 'EventId',
                           'Event', 'Start (UTC+3)', 'Feed',
                           # 'Booking Status',
                           'liga'
                           ]]

    # In[1161]:

    df_genius.rename(columns={'Feed': '_genius'}, inplace=True)

    # In[1162]:

    df_genius = df_genius[~df_genius['Competition'].str.contains('\[Test]')]

    # In[1163]:

    df_genius['com1'] = df_genius['Event'].str.lower().str.split(' v ').str[0]
    df_genius['com2'] = df_genius['Event'].str.lower().str.split(' v ').str[1]

    # In[1164]:

    # ------------------------------------------- liga
    df_genius = age_u_xx(df_genius, 'u18')
    df_genius = age_u_xx(df_genius, 'u19')
    df_genius = age_u_xx(df_genius, 'u20')
    df_genius = age_u_xx(df_genius, 'u21')

    # In[1165]:

    # -------------------------------- woman
    df_genius = woman_(df_genius)

    # In[1166]:

    df_genius['Start (UTC+3)'] = pd.to_datetime(df_genius['Start (UTC+3)'], dayfirst=False, errors='coerce').dt.normalize()
    print(df_genius['Start (UTC+3)'])
    # In[1167]:

    # ----------------------------- (   ) ------ ..
    df_genius['com1'] = df_genius['com1'].str.replace('(', '').str.replace(')', '')
    df_genius['com2'] = df_genius['com2'].str.replace('(', '').str.replace(')', '')

    df_genius['com1'] = df_genius['com1'].str.replace('.', '')
    df_genius['com2'] = df_genius['com2'].str.replace('.', '')

    # In[ ]:

    # In[1168]:

    # ------------------------

    # In[1169]:

    # atlético
    # de
    # sk benešov
    # ý
    # brøndby if

    # In[1170]:

    df_genius['com1'] = df_genius['com1'].str.replace('é', 'e')
    df_genius['com2'] = df_genius['com2'].str.replace('é', 'e')

    df_genius['com1'] = df_genius['com1'].str.replace(' de ', '')
    df_genius['com2'] = df_genius['com2'].str.replace(' de ', '')

    # In[ ]:

    # In[ ]:

    # In[1171]:

    df_genius['key'] = df_genius['Start (UTC+3)'].astype(str) + '-' + df_genius['com1'] + '-' + df_genius[
        'com2'] + '-' + df_genius['liga']
    df_genius['key'] = df_genius['key'].str.replace(' ', '')
    df_genius['key'] = df_genius['key'].str.replace('--', '-')

    # In[1172]:

    # df_genius

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>готовлю df_raning

    # In[1173]:

    # --------------------------- df_raning------------

    # In[1174]:

    # df_raning = pd.read_excel('rf.xls')

    # In[1175]:

    df_raning['liga'] = ''

    # In[1176]:

    df_raning.rename(columns={'Coverage': '_raning'}, inplace=True)

    # In[1177]:

    df_raning['com1'] = df_raning['Competitor 1'].str.lower()
    df_raning['com2'] = df_raning['Competitor 2'].str.lower()

    # In[1178]:

    df_raning = df_raning[[
        # 'Country',
        'Competition',
        # 'Venue', 'Neutral Venue',
        'Team Advantage',
        'Game Start Time', 'com1', 'com2',
        '_raning',
        # 'PlayState', 'Competitor ID 1', 'Competitor ID 2'
        'liga'
    ]]

    # In[1179]:

    df_raning = age_u_xx(df_raning, 'u18')
    df_raning = age_u_xx(df_raning, 'u19')
    df_raning = age_u_xx(df_raning, 'u20')
    df_raning = age_u_xx(df_raning, 'u21')

    # In[1180]:

    # -------------------------------- woman
    df_raning = woman_(df_raning)

    # In[1181]:

    df_raning['Game Start Time'] = pd.to_datetime(df_raning['Game Start Time'], dayfirst=True,
                                                  errors='coerce').dt.normalize()

    # In[1182]:

    # ----------------------------- (   ) ------ ..
    df_raning['com1'] = df_raning['com1'].str.replace('(', '').str.replace(')', '')
    df_raning['com2'] = df_raning['com2'].str.replace('(', '').str.replace(')', '')

    df_raning['com1'] = df_raning['com1'].str.replace('.', '')
    df_raning['com2'] = df_raning['com2'].str.replace('.', '')

    # In[1183]:

    df_raning['key'] = df_raning['Game Start Time'].astype(str) + '-' + df_raning['com1'] + '-' + df_raning[
        'com2'] + '-' + df_raning['liga']
    df_raning['key'] = df_raning['key'].str.replace(' ', '')
    df_raning['key'] = df_raning['key'].str.replace('--', '-')

    # In[1184]:

    df_raning

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>готовлю df_radar

    # In[1185]:

    def liga_radar(df_, u_xx):
        df_['Tournament'] = df_['Tournament'].str.lower()
        df_.loc[
            (df_['Tournament'].str.contains(u_xx) == True)
            , 'liga'] = u_xx

        return df_

    # In[1186]:

    def liga_woman(df_):
        df_['Tournament'] = df_['Tournament'].str.lower()
        df_.loc[
            (df_['Tournament'].str.contains('women') == True)
            , 'liga'] = df_['liga'] + '-' + 'women'

        return df_

    # In[1187]:

    # /-------------------------------------------df_radar

    # In[1188]:

    # df_radar = pd.read_csv('Live-Calendar.csv', delimiter=';', encoding='cp1251')

    # In[1189]:

    df_radar['liga'] = ''

    # In[1190]:

    df_radar.rename(columns={'Covered from': '_radar'}, inplace=True)

    # In[1191]:

    df_radar = df_radar[[
        # 'EventId', 'Day',
        'Date',
        # 'Time', 'Sport',
        'Category', 'Tournament',
        'Event',
        # 'Court',
        # 'Stream',
        '_radar',
        # 'Covered with LO',
        #    'Covered with LScout',
        'liga'
    ]]

    # In[1192]:

    df_radar['com1'] = df_radar['Event'].str.lower().str.split(' vs. ').str[0]
    df_radar['com2'] = df_radar['Event'].str.lower().str.split(' vs. ').str[1]

    # In[ ]:

    # In[1193]:

    df_radar = liga_radar(df_radar, 'u18')
    df_radar = liga_radar(df_radar, 'u19')
    df_radar = liga_radar(df_radar, 'u20')
    df_radar = liga_radar(df_radar, 'u21')
    df_radar = liga_woman(df_radar)

    # In[1194]:

    df_radar['Date'] = pd.to_datetime(df_radar['Date'], dayfirst=True, errors='coerce').dt.normalize()

    # In[1195]:

    df_radar['key'] = df_radar['Date'].astype(str) + '-' + df_radar['com1'] + '-' + df_radar['com2'] + '-' + df_radar[
        'liga']
    df_radar['key'] = df_radar['key'].str.replace(' ', '')
    df_radar['key'] = df_radar['key'].str.replace('--', '-')

    # In[1196]:

    df_radar

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>джойним к генус

    # In[1201]:

    df_genius_m = df_genius.merge(df_raning[['key', 'com1', 'com2', 'liga', '_raning']], on='key',
                                  suffixes=['_gen', '_ran'], how='left').merge(
        df_radar[['key', 'com1', 'com2', 'liga', '_radar']], on='key', suffixes=['_rad'], how='left')
    df_genius_m

    # In[1202]:

    # df_genius_m[~df_genius_m['_raning'].isna()]

    # In[ ]:

    # In[ ]:

    # In[1203]:

    df_genius_m = df_genius_m[[
        'com1_gen', 'com2_gen',
        # 'Event',
        '_genius',
        '_raning',
        '_radar', 'key',
        'liga_gen',
    ]]
    df_genius_m

    # In[1204]:

    df_genius_m.rename(columns=({'com1_gen': 'com1',
                                 'com2_gen': 'com2',
                                 'liga_gen': 'liga',
                                 }), inplace=True)
    df_genius_m

    # In[1205]:

    df_genius_m['источник'] = 'geniu'

    # In[1206]:

    df_genius_m

    # In[1207]:

    # df_genius_m['Feed'].unique()

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>джойним к raning

    # In[1211]:

    df_raning_m = df_raning.merge(df_genius[['key', 'com1', 'com2', 'liga', '_genius']], on='key',
                                  suffixes=['_ran', '_gen'], how='left').merge(
        df_radar[['key', 'com1', 'com2', 'liga', '_radar']], on='key', suffixes=['_rad'], how='left')

    # In[ ]:

    # In[1212]:

    df_raning_m.columns

    # In[1213]:

    df_raning_m = df_raning_m[[
        'com1_ran',
        'com2_ran',
        # 'Competition',
        '_genius', '_raning', '_radar', 'key',
        # 'liga',
        'liga_ran',
    ]]
    df_raning_m

    # In[1214]:

    df_raning_m.rename(columns=({'com1_ran': 'com1',
                                 'com2_ran': 'com2',
                                 'liga_ran': 'liga'}), inplace=True)
    df_raning_m

    # In[1215]:

    df_raning_m['источник'] = 'raning'

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>джойним к df_radar

    # In[1216]:

    df_radar_m = df_radar.merge(df_genius[['key', 'com1', 'com2', 'liga', '_genius']], on='key',
                                suffixes=['_rad', '_gen'], how='left').merge(
        df_raning[['key', 'com1', 'com2', 'liga', '_raning']], on='key', suffixes=['_ran'], how='left')
    df_radar_m

    # In[1144]:

    # df_radar_m[df_radar_m['com2_rad'].isna()]

    # In[ ]:

    # In[ ]:

    # In[1217]:

    df_radar_m = df_radar_m[[
        'com1_rad', 'com2_rad',
        # 'Tournament',
        # 'Category',
        # 'Event',
        '_genius', '_raning', '_radar',
        'key', 'liga_rad',

    ]]
    df_radar_m

    # In[1218]:

    df_radar_m.rename(columns=({'com1_rad': 'com1',
                                'com2_rad': 'com2',
                                'liga_rad': 'liga',
                                }), inplace=True)
    df_radar_m

    # In[1219]:

    df_radar_m['источник'] = 'radar'

    # <div class="alert alert-block alert-info"><font size=3>
    # <b>concat

    # In[1220]:

    df_result = pd.concat([df_genius_m, df_raning_m, df_radar_m])
    df_result

    # In[1221]:

    # ---------------------------------- чичтсим
    df_result = df_result[~df_result['key'].isna()]


    df = df_result[(df_result['_genius'].isin(['VEN+', 'VEN', 'TV+', 'TV', ]))
                   | (df_result['_raning'].isin(['TV', 'LIVE', 'TV Stadium Feed ']))
                   | (df_result['_radar'].isin(['tv', 'venue', ]))]

    df_drop = df.drop_duplicates('key')

    df_drop = df_drop[[
        'com1', 'com2', '_genius', '_raning', '_radar', 'key',
        'источник', 'liga',
    ]]


    df_drop_2x = df_drop[
        (~df_drop['_genius'].isna() & ~df_drop['_raning'].isna())
        | (~df_drop['_genius'].isna() & ~df_drop['_radar'].isna())
        | (~df_drop['_raning'].isna() & ~df_drop['_radar'].isna())
        | (~df_drop['_genius'].isna() & ~df_drop['_raning'].isna() & ~df_drop['_radar'].isna())
        ]



    suffics = str(datetime.datetime.now().replace(microsecond=0))
    suffics = suffics.replace(' ', '_').replace(':', '=')

    df_drop.to_excel(f'Итогововый_файл_{suffics}.xlsx')
    df_drop_2x.to_excel(f'совпад_в_2х_файл_{suffics}.xlsx')
    print(f'Выполнение завершено')
    print(f'Файлы сохранены')
    # print(df_drop)
#     ------------------------------------------------------


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
