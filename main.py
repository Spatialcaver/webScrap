import csv
from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com.br/s?k=livros&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    produtos = soup.find_all('div', class_='a-section a-spacing-base')

    file = open('export_data.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['produto ' , 'preco']
    writer.writerow(headers)

    for headline in produtos:
        produto = headline.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()

        preco = headline.find('span', class_='a-offscreen').text.strip()
        
        row = [produto, preco]
        writer.writerow(row)

        print('produto: ', produto , '|', preco) 
    file.close()
    print("deu tudo certo meu chapa!")

else:
    print('falha ao acessar pagina', response.status_code)
