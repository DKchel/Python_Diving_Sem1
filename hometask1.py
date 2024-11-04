# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

triangle_sides = []
for i in range(3):
    triangle_sides.append(int(input('Введите длину стороны треугольника: ')))

if triangle_sides[0] + triangle_sides[1] <= triangle_sides[2] or triangle_sides[0] + triangle_sides[2] <= triangle_sides[1] or triangle_sides[2] + triangle_sides[1] <= triangle_sides[0]:
    res = f'Треугольника со сторонами {triangle_sides[0]} / {triangle_sides[1]} / {triangle_sides[2]} не существует'
elif len(set(triangle_sides)) == 1:
    res = f'Треугольник со сторонами: {triangle_sides[0]} / {triangle_sides[1]} / {triangle_sides[2]} - равносторонний'
elif len(set(triangle_sides)) == 2:
    res = f'Треугольник со сторонами: {triangle_sides[0]} / {triangle_sides[1]} / {triangle_sides[2]} - равнобедренный'
else:
    res = f'Треугольник со сторонами: {triangle_sides[0]} / {triangle_sides[1]} / {triangle_sides[2]} - разносторонний'
print(res)