# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()


def create_db_table():
    # Create table
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS category_table
        (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL
        );
        CREATE TABLE  IF NOT EXISTS items_table
        (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          description TEXT,
          price INTEGER,
          category_id INTEGER,
          FOREIGN KEY (category_id) REFERENCES category_table (id)
        );
        CREATE TABLE IF NOT EXISTS order_table
        (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          time_order DATETIME NOT NULL,
          items TEXT NOT NULL,
          adres TEXT NOT NULL,
          price_order INTEGER
        );
        """
    )
    conn.commit()


def filling_base():
    # INSERT Category
    cursor.executescript(
        """
        INSERT INTO category_table VALUES (1, 'Постная Выпечка');
        INSERT INTO category_table VALUES (2, 'Домашняя Выпечка');
        INSERT INTO category_table VALUES (3, 'Сытный Вечер');
        INSERT INTO category_table VALUES (4, 'Сладкий Полдник');
        """
    )
    conn.commit()
    # INSERT Items
    cursor.executescript(
        """
        INSERT INTO items_table VALUES (
          1,
          'Миндальный круассан',
          'Круассан в Волконском - такой же, как и во Франции. В нашем круассане насчитывается 260 слоев теста,
          он изготавливается из пшеничной муки, свежайшего сливочного масла и яиц.
          Начинка из миндальной муки крупного помола.',
          150,
          4
        );
        INSERT INTO items_table VALUES (
          2,
          'Эклер (клубника)',
          'Традиционное французское пирожное из нежного заварного теста и легкого клубнично бальзамического крема.
          Покрыт фирменной клубничной глазурью.',
          100,
          4
        );
        INSERT INTO items_table VALUES (
          3,
          'Тарталетка «Малина»',
          'Изящная тарталетка с малиной приготовлена из рассыпчатого песочного теста с добавлением миндальной муки
          и наполнена кремом из густых сливок. Украшена свежими ягодами, посыпанными сахарной пудрой.
          Восхитительное пирожное станет чудесной парой к чашечке утреннего эспрессо или ароматному чаю.',
          200,
          4
        );
        INSERT INTO items_table VALUES (
          4,
          'Пирожное «Картошка»',
          'Традиционное пирожное, приготовленное в лучших традициях советской кухни. Нежный бисквит,
          перетёртый в мелкую крошку, прекрасно сочетается со сливочным кремом, обладает насыщенным
          вкусом тёмного шоколада с нотками терпкого миндаля и сладкой ванили.',
          150,
          4
        );
        INSERT INTO items_table VALUES (
          5,
          'Пирог с семгой и рисом',
          'Сытный пирог из сдобного слоёного теста на сливочном масле — нежный и ароматный.
          Для сочной начинки используется исключительно охлажденная сёмга и рис, приправленные ароматным укропом.
          Аппетитный пирог с золотистой корочкой превратит ваше чаепитие в настоящий праздник, им с
          удовольствием полакомятся как дети, так и взрослые. Будьте уверены, он будет съеден до последней крошки.
          Домашний вкус пирога сделает вечер в кругу семьи по-настоящему тёплым и уютным.',
          245,
          3
        );
        INSERT INTO items_table VALUES (
          6,
          'Хычин с мясом',
          'Хычин — блюдо национальной кухни народов Северного Кавказа.
          Высшим гостеприимством хозяйки дома в прошлом считалось приглашение «на хычины».
          Это одно из самых почётных блюд в списке мучных кушаний карачаево-балкарской кухни.
          Любое застолье было просто немыслимо без хычина. Эта традиция сохраняется и в настоящее время.
          Используют его как хлеб и как самодостаточную закуску. Лепёшка из очень тонкого теста наполнена
          сочным фаршем из говядины, в который добавлены петрушка и репчатый лук.
          Особую пикантность начинке придаёт свежий перец чили.
          Порадуйте своих близких угощением к горячему ароматному чаю.
          Хычин — невероятно, по-кавказски, вкусный и сытный.',
          270,
          3
        );
        INSERT INTO items_table VALUES (
          7,
          'Курник',
          'Классическое блюдо полюбилось многим гурманам. Аппетитно приготовленное куриное мясо в сочетании с
          нежным рисом дополнено воздушным тестом. Идеальное сочетание компонентов делает выпечку сытной и вкусной.
          Ее любят и взрослые, и дети. Благодаря натуральным ингредиентам блюдо получается полезным.
          Шпик, зелень и майонез придают изысканности изделию и раскрывают настоящий вкус.
          Тонкое, хрустящее тесто сохраняет начинку сочной и ароматной.',
          250,
          3
        );
        INSERT INTO items_table VALUES (
          8,
          'Ватрушка королевская',
          'Сладкая песочная крошка и начинка из перетертого с сахаром и яйцом творога идеально сочетаются между собой.
          Хрустящая основа и верхушка с нежной прослойкой из творожного мусса — в меру сладкий,
          не приторный пирог, который очарует с первого кусочка. Яркий, красивый срез этого десерта
          никого не оставит равнодушным.',
          244,
          2
        );
        INSERT INTO items_table VALUES (
          9,
          'Пирог Трёхслойный с черносливом, абрикосом и лимонным джемом',
          'Восхитительное сочетание песочно-дрожжевого теста и фруктовой начинки с черносливом, выложенной слоями.
          Абрикосовая, лимонная начинка из натуральных спелых фруктов гармонично сочетаются друг с другом.
          Легкая кислинка и цитрусовый аромат лимона оттеняет сладость чернослива и кураги, завершая
          палитру вкуса пирога, делая его еще более ярким и насыщенным. Пирог декорирован песочной
          посыпкой и половинкой грецкого ореха.',
          270,
          2
        );
        INSERT INTO items_table VALUES (
          10,
          'Орешки со сгущенным молоком',
          'Орешки со сгущенным молоком в шоколадной глазури довольно простой, но очень вкусный и питательный десерт.
          Его вкус многим знаком с самого детства, так как родом он из СССР.
          Частенько мамы доставали «орешницы», и дом заполнял магически чарующий запах смеси вареной сгущенки и
          свежевыпеченного печенья.',
          255,
          2
        );
        INSERT INTO items_table VALUES (
          11,
          'Пирог осетинский с картофелем и грибами',
          'Сытный и очень вкусный осетинский пирог приготовлен по традиционному кавказскому рецепту из
          тонкого дрожжевого теста и щедро наполнен начинкой их нежного картофельного пюре и обжаренных
          с репчатым луком шампиньонов. В начинку добавлен чёрный молотый перец. Пирог — постный,
          сверху смазан в отличии от классического варианта растительным маслом, в его составе нет
          продуктов животного происхождения. Нежный осетинский пирог, подрумяненный в печи до золотистой
          корочки, отлично подходит к полднику или перекусу на работе, чаепитию в кругу семьи.',
          245,
          1
        );
        INSERT INTO items_table VALUES (
          12,
          'Треугольник со шпинатом',
          'Очень сочный и вкусный греческий треугольник приготовлен из хрустящего тонкого теста фило с
          ароматной нежнейшей начинкой из свежесобранного шпината, лука-порея и зелёного лука.
          Здоровый и питательный выбор для полноценного сытного обеда. Воздушный, мягкий и
          ароматный треугольник полностью изготовлен без продуктов животного происхождения,
          подходит для веганов и людей, которые соблюдают пост.',
          265,
          1
        );
        INSERT INTO items_table VALUES (
          13,
          'Троицкий пирог',
          'Постный пирог из дрожжевого теста с сытной начинкой из картофельного пюре,
          ароматных грибов и репчатого лука.',
          250,
          1
        );
        INSERT INTO items_table VALUES (
          14,
          'Пирог «Невский»',
          'Постный пирог с начинкой из отварного картофеля, грибов шампиньонов и зелени.
          Много начинки и вкусное тонкое постное тесто. Перед выпеканием смазываем пирог крепким чаем,
          после выпечки — растительным маслом. Питайтесь со вкусом, даже в пост.',
          290,
          1
        );
        """
    )
    conn.commit()


def select(sql='', line='*', table='*', where=''):
    try:
        if sql:
            cursor.execute(sql)
            result = cursor.fetchall()
        else:
            where = 'WHERE ' + where if where else ''
            sql_reqvest = f'SELECT {line} FROM {table} {where}'
            cursor.execute(sql_reqvest)
            result = cursor.fetchall()
        return result
    except sqlite3.OperationalError as err:
        print("ERROR_Select -", err)


conn.close()