import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Plotter:
    def __init__(self, plots_dir='plots'):
        self.plots_dir = plots_dir
        if not os.path.exists(self.plots_dir):
            os.makedirs(self.plots_dir)

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        plots_paths = []

        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['mean', 'floor_mean', 'ceiling_mean']])
        plt.xlabel('Тип Отклонений')
        plt.ylabel('Отклонение')
        plt.title('Распределение типов отклонения')
        plot_path = os.path.join(self.plots_dir, 'boxplot_deviations.png')
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()
        plots_paths.append(plot_path)

        plt.figure(figsize=(10, 6))
        plt.scatter(df['gt_corners'], df['mean'], label='Mean Deviation', color='b')
        plt.scatter(df['gt_corners'], df['floor_mean'], label='Floor Mean Deviation', color='g')
        plt.scatter(df['gt_corners'], df['ceiling_mean'], label='Ceiling Mean Deviation', color='r')
        plt.xlabel('Углы')
        plt.ylabel('Отклонение')
        plt.title('Диаграмма отклонений')
        plt.legend()
        plot_path = os.path.join(self.plots_dir, 'scatter_deviations_vs_corners.png')
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()
        plots_paths.append(plot_path)


        plt.figure(figsize=(10, 6))
        correct_predictions = (df['gt_corners'] == df['rb_corners']).sum()
        incorrect_predictions = (df['gt_corners'] != df['rb_corners']).sum()
        labels = ['Доля правильных предсказаний', 'Доля неправильных предсказаний']
        sizes = [correct_predictions, incorrect_predictions]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
        plt.title('Процент правильных предсказаний')
        plot_path = os.path.join(self.plots_dir, 'pie_chart_correct_predictions.png')
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()
        plots_paths.append(plot_path)

        return plots_paths
