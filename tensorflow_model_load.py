import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split







if __name__ == "__main__":
    # 데이터 로드
    df = pd.read_csv("data/weather_classification_data.csv")

    # 'Cloud Cover' 열의 값을 숫자로 변환
    df['Cloud Cover'] = np.where(df['Cloud Cover'] == 'partly cloudy', 0,
                                 np.where(df['Cloud Cover'] == 'clear', 1,
                                          np.where(df['Cloud Cover'] == 'overcast', 2, 3)))

    # 'Season' 열의 값을 숫자로 변환
    df['Season'] = np.where(df['Season'] == 'Winter', 0,
                            np.where(df['Season'] == 'Spring', 1,
                                     np.where(df['Season'] == 'Summer', 2, 3)))

    # 'Location' 열의 값을 숫자로 변환
    df['Location'] = np.where(df['Location'] == 'inland', 0,
                              np.where(df['Location'] == 'mountain', 1, 2))

    # 'Weather Type' 열의 값을 숫자로 변환
    df['Weather Type'] = np.where(df['Weather Type'] == 'Rainy', 0,
                                  np.where(df['Weather Type'] == 'Cloudy', 1,
                                           np.where(df['Weather Type'] == 'Sunny', 2, 3)))

    # 입력 피처와 레이블 설정
    X = df[['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
            'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season',
            'Visibility (km)', 'Location']].values
    y = df[['Weather Type']].values

    # 데이터 정규화
    X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 레이블을 원-핫 인코딩
    y_train = tf.one_hot(y_train.flatten(), 4)
    y_test = tf.one_hot(y_test.flatten(), 4)

    # 모델 로드
    model = tf.keras.models.load_model("weatherAnn_tf_2.15.0_version0")

    # 특정 테스트 샘플 선택 및 예측 수행
    print(X_test[20:21])
    predY = model.predict(X_test[20:21])

    # 실제 레이블 출력
    print(int(tf.argmax(y_test[20:21][0], axis=0)))

    # 예측 결과 출력
    print(predY[0].argmax())

    # 예측 결과 배열 출력
    print(predY)
