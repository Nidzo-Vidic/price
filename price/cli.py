import click
import mechanicalsoup

@click.command()
@click.option('--radius', '-r', default=5, help='Radius der Tankstellen')
@click.option('--city', '-c', required=True, help='Stadt')
@click.option('--type', '-t', required=True, help='Diesel, E10, E5, SuperPlus und die kleingeschriebenen Varianten')
def price(radius, city, type):

    types = {
        'diesel': 3,
        'e10': 5,
        'super': 6,
        'e5': 7
    }

    typenumber = types.get(type)

    city = city.replace(' ', '+')
    url = f'https://www.clever-tanken.de/tankstelle_liste?lat=&lon=&ort={city}&spritsorte={typenumber}&r={radius}'

    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True
    )

    browser.open(url)
    page = browser.get_current_page()
    result_table = page.find_all('div', class_='list-card-container d-flex background-white-gray')

    click.secho(f'{"":-^95s}', fg='white', bold=True)
    click.secho(f'{"Preis":<6} | {"Tankstelle":<16} | {"Stadt":<23} | {"Straße":<30} | {"Radius":<10}', fg='white', bold=True)
    click.secho(f'{"":-^95s}', fg='white', bold=True)

    for patrol in result_table:
        price = patrol.find(class_='price-text price text-color-ct-blue')
        if price == None:
            return
        price = price.get_text().strip()
        patrol_name = patrol.find(class_='fuel-station-location-name').get_text().strip()
        patrol_street = patrol.find(class_='fuel-station-location-street').get_text().strip()
        patrol_city = patrol.find(class_='fuel-station-location-city').get_text().strip()
        patrol_radius = patrol.find(class_='fuel-station-location-distance d-flex justify-content-end').get_text().strip()
        click.secho(f'{price:<6} | {patrol_name[0:16]:<16} | {patrol_city:<23} | {patrol_street:<30} | {patrol_radius}', fg='white')

if __name__ == '__main__':
    price()
