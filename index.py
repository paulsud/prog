import urllib.request
import urllib.error
from spyre import server
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

class StockExample(server.App):
    title = "Inputs"

    inputs = [{"type": 'dropdown',
               "label": 'Index  ',
               "options": [{"label": "VCI", "value": "VCI"},
                           {"label": "TCI", "value": "TCI"},
                           {"label": "VHI", "value": "VHI"}, ],
               "key": 'index',
               "action_id": "update_data"},

              {"type": 'dropdown',
               "label": 'Region',
                "options": [{"label": "Винница", "value": "01"},
                           {"label": "Волынь", "value": "02"},
                           {"label": "Днепропетровск", "value": "03"},
                           {"label": "Донецк", "value": "04"},
                           {"label": "Житомир", "value": "05"},
                           {"label": "Закарпатье", "value": "06"},
                           {"label": "Запорожье", "value": "07"},
                           {"label": "Ивано-Франковск", "value": "08"},
                           {"label": "Киевская область", "value": "09"},
                           {"label": "Кировоград", "value": "10"},
                           {"label": "Луганск", "value": "11"},
                           {"label": "Львов", "value": "12"},
                           {"label": "Николаев", "value": "13"},
                           {"label": "Одесса", "value": "14"},
                           {"label": "Полтава", "value": "15"},
                           {"label": "Ровно", "value": "16"},
                           {"label": "Суммы", "value": "17"},
                           {"label": "Тернополь", "value": "18"},
                           {"label": "Харьков", "value": "19"},
                           {"label": "Херсон", "value": "20"},
                           {"label": "Хмельницкий", "value": "21"},
                           {"label": "Черкассы", "value": "22"},
                           {"label": "Черновцы", "value": "23"},
                           {"label": "Чернигов", "value": "24"},
                           {"label": "Крым", "value": "25"},
                           {"label": "Kиев", "value": "26"},
                           {"label": "Севастополь", "value": "27"}],
               "key": 'region1',
               "action_id": "update_data"},

              {"type": 'dropdown',
               "label": 'Region',
                "options": [{"label": "Винница", "value": "01"},
                           {"label": "Волынь", "value": "02"},
                           {"label": "Днепропетровск", "value": "03"},
                           {"label": "Донецк", "value": "04"},
                           {"label": "Житомир", "value": "05"},
                           {"label": "Закарпатье", "value": "06"},
                           {"label": "Запорожье", "value": "07"},
                           {"label": "Ивано-Франковск", "value": "08"},
                           {"label": "Киевская область", "value": "09"},
                           {"label": "Кировоград", "value": "10"},
                           {"label": "Луганск", "value": "11"},
                           {"label": "Львов", "value": "12"},
                           {"label": "Николаев", "value": "13"},
                           {"label": "Одесса", "value": "14"},
                           {"label": "Полтава", "value": "15"},
                           {"label": "Ровно", "value": "16"},
                           {"label": "Суммы", "value": "17"},
                           {"label": "Тернополь", "value": "18"},
                           {"label": "Харьков", "value": "19"},
                           {"label": "Херсон", "value": "20"},
                           {"label": "Хмельницкий", "value": "21"},
                           {"label": "Черкассы", "value": "22"},
                           {"label": "Черновцы", "value": "23"},
                           {"label": "Чернигов", "value": "24"},
                           {"label": "Крым", "value": "25"},
                           {"label": "Kиев", "value": "26"},
                           {"label": "Севастополь", "value": "27"}],
               "key": 'region2',
               "action_id": "update_data"},


              {"input_type": "text",
               "variable_name": "year",
               "label": "Year",
               "value": 1982,
               "key": 'year',
               "action_id": "update_data"},

              {"type": 'slider',
               "label": 'First week',
               "min": 1, "max": 52, "value": 0,
               "key": 'first',
               "action_id": 'update_data'},

              {"type": 'slider',
               "label": 'Last week',
               "min": 1, "max": 52, "value": 35,
               "key": 'last',
               "action_id": 'update_data'},

              {"type": 'slider',
               "label": 'Percent of area',
               "min": 0, "max": 100, "value": 0,
               "key": 'percent',
               "action_id": 'update_data'},

              {"type": 'slider',
               "label": 'Minimum VHI',
               "min": 0, "max": 100, "value": 0,
               "key": 'minimum',
               "action_id": 'update_data'},

              {"type": 'slider',
               "label": 'Maximum VHI',
               "min": 0, "max": 100, "value": 100,
               "key": 'maximum',
               "action_id": 'update_data'}, ]

    controls = [{"type": "hidden",
                 "id": "update_data"}]

    tabs = ["Plot", "Table", "Drought"]

    outputs = [{"type": "plot",
                "id": "plot",
                "control_id": "update_data",
                "tab": "Plot"},
               {"type": "table",
                "id": "table_id",
                "control_id": "update_data",
                "tab": "Table"},
               {"type": "html",
                "id": "html_id",
                "control_id": "update_data",
                "tab": "Drought"}]

    def get(self, params, reg):

        index = params['index']
        region = params[reg]
        year = params['year']
        first = params['first']
        last = params['last']

        path = r"C:\Users\pc\PycharmProjects\lab1"
        allFiles = glob.glob(path + "/*"+"{}".format(region)+".csv")
        file = allFiles[0]
        df = pd.read_csv(file, header=1, names=['DATE','SMT','VCI','TCI','VHI'],  delimiter=',')
        df = df.dropna()

        df['year'], df['weeksmn'] = df['DATE'].str.split(' ', 1).str
        df['week'], df['smn'] = df['weeksmn'].str.split('  ', 1).str
        del df['DATE']
        del df['weeksmn']
        df = df[['year', 'week', 'smn', 'SMT', 'VCI', 'TCI', 'VHI']]

        df1 = df[(df['year'].astype(int) == int(year)) & (df['week'].astype(int) >= int(first)) & (df['week'].astype(int) <= int(last))]
        df1 = df1[['week', index]]
        return df1

    def getPlot(self, params):

        index = params['index']
        year = params['year']
        first = params['first']
        last = params['last']
        df = self.get(params, 'region1')
        df2 = self.get(params, 'region2')

        result = pd.merge(df, df2, on='week')
        plt_obj = result.plot()
        plt_obj.set_ylabel(index)
        plt_obj.set_xlabel('weeks')
        plt_obj.set_title('Index {index} for {year} from {first} to {last} weeks'.format(index=index,
                                                                                         year=int(year),
                                                                                         first=int(first),
                                                                                         last=int(last)))
        fig = plt_obj.get_figure()
        return fig


app = StockExample()
app.launch()
