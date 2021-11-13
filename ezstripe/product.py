class product_class():
    def __init__(self):
        load_dotenv()
        stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
        self.stripe = stripe
        self.context={}
        
    def list(self, limit=None):
        if limit == None:
            self.context=self.stripe.Product.list(limit=limit)
            return self.context
        self.context=self.stripe.Product.list()
        return self.context
        

    def retrieve(self, id):
        self.stripe.Product.retrieve()

    def modify(self, id, data=None):
        return id
    # modified = self.stripe.Product.modify(
    #     product_id,
    #     name = d['name'],
    #     active = d['active'],
    #     description = d['description'],
    #     metadata=d['metadata']
    # )
    # print(f"MODIFIED47: {modified}")
    # return modified