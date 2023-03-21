from django.shortcuts import render
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import *
from http.client import HTTPResponse
import datetime



date = datetime.date.today().strftime("%d-%#m-%Y")

def Import_excel(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfiles = request.FILES['myfile']
        fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfiles)              
        empexceldata = pd.read_excel(myfiles)        
        dbframe = empexceldata
        
        x = []
        print("F_name",myfiles)
        file_name = str(myfiles)
        x = file_name.split()
        print(x[0])
        # if x[0] == "Kitchen":
        #     for dbframe in dbframe.itertuples():
        #         # if myfiles =="Kitchen Appliance Price List" + date + ".xlsx":             # if myfiles == "1.xlsx":
        # #         # if myfiles == "1.xlsx":
        # #             # print(myfiles)
                    
        #             obj = Kitchen_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
        #                                             poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
        #                                             amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
        #                                             vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
        #                 # print("File has been uploded-1", "*" * 10)
        #             obj.save()
        
        for dbframe in dbframe.itertuples():
            # if myfiles =="Kitchen Appliance Price List" + date + ".xlsx":             # if myfiles == "1.xlsx":
            # if myfiles == "1.xlsx":
                # print(myfiles)
                if x[0] == "Kitchen":
                
                    obj = Kitchen_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                        # print("File has been uploded-1", "*" * 10)
                    obj.save()
                elif x[0] == "Tv":
                
                    obj = Tv_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                        # print("File has been uploded-1", "*" * 10)
                    obj.save()
                elif x[0] == "Laptop":
                     
                    obj = Laptop_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                     
                    obj.save()
                elif x[0] == "Mobiles":
                     
                    obj = Mobiles_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                     
                    obj.save()   
                elif x[0] == "Tablets":
                     
                    obj = Tablets_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                     
                    obj.save()
                elif x[0] == "Accessories":
                     
                    obj = Access_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,flipkart_price=dbframe.Flipkart_Price,
                                                    amazon_price=dbframe.Amazon_Price,croma_price=dbframe.Croma_Price,
                                                    vijay_price=dbframe.Vijay_Price,reliance_price=dbframe.Reliance_Price)
                     
                    obj.save()
                elif x[0] == "Home_appliances":
                     
                    obj = Home_model.objects.create(product_id=dbframe.Product_ID,item_code=dbframe.Item_Code,model_name=dbframe.Model_Name,
                                                    poorvika_price=dbframe.Poorvika_Price,sathiya_price=dbframe.Sathiya_Price,
                                                    vasanth_price =dbframe.Vasanth_Price,darling_price=dbframe.Darling_Price,
                                                    viveks_price=dbframe.Viveks_Price,croma_price=dbframe.Croma_Price,
                                                    amazon_price=dbframe.Amazon_Price,flipkart_price=dbframe.Flipkart_Price,reliance_price=dbframe.Reliance_Price)
                     
                    obj.save()
                else:
                    pass


            
        return render(request, 'Import_excel_db.html', {
                'uploaded_file_url': uploaded_file_url})
    return render(request, 'Import_excel_db.html',{})
        
            
            
            
    #             obj = Tv_model.objects.create(Product_ID=dbframe.Product_ID,Item_Code=dbframe.Item_Code,Model_Name=dbframe.Model_Name,
    #                                            Poorvika_Price=dbframe.Poorvika_Price,Flipkart_Price=dbframe.Flipkart_Price,
    #                                            Amazon_Price=dbframe.Amazon_Price,Croma_price=dbframe.Croma_Price,
    #                                            Vijay_Price=dbframe.Vijay_Price,Reliance_Price=dbframe.Reliance_price)
    #             obj.save()
  
    #     return render(request, 'Import_excel_db.html', {
    #     'uploaded_file_url': uploaded_file_url})
    # return render(request, 'Import_excel_db.html',{})    
        
            
            
           
                                                  
            #     obj.save()
            # return render(request, 'Import_excel_db.html', {
            # 'uploaded_file_url': uploaded_file_url
            # })   
       
    
    
    

    # return render(request, 'Import_excel_db.html',{})


# def Import_excel_TV(request):
     
#     if request.method == 'POST' and request.FILES['myfile']:      
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)              
#         empexceldata = pd.read_excel(filename)        
#         dbframe = empexceldata
        
