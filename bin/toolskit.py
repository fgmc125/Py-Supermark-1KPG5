from datetime import datetime
import os

from mysqlhelper.Conector import Conexion


def sele():
    # para hacer scraping
    import os
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    import time
    import pandas
    from webdriver_manager.chrome import ChromeDriverManager

    # Opciones de navegacion
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)

    # Inicializamos el navegador
    driver.get('https://diaonline.supermercadosdia.com.ar/')

    list_categories = list()
    list_categories_descript = [
        """Encontrá la mayor variedad y el mejor precio en productos de Almacén en la tienda online de Supermercados Dia. 
        Contamos con productos de todo tipo para mantener tu alacena completa. aceites de girasol, maíz y oliva, 
        o aderezos como acetos, vinagres y limón. Tenemos conservas de frutas, pescados y vegetales, pastas secas, arroz, 
        fideos de todo tipo, legumbres, harinas ¡Y mucho más! La alimentación es importante para una vida saludable. 
        Encontrá todo lo que necesites en DIA Online.""",

        """Encontrá la mayor variedad y el mejor precio en productos para el Desayuno en la tienda online de 
        Supermercados Dia. El desayuno es la comida más importante del día. En esta sección vas a poder encontrar todo lo 
        que necesites para un desayuno fácil, rico y completo para toda la familia. Galletitas dulces y saladas, 
        además de cereales. Infusiones como café, té, yerba mate y endulzantes, azúcar y edulcorantes de todo tipo. En la 
        sección para untar, encontrarás dulces de leche, mermeladas y quesos untables. Por último, en nuestra sección de 
        panadería, tenemos pan de molde, facturas, medialunas y otros panificados para tu Desayuno. ¡Descubrilo!""",

        """Encontrá el mejor precio en productos Frescos en la tienda online de Supermercados Dia para que tu familia 
        tenga una alimentación completa, nutritiva y saludable. Encontrá en nuestros productos Frescos la más amplia 
        variedad de productos seleccionados en lácteos como yogures descremados, enteros, mantecas y margarinas, 
        entre otros productos. También podrás encontrar leche entera, descremada, leches vegetales y en polvo.En nuestra 
        sección de Frutas y Verduras, encontrarás gran variedad de productos frescos, frutos secos y huevos. También 
        contamos con Carnicería de primer nivel y una fiambreria completa con quesos, salames, jamones ¡Y mucho más!.""",

        """Encontrá la mejor selección de frutas y verduras. Contamos con una gran variedad de frutas: palta, banana, 
        manzana, naranja. Y con las mejores verduras: cebolla, anco, zanahoria, papa y más. Nuestros productos son 
        frescos y de primerísima calidad.""",

        """Encontrá la mayor variedad y el mejor precio en Bebidas en la tienda online de Supermercados Dia. Vas a poder 
        encontrar grandes ofertas de aguas con gas, sin gas y saborizadas. También descuentos imperdibles en gaseosas de 
        todo tipo, jugos listos, en polvo y concentrados, y bebidas isotónicas. En la sección de bebidas alcohólicas 
        podrás encontrar aperitivos, bebidas blancas como vodka, gin, ron o whisky. También contamos con precios bajos en 
        licores, cervezas de todo tipo. Por último, en nuestra bodega descubrirás gran variedad y precios de vinos 
        blancos, rosados y tintos, además de espumantes de primera calidad, ideal para cada ocasión y miembro de la 
        familia.""",

        """Encontrá la mayor variedad y el mejor precio en productos Congelados en la tienda online de Supermercados Dia. 
        Para que tu rutina sea siempre más simple, rápida y flexible, la mejor solución es planificar tus comidas. En 
        esta sección podrás encontrar congelados rebozados como milanesas de pescado, pollo, soja o nuggets y bastones 
        congelados. A su vez, contamos con una amplia variedad de helados de crema y de fruta. Contamos con una 
        pescadería completa y vegetales congelados, pizzas y empanadas para tener siempre a mano en el freezer y, 
        por supuesto, hamburguesas y medallones de carne, pollo y pescado.""",

        """Encontrá el mejor precio en productos de Limpieza en la tienda online de Supermercados Dia. Mantener la 
        limpieza y orden del hogar es fundamental para el cuidado de tu familia. Descubrí una amplia variedad de 
        productos de limpieza para el hogar y para la ropa empezando por papelería, donde encontrarás pañuelos, 
        papel higiénico, rollos de cocina y servilletas. A su vez, contamos con limpiadores como lavandina, limpiadores 
        de piso y lustramuebles. También podrás encontrar detergentes, esponjas y guantes para la limpieza de la cocina y 
        accesorios de limpieza como escobas, secadores, bolsas de residuos y una amplia variedad de trapos.""",

        """Encontrá la mayor variedad y el mejor precio en productos de Perfumería en la tienda online de Supermercados 
        Dia. Descubrí gran cantidad de productos para la higiene personal, cuidado del pelo, bucal y corporal. En esta 
        sección podrás encontrar todo tipo de productos para mantener saludable tu boca, con cepillos de dientes, 
        pastas dentífricas, enjuague bucal e hilo dental. También contamos con cremas corporales, desodorantes femeninos 
        y masculinos y productos de limpieza facial. A su vez, tenemos una amplia variedad de marcas y productos para el 
        cuidado del pelo con todo tipo de shampoo, acondicionadores, gel y tratamientos de caída del cabello. En la 
        sección Farmacia podrás comprar algodón, hisopos, alcohol y talco, entre otros. También tenemos jabones en barra, 
        líquidos y antisépticos. Por último te acercamos los mejores productos de protección femenina.""",

        """Encontrá la mayor variedad y el mejor precio en productos para Bebés y Niños en la tienda online de 
        Supermercados Dia. Todo lo que tu hijo necesita en un solo lugar. Contamos con gran variedad de Pañales y toallas 
        húmedas. También podrás encontrar colonias, aceites, cremas, jabones, talcos y mucho más para el cuidado y la 
        higiene de tus hijos.En cuanto a la alimentación de los más chicos, contamos con leches infantiles, papillas y 
        otras opciones para darles de comer algo rico y sano. Finalmente, encontrá una amplia variedad de juegos y 
        juguetes y todo tipo de indumentaria para niños. Disfrutá de las mejores ofertas para tu hijo al mejor precio. 
        Dale lo mejor a tu hijo.""",

        """Encontrá la mayor variedad y el mejor precio en productos para las Mascotas en la tienda online de 
        Supermercados Dia. Tu mascota necesita del mayor cuidado, por eso, en esta sección vas a encontrar variedad de 
        productos para alimentar a las mascotas de tu hogar como alimentos húmedos, secos y snacks especialmente 
        diseñados para gatos y para perros. Encontrá las mejores ofertas de las marcas número uno de alimentos y 
        accesorios para tus mascotas como Gati, Dog Chow, Dogui, Bacán y Pedigree, entre otros. Sabemos lo importante que 
        es que tus animales se sientan sanos, fuertes, nutritivos y que le puedas dar siempre lo mejor.""",

        """En nuestra categoría de golosinas y alfajores vas encontrar cientos de productos dulces: mantecol, 
        garrapiñadas, turrones, chocolates, alfajores y más de las mejores marcas; Dia, Arcor, Terrabusi, Nestlé, 
        Bonafide. Tentate con algo dulce y compralo al mejor precio en Dia.""",

        """Sin descripción""",

        """Encontrá la mayor variedad y el mejor precio en productos de Electro Hogar en la tienda online de 
        Supermercados Dia. En esta sección podrás encontrar electrodomésticos como aspiradoras, planchas y cocinas y 
        hornos de todo tipo y tamaño. También contamos con lavarropas, secarropas, campanas, purificadores y heladeras 
        con y sin freezer. Por otro lado, tenemos ventiladores y calefacción para tener una mejor climatización en tu 
        hogar y una amplia gama de electrodomésticos para la cocina. No lo dudes más, equipa tu casa con los mejores 
        electrodomésticos que la tienda online de Dia tiene para vos."""
    ]
    list_subcategories = list()

    WebDriverWait(driver, 5) \
        .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                            '.diaio-site-onboarding-1-x-sob_close'))).click()

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((
        By.XPATH,
        '/html/body/div[2]/div/div[1]/div/div[1]/div/div[4]/div/div[1]/button'
    ))).click()

    texto = driver.find_element(By.CSS_SELECTOR, '.diaio-store-3-x-menuContainer.list.ma0.pa0.pb3.br.b--muted-4')
    list_categories = texto.text.split('\n')
    print(list_categories, len(list_categories))
    print(list_categories_descript, len(list_categories_descript))

    driver.quit()


class EmailSender:
    def __init__(self, __email_from, __password):
        self.__email_from = __email_from
        self.__password = __password

    def send_mail(self, rcpt_to, subject, content):
        from email.message import EmailMessage
        import ssl
        import smtplib

        emailMessage = EmailMessage()
        emailMessage['From'] = self.__email_from
        emailMessage['To'] = rcpt_to
        emailMessage['Subject'] = subject
        emailMessage.set_content(content)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail,com', 465, context=context) as smtp:
            smtp.login(self.__email_from, self.__password)
            smtp.sendmail(self.__email_from, rcpt_to, emailMessage.as_string())


def json_to_mysql():
    import json

    json_files = os.listdir('../db_json')
    contador = 0
    for file in json_files:
        print('../db_json/' + str(file))
        with open('../db_json/' + file, encoding="utf8") as json_file:
            data = json.load(json_file)

        for art in data:
            contador += 1

            print("Productos cargados:", contador, art['name'], art['category'])
            __save(art)


def __save(art):
    __connector = Conexion()
    if __connector.is_connected():
        sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.product_db WHERE name = '" + art['name'].title() + "'"
        data = __connector.run_query(sql)
        if data:
            print(" * ¡ERROR! El producto ingresado ya existe.")
        else:
            sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.category_db WHERE name = '" + art['category'] + "'"
            id_category = __connector.run_query(sql)

            id_category = id_category[0][0]

            sql = """INSERT INTO bhhj3cug6bdknptqdl7k.product_db (
                                                        id,
                                                        name,
                                                        description,
                                                        price,
                                                        current,
                                                        minimum,
                                                        maximum,
                                                        image,
                                                        created,
                                                        updated,
                                                        new,
                                                        family_id
                                                        )
                                                        VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

            price_prod = art['price'][2:art['price'].index(',')+3]
            chars = '.'

            price_prod = price_prod.translate(str.maketrans('', '', chars))
            price_prod = price_prod.replace(',', '.')
            price_prod = float(price_prod)
            data = art['name'].title(), \
                   art['description'], \
                   price_prod, \
                   10, \
                   0, \
                   0, \
                   None, \
                   datetime.now().strftime('%Y-%m-%d %H:%M:%S'), \
                   datetime.now().strftime('%Y-%m-%d %H:%M:%S'), \
                   True, \
                   id_category

            __connector.run_query(query=sql, data=data)
            __connector.close()
    else:
        print(" * ¡ERROR! No se pudo realizar la coneccion.")

if __name__ == "__main__":
    json_to_mysql()