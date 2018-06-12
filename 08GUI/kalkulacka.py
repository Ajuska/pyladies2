from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()

with open('kalkulacka_horizontal.ui', encoding='utf-8') as file:
    uic.loadUi(file, window)

operand1 = window.findChild(QtWidgets.QDoubleSpinBox, 'Operant1')
print(operand1)
operand2 = window.findChild(QtWidgets.QDoubleSpinBox, 'Operant2')
print(operand2)
operator = window.findChild(QtWidgets.QComboBox, 'operant_box')
print(operator)
result = window.findChild(QtWidgets.QLabel, 'result')
print(result)

def calculate():
    number1 = operand1.value()
    number2 = operand2.value()
    operator_text = operator.currentText()

    try:
        if operator_text == '+':
            result_number = number1 + number2
        if operator_text == '-':
            result_number = number1 - number2
        if operator_text == '*':
            result_number = number1 * number2
        if operator_text == '/':
            result_number = number1 / number2
    except Exception:
        result_number = 'Chyba! Nulou nelze delit'

    print(number1, operator_text, number2, "=" ,result_number)
    result.setText(str(result_number))

operand1.valueChanged.connect(calculate)
operand2.valueChanged.connect(calculate)
operator.currentTextChanged.connect(calculate)

calculate()
window.show()
app.exec()


#DU
#tlacitko clear
#nastaveni hodnoty comboboxu
#operator.setCurrentText('+')
#nastaveni hodnoty doublespinboxu
#operator.setValue(0)
