from django.db import models

class Kitchen_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.Amazon_Price()
    objects = models.Manager()

class Tv_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.Amazon_Price()
    objects = models.Manager()


class Laptop_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.Amazon_Price()
    objects = models.Manager()

class Tablets_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.Amazon_Price()
    objects = models.Manager()

class Home_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    sathiya_price = models.CharField(max_length=20,default='')
    vasanth_price = models.CharField(max_length=20,default='')
    darling_price = models.CharField(max_length=20, default='')
    viveks_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
#     # def __str__(self):
#     #     return self.Amazon_Price()
#     objects = models.Manager()
class Access_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.Amazon_Price()
    objects = models.Manager()

class Mobiles_model(models.Model):
    product_id = models.CharField(max_length=20, default='')
    item_code = models.CharField(max_length=20, default='')
    model_name = models.CharField(max_length=100,default='')
    poorvika_price =models.CharField(max_length=20, default='')
    flipkart_price = models.CharField(max_length=20, default='')
    amazon_price = models.CharField(max_length=20, default='')
    croma_price = models.CharField(max_length=20, default='')
    vijay_price = models.CharField(max_length=20, default='')
    reliance_price = models.CharField(max_length=20, default='')
    #     return self.Amazon_Price()
    objects = models.Manager()

# class flipkart_models(models.Model):
#     Item_Code = models.CharField(max_length=20, default='')
#     Model_Name = models.CharField(max_length=100, default='')
#     Flipkart_Urls = models.CharField(max_length=1000 , default='')
#     Flipkart_Price = models.CharField(max_length=20, default='')
#     Flipkart_Name = models.CharField(max_length=100, default='')
#     seller_1 = models.CharField(max_length=20, default='')


