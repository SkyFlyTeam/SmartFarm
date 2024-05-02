from flask import Flask, render_template, send_from_directory, request, redirect
from gerar_grafico import grafico, gerar_tabela, obter_ultimos_valores, comparar_ultimos_valores
from banco import criar_banco
from werkzeug.utils import secure_filename
import os
#globals
import estaticos as statics




app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = statics.up_folder




@app.route('/')
def main():
    dados0 = obter_ultimos_valores("Umidade Ambiente")
    dados1 = obter_ultimos_valores("Umidade solo")
    dados2 = obter_ultimos_valores("Temperatura")
    dados3 = obter_ultimos_valores("Volume Água (L)")
    # Filtro de 'str' para dados'Z'
    if type(dados2) is str:
        dados2 = float(obter_ultimos_valores("Temperatura").replace(",","."))
    if type(dados3) is str:
        dados3 = float(obter_ultimos_valores("Volume Água (L)").replace(",","."))

    ante0 = comparar_ultimos_valores("Umidade Ambiente")
    ante1 = comparar_ultimos_valores("Umidade solo")
    ante2 = comparar_ultimos_valores("Temperatura")
    ante3 = comparar_ultimos_valores("Volume Água (L)")
    # Filtro de 'str' para ante'Z'
    if type(ante2) is str:
        ante2 = float(comparar_ultimos_valores("Temperatura").replace(",","."))
    if type(ante3) is str:
        ante3 = float(comparar_ultimos_valores("Volume Água (L)").replace(",","."))


    # Zero on 0
    if dados0 == 0:
        print(dados0, ante0)
        comp0 = statics.zero
    else:
        print(round(ante0 / dados0, 2))
        print(statics.data_aprox.format((ante0 / dados0) - 1))
        comp0 = statics.data_aprox.format((ante0 / dados0) - 1).replace(".", ",")
    # Zero on 1
    if dados1 == 0:
        print(dados1, ante1)
        comp1 = statics.zero
    else:
        print(round(ante1 / dados1, 2))
        print(statics.data_aprox.format((ante1 / dados1) - 1))
        comp1 = statics.data_aprox.format((ante1 / dados1) - 1).replace(".", ",")
    # Zero on 2
    if dados2 == 0:
        print(dados2, ante2)
        comp2 = statics.zero
    else:
        print(round(ante2 / dados2))
        print(statics.data_aprox.format((ante2 / dados2) - 1))
        comp2 = statics.data_aprox.format((ante2 / dados2) - 1).replace(".", ",")
    # Zero on 3
    if dados3 == 0:
        print(dados3, ante3)
        comp3 = statics.zero
    else:
        print(round(ante3 / dados3))
        print(statics.data_aprox.format((ante3 / dados3) - 1))
        comp3 = statics.data_aprox.format((ante3 / dados3) - 1).replace(".", ",")
    

    
    # 0
    if comp0[statics.zero_rlen:] == statics.zero:
        comp0 = statics.zero
        ico0 = "neutro"
        res0 = "sem alteração desde a última atualização"
    elif comp0[0] == '-':
        ico0 = "negativo"
        res0 = "abaixo desde a última atualização"
    else:
        ico0 = "positivo"
        res0 = "acima desde a última atualização"

    # 1
    if comp1[statics.zero_rlen:] == statics.zero:
        comp1 = statics.zero
        ico1 = "neutro"
        res1 = "sem alteração desde a última atualização"
    elif comp1[0] == '-':
        ico1 = "negativo"
        res1 = "abaixo desde a última atualização"
    else:
        ico1 = "positivo"
        res1 = "acima desde a última atualização"

    # 2
    if comp2[statics.zero_rlen:] == statics.zero:
        comp2 = statics.zero
        ico2 = "neutro"
        res2 = "sem alteração desde a última atualização"
    elif comp2[0] == '-':
        ico2 = "negativo"
        res2 = "abaixo desde a última atualização"
    else:
        ico2 = "positivo"
        res2 = "acima desde a última atualização"

    # 3
    if comp3[statics.zero_rlen:] == statics.zero:
        comp3 = statics.zero
        ico3 = "neutro"
        res3 = "sem alteração desde a última atualização"
    elif comp3[0] == '-':
        ico3 = "negativo"
        res3 = "abaixo desde a última atualização"
    else:
        ico3 = "positivo"
        res3 = "acima desde a última atualização"


    return render_template('index.html', dados0=dados0, dados1=dados1, dados2=dados2, dados3=dados3, comp0=comp0, comp1=comp1, comp2=comp2, comp3=comp3, res0=res0, res1=res1, res2=res2, res3=res3, ico0=ico0, ico1=ico1, ico2=ico2, ico3=ico3)

@app.route('/Graficos')
def especific():
    div_html = grafico("Temperatura")
    div_html1 = grafico("Umidade solo") 
    div_html2 = grafico("Umidade Ambiente") 
    div_html3 = grafico("Volume Água (L)") 
    return render_template('grafico.html', plotly_div=div_html, plotly_div1=div_html1, plotly_div2=div_html2, plotly_div3=div_html3)


@app.route('/Baixar', methods=['GET', 'POST'])
def tabela():
    gerar_tabela()
    return send_from_directory(directory='static', path='relatorio.xlsx', as_attachment=True) 



@app.route('/Importar', methods=['GET', 'POST'])
def upload_file():
    if 'arquivo_csv' not in request.files:
        print("Arquivo não encontrado")
        return redirect(request.url)
    file = request.files['arquivo_csv']
    if file.filename == '':
        print("Nenhum arquivo selecionado")
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"Arquivo salvo em: {filepath}")
        criar_banco()
        return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)