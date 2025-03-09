import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, Subset
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
def load_and_prepare_data(filepath, sep=';'):
    data = pd.read_csv(filepath, sep=sep)
    data = data.replace(',', '.', regex=True).astype(float)
    data = data.sample(frac=0.001, random_state=42)
    X = data.iloc[:, :-1].values  # Признаки
    y = data.iloc[:, -1].values   # Метки
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.long)
    dataset = TensorDataset(X_tensor, y_tensor)
    return dataset, X.shape[1], len(np.unique(y))
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
#обучает одну модель
def train_model(model, train_loader, num_epochs=20):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)# возвращает итератор параметров модели
    for epoch in range(num_epochs):
        for data, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
def train_ensemble(models, dataset, sample_size=0.8, num_epochs=20):
    for model in models:
        sample_indices = torch.randperm(len(dataset))[:int(sample_size * len(dataset))]#генерирует случайную перестановку индексов всех элементов датасета.
        subset = Subset(dataset, sample_indices)#создаёт подвыборку данных из исходного датасета на основе выбранных индексов.
        train_loader = DataLoader(subset, batch_size=16, shuffle=True)
        train_model(model, train_loader, num_epochs)
def ensemble_predict(models, data):
    outputs = [model(data) for model in models]
    avg_output = torch.mean(torch.stack(outputs), dim=0)
    _, predicted = torch.max(avg_output, 1)
    return predicted
def calculate_accuracy(models, data_loader):
    correct = 0
    total = 0
    with torch.no_grad():
        for data, labels in data_loader:
            predictions = ensemble_predict(models, data)
            correct += (predictions == labels).sum().item()
            total += labels.size(0)
    accuracy = correct / total * 100
    return accuracy
if __name__ == "__main__":
    filepath = '/content/fegnn.csv'
    dataset, input_size, output_size = load_and_prepare_data(filepath)
    num_models = 10
    hidden_size1 = 64
    hidden_size2 = 32
    models = [SimpleNet(input_size, hidden_size1, hidden_size2, output_size) for _ in range(num_models)]
    train_ensemble(models, dataset)
    data_loader = DataLoader(dataset, batch_size=16, shuffle=False)
    accuracy = calculate_accuracy(models, data_loader)
def preprocess_input(user_input, scaler):
    processed_input = np.array(user_input).reshape(1, -1)
    processed_input = scaler.transform(processed_input)
    return torch.tensor(processed_input, dtype=torch.float32)
def plot_wind_rose(predictions):
    angles = np.deg2rad(np.linspace(0, 360, len(predictions), endpoint=False))
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.bar(angles, predictions, width=np.deg2rad(360 / len(predictions)), color='skyblue', edgecolor='black')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    angles_ticks = np.linspace(0, 2 * np.pi, len(directions), endpoint=False)
    ax.set_xticks(angles_ticks)
    ax.set_xticklabels(directions)
    plt.title("Wind Rose - Predictions", fontsize=16)
    plt.show()
def ensemble_predict(models, processed_input):
    predictions = [model(processed_input).item() for model in models]
    return sum(predictions) / len(predictions)
if __name__ == "__main__":
    class DummyModel:
        def __call__(self, x):
            return torch.sum(x)
    models = [DummyModel() for _ in range(3)]
    scaler = StandardScaler()
    scaler.fit([[1.23, 4.56, 7.89, 0.12, 3.45, 6.78, 9.01]])  # Пример данных для обучения scaler
    example_input = [
        [234, 456, 789, 12, 345,6.78, 9.01],  # Пример 1
    ]

    predictions = []
    for user_input in example_input:
        processed_input = preprocess_input(user_input, scaler)
        prediction = ensemble_predict(models, processed_input)
        predictions.append(prediction)
    plot_wind_rose(predictions) 
import pygame
import numpy as np
import time

# Параметры сетки
GRID_WIDTH = 20
GRID_HEIGHT = 10
CELL_SIZE = 20  # Размер одной клетки в пикселях

# Цвета
BACKGROUND_COLOR = (0, 0, 0)  # черный
CELL_COLOR = (255, 255, 255)  # белый

# Инициализация сетки
def initialize_grid():
    grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    grid[GRID_HEIGHT // 2, GRID_WIDTH // 2] = 1  # Центр активен
    return grid

# Обновление сетки
def update_grid(grid):
    new_grid = grid.copy()
    for y in range(1, GRID_HEIGHT - 1):
        for x in range(1, GRID_WIDTH - 1):
            if grid[y, x] == 1:
                if np.random.rand() < 0.1:
                    new_grid[y + np.random.randint(-1, 2), x + np.random.randint(-1, 2)] = 1
    return new_grid

# Отрисовка сетки
def draw_grid(screen, grid):
    screen.fill(BACKGROUND_COLOR)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y, x] == 1:
                pygame.draw.rect(screen, CELL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Основной цикл
def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Клеточный автомат")

    grid = initialize_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        draw_grid(screen, grid)
        time.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    main()
