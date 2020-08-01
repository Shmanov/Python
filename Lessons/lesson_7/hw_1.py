# Реализовать класс Matrix (матрица). 
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — 
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д

list_matrix = list()

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        matr = ""
        for i in range(0, len(self.matrix)):
            
            for j in range(len(self.matrix[i])):
                matr += str(self.matrix[i][j]) + " "
            matr +="\n"
            
        return matr

    def __add__(self, other):
        rezult_matrix = list()
        
        for i in range(0, len(self.matrix)):
            row_matrix = list()
            for j in range(len(self.matrix[i])):
                row_matrix.append((float(self.matrix[i][j]) + float(other.matrix[i][j])))
            rezult_matrix.append(row_matrix)
        return rezult_matrix


matrix_1 = Matrix([[5,5],[3,8],[9,7]])
matrix_2 = Matrix([[3,2],[1,4],[8,6]])

#matrix_1 = Matrix([[float(input("Введите элемент " + str(i) + str(j) + " ")) for i in range(3)] for j in range(3)])
#matrix_2 = Matrix([[float(input("Введите элемент " + str(i) + str(j) + " ")) for i in range(3)] for j in range(3)])

matrix_3 = Matrix(matrix_1 + matrix_2)

print(matrix_1)

print(matrix_2)

print(matrix_3)