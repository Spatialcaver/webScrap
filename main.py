import csv
import BeautifulSoup
import requests

url = "https://www.magazineluiza.com.br/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    produtos = soup.find_all('div', class_='pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5')

    file = open('export_data.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['produto ',  'preço']
    writer.writerow(headers)

    for headline in produtos:
        produto = headline.find('div', class_='commerce_columns_item_caption').text.strip()
        preco = headline.find('div', class_='sc-fqkvVR dzACBc sc-bfhvDw eCuCbE').text.strip()
        
        row = [produto, preco]
        writer.writerow(row)

        print('produto: ', produto, ' |', preco) 
    file.close()
    print("deu tudo certo meu chapa!")

else:
    print('falha ao acessar pagina', response.status_code)