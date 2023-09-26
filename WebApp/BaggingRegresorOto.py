import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
import pickle
# Đọc dữ liệu từ file
data = pd.read_excel('data.xlsx',index_col=0)
data = data.dropna()
le = LabelEncoder()
data['Hãng xe'] = le.fit_transform(data['Hãng xe'])
data['Tên xe'] = le.fit_transform(data['Tên xe'])
data['Loại xe'] = le.fit_transform(data['Loại xe'])
data['Năm SX'] = le.fit_transform(data['Năm SX'])
data['Xuất xứ'] = le.fit_transform(data['Xuất xứ'])
data['Tỉnh thành'] = le.fit_transform(data['Tỉnh thành'])
data['Quận huyện'] = le.fit_transform(data['Quận huyện'])
data['Km đã đi'] = le.fit_transform(data['Km đã đi'])
data['Tình trạng'] = le.fit_transform(data['Tình trạng'])
data['Nhiên liệu'] = le.fit_transform(data['Nhiên liệu'])
data['Kiểu dáng'] = le.fit_transform(data['Kiểu dáng'])
data['Hộp số'] = le.fit_transform(data['Hộp số'])
scaler = StandardScaler()
X = data[['Hãng xe','Tên xe', 'Loại xe','Năm SX','Xuất xứ','Tỉnh thành','Quận huyện','Km đã đi', 'Tình trạng', 'Nhiên liệu', 'Kiểu dáng', 'Hộp số']]
y = data['Đơn giá']
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeRegressor()
# Khởi tạo một Bagging Regressor với 10 mô hình Decision Tree
bagging = BaggingRegressor(base_estimator=model, n_estimators=10)
# Huấn luyện mô hình với dữ liệu huấn luyện X_train, y_train
bagging.fit(X_train, y_train)
# Dự đoán giá trị y cho dữ liệu kiểm tra X_test
y_pred = bagging.predict(X_test)
def predict(input_data):
    # Thực hiện chuẩn hóa đầu vào theo scaler đã được train trước đó
    input_data = scaler.transform(input_data)

    # Dự đoán giá trị của đầu vào bằng mô hình đã được train
    output = model.predict(input_data)

    # Chuẩn hóa lại đầu ra theo scaler đã được train trước đó
    output = scaler.inverse_transform(output)

    # Trả về giá trị dự đoán
    return output[0]

# with open("car_price_prediction.pkl", "wb") as file:
#     pickle.dump(model, file)

import pickle
pickle.dump(bagging, open('bagging.pkl', 'wb'))