import xlsxwriter

workbook = xlsxwriter.Workbook("Boletim2.0")
worksheet = workbook.add_worksheet()
worksheet.write("B3", "Física")
worksheet.write("B4", "Matemática")
worksheet.write("B5", "Português")
worksheet.write("B6", "Filosofia")
worksheet.write("B7", "Sociologia")

worksheet.write("C2", "1° bimestre")
worksheet.write("C3", 10)
worksheet.write("C4", 10)
worksheet.write("C5", 8.80)
worksheet.write("C6", 9.5)
worksheet.write("C7", 7)

worksheet.write("D2", "2° bimestre")
worksheet.write("D3", 8)
worksheet.write("D4", 10)
worksheet.write("D5", 9.90)
worksheet.write("D6", 10)
worksheet.write("D7", 9)

worksheet.write("E2", "3° bimestre")
worksheet.write("E3", 9)
worksheet.write("E4", 10)
worksheet.write("E5", 8)
worksheet.write("E6", 9.5)
worksheet.write("E7", 9)

worksheet.write("F2", "4° bimestre")
worksheet.write("F3", 10)
worksheet.write("F4", 10)
worksheet.write("F5", 10)
worksheet.write("F6", 10)
worksheet.write("F7", 10)

worksheet.write("G2", "Média")
worksheet.write("G3", "=SOMA(C3:F3)/4")
worksheet.write("G4", "=SOMA(C4:F4)/4")
worksheet.write("G5", "=SOMA(C5:F5)/4")
worksheet.write("G6", "=SOMA(C6:F6)/4")
worksheet.write("G7", "=SOMA(C7:F7)/4")

workbook.close()