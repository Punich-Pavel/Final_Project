import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Создаем бесконечный цикл для обновления гистограммы ошибок
while True:
    try:
        # Читаем файл логов
        data = pd.read_csv('logs/metric_log.csv')

        # Визуализируем гистограмму ошибок модели
        fig = plt.figure(figsize=(10, 5))
        sns.histplot(data['absolute_error'], kde=True, color="orange")
        
        # Сохраняем гистограмму
        plt.savefig('logs/error_distribution.png')
        print('Файл успешно сохранен')
    except Exception as error:
        print('Визуализация не удалась: {}'.format(error))