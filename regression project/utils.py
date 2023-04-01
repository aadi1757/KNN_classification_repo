import pickle
import  json
import numpy as np
import pandas as pd
import os
import CONFIG

class Prediction():
    def __inin__(self):
        print(os.getcwd())

    def load_raw(self):
        with open(CONFIG.MODEL_PATH,"rb") as model_file:
            self.model = pickle.load(model_file)

        with open(CONFIG.SCALE_PATH, "rb") as scaled_file:
            self.scaled_model = pickle.load(scaled_file)

        with open(CONFIG.COL_NAMES, "r") as col_file:
            self.col_names = json.load(col_file)

        return ""

    def Price(self, data):
        self.load_raw()
        self.data = data

        user_input = np.zeros(len(self.col_names['column_names']))
        CRIM = self.data['html_crim']
        ZN = self.data['html_zn']
        INDUS = self.data['html_ind']
        CHAS = self.data['html_chas']
        NOX = self.data['html_nox']
        RM = self.data['html_rm']
        AGE = self.data['html_age']
        DIS = self.data['html_dis']
        RAD = self.data['html_rad']
        TAX = self.data['html_tax']
        PTRATIO = self.data['html_ptr']
        B = self.data['html_b']
        LSTAT = self.data['html_lstat']



        user_input[0] = CRIM
        user_input[1] = ZN
        user_input[2] = INDUS
        user_input[3] = CHAS
        user_input[4] = NOX
        user_input[5] = RM
        user_input[6] = AGE
        user_input[7] = DIS
        user_input[8] = RAD
        user_input[9] = TAX
        user_input[10] = PTRATIO
        user_input[11] = B
        user_input[12] = LSTAT


        scaled_user_input = self.scaled_model.transform([user_input])


        result = self.model.predict(scaled_user_input)
        print(result)

        return str(result)


if __name__==("__main__"):
    pred_obj = Prediction()
    pred_obj.load_raw()