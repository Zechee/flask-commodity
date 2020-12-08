from models.user import UserModel
from models.address import AddressModel
from models.order import OrderModel, OrderItemModel
from models.category import CategoryModel
from models.product import ProductModel
from schemas.order import OrderItemSchema, OrderSchema
from schemas.address import AddressSchema
from schemas.product import ProductSchema
from schemas.category import CategorySchema
from schemas.user import UserSchema

from faker import Faker

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import calendar, random

def add_users(username, fullname, timezone="+8"):
    user = UserModel(
        username=username, 
        fullname=fullname, 
        timezone=timezone
    )
   
    user.set_password('test')
    user.save_to_db()
    return user

def generate_username():
    faker = Faker()
    return faker.profile()['username']

def generate_fullname():
    faker = Faker()
    return faker.name()

def generate_text():
    faker = Faker()
    return faker.paragraph(nb_sentences=5)

def generate_address():
    faker = Faker()
    return faker.address()

def generate_phone_number():
    faker = Faker()
    return faker.phone_number()

def generate_image_url():
    faker = Faker()
    return faker.image_url(width=None, height=None)

def generate_workingdays(start_date, nums_of_month):

    current_month = date(start_date.year, start_date.month, 1)

    days = []
    for i in range(nums_of_month):
        current_day = current_month + relativedelta(months=i)
        _, days_in_month = calendar.monthrange(current_day.year, current_day.month)
        # print(current_day, days_in_month)
        days.append({ 'current_day':current_day, 'days':days_in_month})

    return days

def add_user(db):
    # add a first users 'maxazure': 'test'
    # first_user = add_users(username='maxazure', fullname='Jay Liu', timezone="+8")
    # print(first_user.id, first_user.fullname)

    # add other 10 users
    for _ in range(1,11):
        user = add_users(username=generate_username(), fullname=generate_fullname(), timezone="+8")
        print(user.id, user.fullname)

def add_category(db):
    categories = []
    for i in range(random.randint(1,10)):
        category = CategoryModel(
            name = generate_username(), 
            parent_id = random.randint(1,2), 
            depth = random.randint(1,2), 
            order = random.randint(1,4)
        )
        categories.append(category)

    db.session.bulk_save_objects(categories)
    db.session.commit()

def add_product(db):
    products = []
    for i in range(random.randint(1,10)):
        product  = ProductModel(
            name = generate_fullname(),
            photo = generate_image_url(), 
            intro = generate_text(), 
            on_sale = random.randint(0,1), 
            category_id = random.randint(1,20), 
            price = random.randint(1,500), 
            market_price = random.randint(1,500), 
            status = random.randint(0,1)
        )
        products.append(product)

    db.session.bulk_save_objects(products)
    db.session.commit()

def add_address(db):
    addresses = []
    for i in range(random.randint(1,10)):
        address = AddressModel(
            user_id = random.randint(1,20), 
            name = generate_fullname(), 
            number = generate_phone_number(), 
            address = generate_address()
        )   
        addresses.append(address)
    
    db.session.bulk_save_objects(addresses)
    db.session.commit()  

def add_orderitem(db):
    orderitems = []
    for i in range(random.randint(1,10)):
        orderitem = OrderItemModel(
            order_id = random.randint(1,20), 
            product_id = random.randint(1,20), 
            price = random.randint(1,500), 
            quantity = random.randint(1,10)
        )
        orderitems.append(orderitem)

    db.session.bulk_save_objects(orderitems)
    db.session.commit()

def add_order(db):
    orders = []
    for i in range(random.randint(1,10)):
        order = OrderModel(
            user_id = 1, 
            status = "Order Completed !", 
            address = generate_address(), 
            total_amount = random.randint(1,1000),
        )
        orders.append(order)

    db.session.bulk_save_objects(orders)
    db.session.commit()


def init_database(db):
    add_user(db)

    add_category(db)
    add_product(db)
    add_address(db)
    add_orderitem(db) 
    add_order(db)

        # days_of_months = generate_workingdays(date(2020,1,1), 14)
        # for mon in days_of_months:
        #     reports =[]
        
        #     for day in range(mon['days']):
        #         current = mon['current_day'] + relativedelta(days=day)
        #         if current.weekday()<5:
        #             report = ReportModel(plan='{} test for plan content'.format(user.username), user_id=user.id)
        #             report.created_at = current
        #             # report.save_to_db()
    
        #             for i in range(8):
        #                 report_item = ReportItemModel(duration=1, content='{} hour for test. {}'.format(i, generate_text()))
        #                 report_item.report_id =report.id
        #                 report_item.created_at = report.created_at
        #                 report.report_items.append(report_item)
        #                 # report_item.save_to_db()
        #             reports.append(report)
        #     db.session.bulk_save_objects(reports)
        #     db.session.commit()
        #     print(mon, user.id)






