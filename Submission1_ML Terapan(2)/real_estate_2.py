# -*- coding: utf-8 -*-
"""Real Estate-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D-hohBnGfjsVjtUUX2SMxbYDfI-YziOz

#Data Loading
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

url = '/content/taipei_city_real_estate_transaction_v2.csv'
realestate = pd.read_csv(url)
realestate

"""Kolom Kategorikal:
1. district = Distrik tempat transaksi real estat berlangsung (contoh: Daerah di Taipei seperti Xinyi, Wanhua, dll.).
2. transaction_type = Jenis properti yang dibeli.
3. urban_land_use = Penggunaan lahan perkotaan sesuai zonasi, seperti perumahan, komersial, atau industri.
4. main_use = Penggunaan utama bangunan atau properti, misalnya hunian, kantor, atau toko.
5. main_building_material = Jenis material utama yang digunakan untuk membangun properti, seperti beton, baja, atau kayu.
6. num_partition = Kategori yang menunjukkan jumlah sekat atau partisi di dalam properti (seperti open-space atau bersekat banyak).
7. management_org = Informasi tentang ada atau tidaknya organisasi pengelola properti (contoh: "yes" untuk properti yang dikelola oleh pihak ketiga, "no" untuk properti yang dikelola sendiri).
8. carpark_category = Kategori tempat parkir, seperti parkir di bawah tanah, parkir di luar ruangan, atau parkir tertutup.

Kolom Numerik:
1. land_shift_area = Luas lahan (dalam satuan tertentu, seperti meter persegi) yang termasuk dalam transaksi.
2. complete_year = Tahun penyelesaian konstruksi bangunan yang ditransaksikan.
3. building_shift_total_area = Total luas bangunan yang termasuk dalam transaksi (dalam meter persegi).
4. num_room = Jumlah kamar di dalam properti.
5. num_hall = Jumlah ruang tengah atau ruang serbaguna dalam properti.
6. num_toilet = Jumlah toilet atau kamar mandi di properti.
7. total_ntd = Total harga transaksi dalam mata uang New Taiwan Dollar (NTD).
8. unit_ntd = Harga per satuan luas dalam mata uang NTD (contoh: NTD per meter persegi).
9. carpark_shift_area = Luas area tempat parkir yang termasuk dalam transaksi (dalam meter persegi).
10. carpark_ntd = Harga tempat parkir dalam mata uang NTD.
11. transaction_year = Tahun ketika transaksi berlangsung.
12. transaction_month = Bulan ketika transaksi berlangsung.
13. building_age = Usia bangunan (dalam tahun) pada saat transaksi dilakukan.
14. number_of_land = Jumlah bidang tanah yang termasuk dalam transaksi.
15. number_of_building = Jumlah bangunan yang termasuk dalam transaksi.
16. number_of_carpark = Jumlah tempat parkir yang termasuk dalam transaksi.

#Exploratory Data Analysis

##Deskripsi Variabel
"""

realestate.info()

realestate.describe()

"""##Missing Value"""

zero_value = (realestate == 0).sum()
zero_value

print(realestate[realestate['total_ntd'] == 0])

print(realestate[realestate['unit_ntd'] == 0])

realestate = realestate[(realestate['unit_ntd'] != 0) | (realestate['total_ntd'] != 0)]

duplicate_rows = realestate[realestate.duplicated()]

if not duplicate_rows.empty:
    print("Duplicate Rows:")
    print(duplicate_rows)
else:
    print("No duplicate rows found.")

realestate = realestate.drop_duplicates()

realestate.shape

"""##Menangani Outliers"""

rows, cols = 6, 4
fig, axes = plt.subplots(rows, cols, figsize=(20, 30))

for i, column in enumerate(realestate.columns):
    row, col = divmod(i, cols)
    sns.boxplot(ax=axes[row, col], x=realestate[column])
    axes[row, col].set_title(f'Box Plot of {column}')

for j in range(len(realestate.columns), rows * cols):
    fig.delaxes(axes.flatten()[j])

plt.tight_layout()
plt.show()

"""###Isolation Forest Method"""

numerical_features = ['land_shift_area','complete_year','building_shift_total_area' ,'num_room','num_hall','num_toilet','total_ntd','unit_ntd','carpark_shift_area','carpark_ntd','transaction_year','transaction_month','building_age','number_of_land','number_of_building','number_of_carpark']
categorical_features = ['district' ,'transaction_type' ,'urban_land_use' ,'main_use' ,'main_building_material' ,'num_partition' ,'management_org' ,'carpark_category']

from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.05, random_state=42)  # 5% dianggap outlier
outliers = iso_forest.fit_predict(realestate[numerical_features])
realestate_no_outliers = realestate[outliers == 1]

print(realestate_no_outliers.shape)

for column in numerical_features:
    plt.figure(figsize=(8, 6))
    sns.histplot(realestate[column], kde=True, label="Original Data", color="blue")
    sns.histplot(realestate_no_outliers[column], kde=True, label="Filtered Data", color="orange")
    plt.legend()
    plt.title(f'Distribution of {column}')
    plt.show()

iso_forest = IsolationForest(contamination=0.05, random_state=42)  # 5% dianggap outlier
outliers = iso_forest.fit_predict(realestate[numerical_features])
realestate = realestate[outliers == 1]

print(realestate.shape)

"""##Feature Engineering


"""

realestate['management_org'] = realestate['management_org'].replace({'有': 1, '無': 0})
realestate['num_partition'] = realestate['num_partition'].replace({'有': 1, '無': 0})

"""###Haversine"""

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c

# Koordinat distrik-distrik
districts_data = {
    "district": ["Zhongshan Area", "Neihu District", "Wenshan District", "shihlin", "Daan District", "Beitou", "Wanhua District", "Songshan District", "Xinyi District", "Zhongzheng District", "Datong District", "Nangang District"],
    "Latitude": [25.0500, 25.0800, 24.9900, 25.0800, 25.0260, 25.1300, 25.0300, 25.0500, 25.0339, 25.0330, 25.0500, 25.0600],
    "Longitude": [121.5200, 121.6000, 121.5700, 121.5200, 121.5350, 121.5000, 121.5000, 121.5500, 121.5645, 121.5140, 121.5200, 121.6400]
}

# Koordinat pusat kota Taipei
taipei_center_lat = 25.0320
taipei_center_lon = 121.5654

Distance_to_Taipei_Center = pd.DataFrame(districts_data)
Distance_to_Taipei_Center['Distance_to_Taipei_Center'] = Distance_to_Taipei_Center.apply(lambda row: haversine(row['Latitude'], row['Longitude'], taipei_center_lat, taipei_center_lon), axis=1)

print(Distance_to_Taipei_Center)

realestate = realestate.merge(
    Distance_to_Taipei_Center[['district', 'Distance_to_Taipei_Center']],
    how='left',
    on='district'
)

print(realestate.head())

"""##Univariate Analysis"""

numerical_features = ['land_shift_area','complete_year','building_shift_total_area' ,'num_room','num_hall','num_toilet','total_ntd','unit_ntd','carpark_shift_area','carpark_ntd','transaction_year','transaction_month','building_age','number_of_land','number_of_building','number_of_carpark','Distance_to_Taipei_Center']
categorical_features = ['district','transaction_type' ,'urban_land_use' ,'main_use' ,'main_building_material' ,'num_partition' ,'management_org' ,'carpark_category']

"""###Categorical Features"""

feature = categorical_features[0]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[1]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[2]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[3]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[4]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[5]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

feature = categorical_features[6]
count = realestate[feature].value_counts()
percent = 100*realestate[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""###Numerical Features"""

realestate.hist(bins=50, figsize=(20,15))
plt.show()

"""##Multivariate Analysis

###Categorical Feature
"""

print(realestate.dtypes)

cat_features = realestate.select_dtypes(include='object').columns.to_list()

for col in cat_features:
    sns.catplot(
        x=col,
        y="total_ntd",
        kind="bar",
        dodge=False,
        height=4,
        aspect=3,
        data=realestate,
        palette="Set3"
    )
    plt.title("Rata-rata 'price' Relatif terhadap - {}".format(col))
    plt.xticks(rotation=90)
    plt.show()

"""###Numerical Features"""

sns.pairplot(realestate, diag_kind = 'kde')

"""###Melihat Korelasi menggunakan metode spearman"""

plt.figure(figsize=(10, 8))
correlation_matrix = realestate[numerical_features].corr(method='spearman').round(2)

sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""#Data Preparation

##Encoding Fitur Kategori
"""

from sklearn.preprocessing import  OneHotEncoder
realestate = pd.concat([realestate, pd.get_dummies(realestate['district'], prefix='district').astype(int)], axis=1)
realestate.drop(['district'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['transaction_type'], prefix='transaction_type').astype(int)], axis=1)
realestate.drop(['transaction_type'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['urban_land_use'], prefix='urban_land_use').astype(int)], axis=1)
realestate.drop(['urban_land_use'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['main_use'], prefix='main_use').astype(int)], axis=1)
realestate.drop(['main_use'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['main_building_material'], prefix='main_building_material').astype(int)], axis=1)
realestate.drop(['main_building_material'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['num_partition'], prefix='num_partition').astype(int)], axis=1)
realestate.drop(['num_partition'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['management_org'], prefix='management_org').astype(int)], axis=1)
realestate.drop(['management_org'], axis=1, inplace=True)

realestate = pd.concat([realestate, pd.get_dummies(realestate['carpark_category'], prefix='carpark_category').astype(int)], axis=1)
realestate.drop(['carpark_category'], axis=1, inplace=True)

realestate.head()

"""##Train-Test-Split"""

from sklearn.model_selection import train_test_split

X = realestate.drop(["total_ntd"],axis =1)
y = realestate["total_ntd"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""##Standarisasi fitur"""

from sklearn.preprocessing import StandardScaler

numerical_features = ['land_shift_area','complete_year','building_shift_total_area' ,'num_room','num_hall','num_toilet','unit_ntd','carpark_shift_area','carpark_ntd','building_age','number_of_building','number_of_carpark']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(3)

"""##PCA

###Data Train

####building_age dan complete_year
"""

sns.pairplot(X_train[['building_age','complete_year']], plot_kws={"s": 2});

from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=123)
pca.fit(X_train[['building_age','complete_year']])
princ_comp = pca.transform(X_train[['building_age','complete_year']])

pca.explained_variance_ratio_.round(2)

X_train.drop(['building_age'], axis=1, inplace=True)

"""####carpark_shift_area dan carpark_ntd"""

sns.pairplot(X_train[['carpark_shift_area','carpark_ntd']], plot_kws={"s": 2});

pca = PCA(n_components=2, random_state=123)
pca.fit(X_train[['carpark_shift_area','carpark_ntd']])
princ_comp = pca.transform(X_train[['carpark_shift_area','carpark_ntd']])

pca.explained_variance_ratio_.round(2)

from sklearn.decomposition import PCA
pca = PCA(n_components=1, random_state=123)
pca.fit(X_train[['carpark_shift_area','carpark_ntd']])
X_train['carpark_area_ntd'] = pca.transform(X_train.loc[:, ('carpark_shift_area','carpark_ntd')]).flatten()
X_train.drop(['carpark_shift_area','carpark_ntd'], axis=1, inplace=True)

"""####num_hall, num_room, dan num_toilet"""

sns.pairplot(X_train[['num_hall','num_room','num_toilet']], plot_kws={"s": 3});

pca = PCA(n_components=3, random_state=123)
pca.fit(X_train[['num_hall','num_room','num_toilet']])
princ_comp = pca.transform(X_train[['num_hall','num_room','num_toilet']])

pca.explained_variance_ratio_.round(3)

pca = PCA(n_components=1, random_state=123)
pca.fit(X_train[['num_hall','num_room','num_toilet']])
X_train['facility'] = pca.transform(X_train.loc[:, ('num_hall','num_room','num_toilet')]).flatten()
X_train.drop(['num_hall','num_room','num_toilet'], axis=1, inplace=True)

"""#Model Development"""

models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""##Model Development dengan K-Nearest Neighbor"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=15)
knn.fit(X_train, y_train)

models.loc['train_mse','KNN'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""##Model Development dengan Random Forest"""

from sklearn.ensemble import RandomForestRegressor

RF = RandomForestRegressor(n_estimators=20, max_depth=5, random_state=35, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""##Model Development dengan Boosting Algorithm"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(n_estimators=300,
                             learning_rate=0.01,
                             random_state=42)

boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""##Evaluasi Model

### Scaling tes data
"""

X_test[numerical_features] = scaler.transform(X_test.loc[:, numerical_features])
X_test[numerical_features].head()

X_test[numerical_features].describe().round(3)

"""###PCA pada data tes"""

X_test.drop(['building_age'], axis=1, inplace=True)

pca = PCA(n_components=2, random_state=123)
pca.fit(X_test[['carpark_shift_area','carpark_ntd']])
princ_comp = pca.transform(X_test[['carpark_shift_area','carpark_ntd']])

pca.explained_variance_ratio_.round(2)

pca = PCA(n_components=1, random_state=123)
pca.fit(X_test[['carpark_shift_area','carpark_ntd']])
X_test['carpark_area_ntd'] = pca.transform(X_test.loc[:, ('carpark_shift_area','carpark_ntd')]).flatten()
X_test.drop(['carpark_shift_area','carpark_ntd'], axis=1, inplace=True)

pca = PCA(n_components=3, random_state=123)
pca.fit(X_test[['num_hall','num_room','num_toilet']])
princ_comp = pca.transform(X_test[['num_hall','num_room','num_toilet']])

pca.explained_variance_ratio_.round(3)

pca = PCA(n_components=1, random_state=123)
pca.fit(X_test[['num_hall','num_room','num_toilet']])
X_test['facility'] = pca.transform(X_test.loc[:, ('num_hall','num_room','num_toilet')]).flatten()
X_test.drop(['num_hall','num_room','num_toilet'], axis=1, inplace=True)

"""### Hasil Evaluasi"""

mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(X_test).round(1)

pd.DataFrame(pred_dict)

pred_dict = {
    'y_true': y_test
}

for name, model in model_dict.items():
    pred_dict[f'prediksi_{name}'] = model.predict(X_test).round(1)

pred_df = pd.DataFrame(pred_dict)

model_names = [col for col in pred_df.columns if col.startswith('prediksi_')]
for model in model_names:
    pred_df[f'error_{model}'] = np.abs(pred_df['y_true'] - pred_df[model])

pred_df['best_model'] = pred_df[[f'error_{model}' for model in model_names]].idxmin(axis=1)

conf_matrix = pd.DataFrame(
    {model: [(pred_df['best_model'] == f'error_{model}').sum() for model in model_names]},
    index=model_names
)

print("Confusion Matrix Berdasarkan Selisih Terkecil:")
print(conf_matrix)

gridtuning = pd.DataFrame(index=['KNN', 'RF', 'Adaboost'], columns=['train_mse', 'test_mse'])

from sklearn.model_selection import GridSearchCV

param_grid_knn = {
    'n_neighbors': [3, 5, 7, 9, 11, 13, 15]
}

knn = KNeighborsRegressor()

grid_search_knn = GridSearchCV(knn, param_grid_knn, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_knn.fit(X_train, y_train)

gridtuning.loc['KNN', 'train_mse'] = mean_squared_error(y_pred=grid_search_knn.predict(X_train), y_true=y_train)
gridtuning.loc['KNN', 'test_mse'] = mean_squared_error(y_pred=grid_search_knn.predict(X_test), y_true=y_test)

param_grid_rf = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

rf = RandomForestRegressor(random_state=35, n_jobs=-1)

grid_search_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_rf.fit(X_train, y_train)

gridtuning.loc['RF', 'train_mse'] = mean_squared_error(y_pred=grid_search_rf.predict(X_train), y_true=y_train)
gridtuning.loc['RF', 'test_mse'] = mean_squared_error(y_pred=grid_search_rf.predict(X_test), y_true=y_test)

param_grid_ada = {
    'n_estimators': [50, 100, 200, 300],
    'learning_rate': [0.01, 0.1, 1.0]
}

ada = AdaBoostRegressor(random_state=42)

grid_search_ada = GridSearchCV(ada, param_grid_ada, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_ada.fit(X_train, y_train)

gridtuning.loc['Adaboost', 'train_mse'] = mean_squared_error(y_pred=grid_search_ada.predict(X_train), y_true=y_train)
gridtuning.loc['Adaboost', 'test_mse'] = mean_squared_error(y_pred=grid_search_ada.predict(X_test), y_true=y_test)

gridtuning

fig, ax = plt.subplots()
gridtuning.sort_values(by='test_mse', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

pred_dict_grid = {'y_true': y_test}

model_dict_grid = {
    'KNN': grid_search_knn,
    'RF': grid_search_rf,
    'Adaboost': grid_search_ada
}

for name, model in model_dict_grid.items():
    pred_dict_grid[f'prediksi_{name}'] = model.predict(X_test).round(1)

pred_df_grid = pd.DataFrame(pred_dict_grid)
pred_df_grid

for name, model in model_dict_grid.items():
    pred_dict_grid[f'prediksi_{name}'] = model.predict(X_test).round(1)

pred_df = pd.DataFrame(pred_dict_grid)

model_names = [col for col in pred_df.columns if col.startswith('prediksi_')]
for model in model_names:
    pred_df[f'error_{model}'] = np.abs(pred_df['y_true'] - pred_df[model])

pred_df['best_model'] = pred_df[[f'error_{model}' for model in model_names]].idxmin(axis=1)

conf_matrix = pd.DataFrame(
    {model: [(pred_df['best_model'] == f'error_{model}').sum() for model in model_names]},
    index=model_names
)

print("Confusion Matrix Berdasarkan Selisih Terkecil:")
print(conf_matrix)