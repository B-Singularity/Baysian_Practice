import matplotlib.pyplot as plt
def plot(distributions, labels=None):
    """
    여러 분포를 한 화면에 동시에 플롯합니다.

    Parameters:
        distributions (list of Series): 분포(Pandas Series)의 리스트
        xs (array-like): X 축 값
        labels (list of str): 각 분포에 대한 레이블 리스트 (선택적)
    """
    plt.figure(figsize=(10, 5))

    for i, distribution in enumerate(distributions):
        label = labels[i] if labels else f'Distribution {i + 1}'
        plt.plot(distribution.index, distribution.values, label=label)

    plt.xlabel('x')
    plt.ylabel('probability')
    plt.legend()
    plt.grid(True)
    plt.show()