import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import seaborn as sns
import xlrd
import xlwt

book = xlrd.open_workbook('Planilha.xls')
sheet = book.sheet_by_name('notas')

planilha_inteira=[[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

nomes = [planilha_inteira[i][0] for i in range(1,len(planilha_inteira))]

A1 = [planilha_inteira[i][1] for i in range(1,len(planilha_inteira))]

A1 = np.array(A1)

A2 = [planilha_inteira[i][2] for i in range(1,len(planilha_inteira))]

A2 = np.array(A2)

notafinal = (A1+A2)/2

status = []
for i in range(len(notafinal)):
    if notafinal[i] >= 6:
        status.append("Aprovado")
    elif notafinal[i] >= 1:
        status.append("Recuperação")
    else:
        status.append("Reprovado")

doc = xlwt.Workbook('Planilha.xls')

planilha_p_escreve = doc.add_sheet('notas')

planilha_p_escreve.write(0,0,'Aluno')
planilha_p_escreve.write(0,1,'A1')
planilha_p_escreve.write(0,2,'A2')
planilha_p_escreve.write(0,3,'Nota Final')
planilha_p_escreve.write(0,4,'Status')

for i in range(len(A1)):
    planilha_p_escreve.write(i+1, 0, nomes[i])
    planilha_p_escreve.write(i+1, 1, A1[i])
    planilha_p_escreve.write(i+1, 2, A2[i])
    planilha_p_escreve.write(i+1, 3, notafinal[i])
    planilha_p_escreve.write(i+1, 4, status[i])
    
doc.save('Planilha.xls')
