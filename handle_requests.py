import requests
import json

class db:
    def __init__(self):
        self.headers = {
    'X-API-KEY': 'neurelo_9wKFBp874Z5xFw6ZCfvhXQ1/XI/KtLlq7fMc5VcSVfYTeNSTXWmqNBY5nfpVBoFGZUFMWsjJzvdLY6V+7TUXBMDy38/yheOlpk5ZBF5C2KZxQ418juR/E1t8COChJUi/75YLsZreGpwWZhRMrJzAd5Tt9vKUh4tUXwXZ5vL3UJA+enhrlqga/gGAM8AiZAmZ_5svMbamdaY5uSpuHcxrGffYR+fuiVk6GflZV9oNBlRE=',
        'Content-Type': 'application/x-www-form-urlencoded'
}
        self.api = "https://us-west-2.aws.neurelo.com"

    def get(self, api_point, params):
        if api_point[0] != '/':
            api_point = '/' + api_point
        return requests.get(self.api + api_point, params=params, headers=self.headers).json()
    
    def post(self, api_point, params, data):
        if api_point[0] != '/':
            api_point = '/' + api_point
        print(self.api + api_point)
        return requests.post(self.api + api_point, params=params, headers=self.headers, data=data).json()

    def delete(self, api_point, params):
        response = requests.delete(self.api + api_point, params=params,headers=self.headers)

        
    
    def get_login(self, username, password):
        params = {
            'username': username,
            'password': password,
        }
        response = self.get('/custom/get_login?', params)['data']['cursor']['firstBatch']
        return response
    
    def admin_table(self):
        params = ""
        response = self.get('/rest/Orders', params)['data']
        print(response)

    def view_company_products(self, company):
        params = {
    'filter': '{\n  "company_name": {\n    "equals": "c1"\n  }\n}',
}
        response = self.get('/rest/Orders?', params=params)
        print(response)


    def add_product(self, stock: int, origin_country, username, product_description, product_name):
        data = {
            "stock":stock,
            "origin_country":origin_country,
            "username": username,
            "product_description": product_description,
            "product_name": product_name
            }

        response = self.post("/rest/Products/__one?", params="", data=str(data))
    
    def get_user_orders(self, username):
        params = {'username': username}
        responses = self.get("/custom/get_users_orders?", params=params)['data']['cursor']['firstBatch']
        print(responses)
        
    def get_products(self):
        responses = self.get("/rest/Products", params="")
        return responses["data"]
    
    def add_to_cart(self, product, username, amount: int):
        data = {
            "product_name":product["product_name"],
            "quantity": amount,
            "shipping_country": product["country"],
            "username": username,
            "company_name": product["username"]
            }
        response = self.post("/rest/Orders/__one?", data=json.dumps(data), params="")
        print(response)
    
    def del_from_cart(self, product_id):
        response = self.delete("/rest/Orders/"+str(product_id), "")
        print(response)
        